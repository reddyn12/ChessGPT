from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset
from torch import device
import sys

tokenizer = GPT2Tokenizer.from_pretrained("tokeniLabV3",unk_token="<unk>", eos_token="</N>", bos_token="<N>", pad_token="<pad>")
# print(tokenizer("1. d4"))
# sys.exit()
dpath = "dataPre/KingBase2019/kingCleanV2.pgn"


config = GPT2Config(
    vocab_size = tokenizer.vocab_size,
    bos_token = tokenizer.bos_token,
    eos_token = tokenizer.eos_token,
    pad_token = tokenizer.pad_token,
    bos_token_id = 0,
    eos_token_id=2,
    n_layer=12,
    n_head=12,
)

model = GPT2LMHeadModel(config).to("cuda")

#check out cache_dir
dataset = load_dataset("text", data_files=dpath)
dataset = dataset["train"]

def encode(lines):
    a = tokenizer(lines["text"], add_special_tokens=True, truncation=True, max_length=512)
    print(a)
    sys.exit()
    
    return a
dataset.set_transform(encode)


# print(len(dataset))
# sys.exit()

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False, pad_to_multiple_of=8)

training_args = TrainingArguments(
    output_dir="iLabV3",
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
trainer.save_model("iLabV3")