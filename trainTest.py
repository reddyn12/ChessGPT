from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset
from torch import device
import sys
dpath = "dataPre/KingBase2019/kingCleanPre.pgn"

tokenizer = GPT2Tokenizer.from_pretrained("tokenizer")

#CHECK IF THIS HITS
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

config = GPT2Config(
    vocab_size = tokenizer.vocab_size,
    bos_token = tokenizer.bos_token_id,
    eos_token = tokenizer.eos_token_id,
    n_layer=8,
    n_head=8,
)

model = GPT2LMHeadModel(config).to(device("cuda:0"))
#check out cache_dir
dataset = load_dataset("text", data_files=dpath)

def encode(lines):
    return tokenizer(lines["text"], add_special_tokens=True, truncation=True, max_length=512*2)
dataset.set_transform(encode)

dataset = dataset["train"]
# print(len(dataset))
# sys.exit()

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

training_args = TrainingArguments(
    output_dir="smallModel",
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
trainer.save_model("smallModel")