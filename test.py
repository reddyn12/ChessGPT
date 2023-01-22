import sys
import torch
from datasets import load_dataset, Dataset
from transformers import GPT2Tokenizer

from tokenizers.implementations import ByteLevelBPETokenizer

# t2 = ByteLevelBPETokenizer.from_file("tokenizerNewClean/vocab.json", "tokenizerNewClean/merges.txt")
# t =t2.encode("Hello world")
# t2.p
# print(t.attention_mask)


# print(torch.cuda.is_available())
# dpath = "dataPre/KingBase2019/kingCleanV2.pgn"

# data = load_dataset("text", data_files=dpath)
# print(data["train"]["text"][0][-1])


# t = {1:"hi", 2:"bye"}

# print(t[3])


s = "1234"
s = s[1:]
print(s)


t = [1,2,3,4]
t = t + []
print(t)
'''dpath = "dataPre/KingBase2019/kingCleanV3.pgn"


dataset = load_dataset("text", data_files=dpath)
d = Dataset.from_file(dpath)
print(d[:2])
s = dataset["train"]["text"]
#print(s[:2])
'''
