import sys
import torch
from datasets import load_dataset, Dataset
from transformers import GPT2Tokenizer

from tokenizers.implementations import ByteLevelBPETokenizer

t2 = ByteLevelBPETokenizer.from_file("tokenizerNewClean/vocab.json", "tokenizerNewClean/merges.txt")
t =t2.encode("Hello world")
t2.p
print(t.attention_mask)
sys.exit()
print(torch.cuda.is_available())


'''dpath = "dataPre/KingBase2019/kingCleanV3.pgn"


dataset = load_dataset("text", data_files=dpath)
d = Dataset.from_file(dpath)
print(d[:2])
s = dataset["train"]["text"]
#print(s[:2])
'''
