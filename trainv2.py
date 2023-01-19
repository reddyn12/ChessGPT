#%%
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DefaultDataCollator,DataCollatorForLanguageModeling, DataCollatorWithPadding,Trainer, TrainingArguments
from tokenizers.implementations import ByteLevelBPETokenizer

from datasets import load_dataset, Dataset

from torch import device

dpath = "dataPre/KingBase2019/kingCleanV3.pgn"

tokenizer = ByteLevelBPETokenizer.from_file("tokenizerNewClean/vocab.json", "tokenizerNewClean/merges.txt")
tokenizer.enable_padding(pad_id=2)

#CHECK IF THIS HITS


config = GPT2Config(
    vocab_size = tokenizer.get_vocab_size(),
    bos_token_id=0,
    eos_token_id = 0,
    n_layer=12,
    n_head=12,
)

model = GPT2LMHeadModel(config).to(device("cuda:0"))
#check out cache_dir
dataset = load_dataset("text", data_files=dpath)
dataset = dataset["train"]
dataset = Dataset.from_list(dataset)
def encode(lines):
    a = tokenizer.encode(lines["text"][0], add_special_tokens=True)
    ans = {}
    ans["input_ids"] = a.ids
    ans["attention_mask"] = a.attention_mask

    return ans
dataset.set_transform(encode)
'''ndata = []
for i in dataset:
    ndata.append(encode(i))'''

#data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
data_collator = DefaultDataCollator()
training_args = TrainingArguments(
    output_dir="smallModelV2",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=96, #64
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
trainer.save_model("smallModelV2")