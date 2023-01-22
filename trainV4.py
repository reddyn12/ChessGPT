from lib2to3.pgen2 import token
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset
from torch import device
import sys
from customTokenImp import CustByteLevelBPETokenizer
import os
from transformers import DataCollatorWithPadding

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2,3"

dpath = "dataPre/KingBase2019/kingCleanV3.pgn"

# tokenizer = GPT2Tokenizer.from_pretrained("tokenizerV2")
tokenizer = CustByteLevelBPETokenizer.from_file("tokenizerV2/vocab.json", "tokenizerV2/merges.txt")


#CHECK IF THIS HITS
# tokenizer.add_special_tokens({
#     "eos_token": "<N",
#     "bos_token": "\nN>",
#     "unk_token": "<unk>",
#     "pad_token": "<pad>",
#     "mask_token": "<mask>"
# })

#fix eos and os ids
config = GPT2Config(
    vocab_size = tokenizer.get_vocab_size(),
    bos_token = "\nN>",
    eos_token = "<N",
    n_layer=12,
    n_head=12,
)

model = GPT2LMHeadModel(config).to(device("cuda:0"))
# model.from_pretrained("smallModelV3/checkpoint-10000")
# model.train()
#check out cache_dir
dataset = load_dataset("text", data_files=dpath)
#tokenizer.encode()

tokenizer.enable_padding(pad_id=3, pad_token="<pad>")


def encode(lines):
    #a1 = tokenizer.encode_plus()
    # print()
    # print(len(lines["text"]))
    # sys.exit()
    
    a = tokenizer.encode(lines["text"][0])
    
    #a.special_tokens_mask
    ans = {}
    ans["ids"] = a.ids
    ans["attention_mask"] = a.attention_mask
    ans["type_ids"] = a.type_ids
    ans["tokens"] = a.tokens
    ans["offsets"] = a.offsets
    # ans["overflowing"] = a.overflowing
    ans["special_tokens_mask"] = a.special_tokens_mask

    return ans
dataset.set_transform(encode)

dataset = dataset["train"]
# print(len(dataset))
# sys.exit()

#data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

training_args = TrainingArguments(
    output_dir="smallModelV4",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=15, #64
    save_steps=10000,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns=False,
    do_train= True,
    
    
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
    

)


trainer.train()
trainer.save_model("smallModelV4")