#%%
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments



tokenizer = GPT2Tokenizer.from_pretrained("tokeniLabV3",unk_token="<unk>", eos_token="</N>", bos_token="<N>", pad_token="<pad>")

model = GPT2LMHeadModel.from_pretrained("iLabV3").to("cuda")


s = " 1."

def gen(game):
    stoken = tokenizer(game, return_tensors="pt").to("cuda")
    print(stoken)
    beamOut = model.generate(
        stoken["input_ids"],
        max_length=200,
        num_beams=10,
        temperature=0.7,
        no_repeat_ngram_size=3,
        num_return_sequences=3,

        )
    cnt = 0
    for beam in beamOut:
        cnt = cnt +1
        #print(cnt)
        out = tokenizer.decode(beam)
        print(out)
#%%
s = " 1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5"
stoken = tokenizer(s, return_tensors="pt").to("cuda")
print(stoken)
beamOut = model.generate(
    stoken["input_ids"],
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

#%%
s = " 1. c4 e5 2. Qa4 Nf6 3. g3 c6 4. Bh3 d5 5. cxd5 Nxd5 6. Nf3 Nd7 7. Na3 Nc5 8. Qc2 g6 9. Nxe5 Bg7 10. Ng4 h5 11. Ne3 Nxe3 12. fxe3 Qe7 13. Bxc8 Rxc8 14. b4"
gen(s)

# %%
