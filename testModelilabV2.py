from statistics import mode
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments


tokenizer = GPT2Tokenizer.from_pretrained("tokenizerV2")

#CHECK IF THIS HITS
tokenizer.add_special_tokens({
    "eos_token": "<N",
    "bos_token": "\nN>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})



model = GPT2LMHeadModel.from_pretrained("iLabV2").to("cuda")
model.config.eos_token_id = 0

s = '''1.'''
#s= '''9.'''

stoken = tokenizer.encode(s, return_tensors="pt").to("cuda")
print(stoken)



greedy_output = model.generate(inputs = stoken, max_length=100)

print(tokenizer.decode(greedy_output[0], skip_special_tokens=False))
# print(stoken)
beamOut = model.generate(
    stoken,
    max_length=250,
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

# outs = model(**stoken)
# outs = outs[-1]
# print(''.join(str(e) for e in outs.logits))

