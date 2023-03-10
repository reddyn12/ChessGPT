from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments


tokenizer = GPT2Tokenizer.from_pretrained("tokenizer")

#CHECK IF THIS HITS
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})



model = GPT2LMHeadModel.from_pretrained("smallModel").to("cuda")

s = '''1.d4 Nf6 2.Nc3 e6 3.e4 d5 4.e5 Nfd7 5.Nf3 c5 6.Bg5 Nc6 7.Bxd8 Nxd8 8.dxc5'''

s="1. e4 d6"
#s= '''9.'''

#s='''1.b3 e5 2.Bb2 Nc6 3.Nc3 Nf6 4.Nf3 d6 5.e3 g6 6.Bc4 Bg7 7.Nxe5 Nxe5 8.Nb5\\n'''

stoken = tokenizer.encode(s, return_tensors="pt").to("cuda")
# print(stoken)
beamOut = model.generate(
    stoken,
    max_length=200,
    num_beams=10,
    temperature=0.7,
    no_repeat_ngram_size=3,
    num_return_sequences=3,

    )
cnt = 0
for beam in beamOut:
    cnt = cnt +1
    print(cnt)
    out = tokenizer.decode(beam)
    print(out)

