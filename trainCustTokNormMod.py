import customToken
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, TrainingArguments, Trainer, DefaultDataCollator
from datasets import load_dataset
import numpy as np
dpath = "dataPre/KingBase2019/kingCleanV2.pgn"


config = GPT2Config(
    vocab_size = len(customToken.tokens),
    bos_token = customToken.ex_token,
    eos_token = customToken.eos_token,
    pad_token = customToken.pad_token,
    bos_token_id = customToken.ex_token_id,
    eos_token_id=customToken.eos_token_id,
    n_layer=12,
    n_head=12,
)
print(len(customToken.tokens))
model = GPT2LMHeadModel(config).to("cuda")


dataset = load_dataset("text", data_files=dpath)
dataset = dataset["train"]

def encode(lines):
    ans = {}
    ans["input_ids"] = []
    ans["attention_mask"] = []
    for i in lines["text"]:
        #print(i)
        a = customToken.tokenize(i)
        
        ans["input_ids"]=ans["input_ids"]+a
        ans["attention_mask"]= ans["attention_mask"] +np.ones((len(a),), dtype=int).tolist()

    ans["attention_mask"] = [ans["attention_mask"]]
    ans["input_ids"] = [ans["input_ids"]]
    return ans
# def encode(lines):
#     ans = {}
#     for i in lines["text"]:
#     a = customToken.tokenizeArr(lines["text"])
    
#     ans["input_ids"] = a
#     ans["attention_mask"] = np.ones((len(a),), dtype=int)

#     return ans
dataset.set_transform(encode)

#data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False, pad_to_multiple_of=8)
data_collator = DefaultDataCollator()


training_args = TrainingArguments(
    output_dir="custTokenNormModel",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=5, #64
    save_steps=10000,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns=False,
)
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,

)


trainer.train()
trainer.save_model("custTokenNormModel")