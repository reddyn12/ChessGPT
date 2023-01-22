from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments

from customTokenImp import CustByteLevelBPETokenizer
import torch
tokenizer = CustByteLevelBPETokenizer.from_file("tokenizerV2/vocab.json", "tokenizerV2/merges.txt")
#tokenizer = GPT2Tokenizer.from_pretrained("tokenizer")

# #CHECK IF THIS HITS
# tokenizer.add_special_tokens({
#     "eos_token": "</s>",
#     "bos_token": "<s>",
#     "unk_token": "<unk>",
#     "pad_token": "<pad>",
#     "mask_token": "<mask>"
# })
# torch.as_tensor()
# torch.tensor()

model = GPT2LMHeadModel.from_pretrained("smallModelV3").to("cuda")
model.eval()

s = '''1 . d4 '''
tokenizer.no_padding()

stoken = tokenizer.encode(s)
print(stoken)
print(stoken.tokens)
print(torch.tensor(stoken.ids))
temp = torch.as_tensor([stoken.ids],device="cuda")
#temp =temp.transpose(-1,0)

beamOut = model.generate(
    temp,
    max_length=200,
    num_beams=10,
    temperature=0.7,
    no_repeat_ngram_size=3,
    num_return_sequences=3,
    eos_token_id=0,
    pad_token_id=0,

    )
cnt = 0

for beam in beamOut:
    cnt = cnt +1
    print(cnt)
    beam=beam.tolist()
    nbeam = ""
    for i in beam:
        nbeam = nbeam +tokenizer.id_to_token(int(i))
        nbeam = nbeam +" "
    print(nbeam)

    out = tokenizer.decode(beam)
    print(out)
    break