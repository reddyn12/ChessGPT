#%%
import sys
import torch
from datasets import load_dataset, Dataset
from transformers import GPT2Tokenizer

from tokenizers.implementations import ByteLevelBPETokenizer
import customToken
import os


print(int(os.environ.get('RANK', -1)))

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


# s = "1234"
# s = s[1:]
# print(s)


# t = [1,2,3,4]
# t = t + []
# print(t)

# test = "1 . d4 Nf6 2 . c4 e6 3 . Nc3 Bb4 4 . Qc2 O-O 5 . e4 d5 6 . e5 Nfd7 7 . a3 Be7 8 . cxd5  exd5 9 . Nxd5 c5 10 . Bd3 Kh8 11 . Bxh7 Nc6 12 . Be4 cxd4 13 . Qe2 g6 14 . h4 Ndxe5  15 . Bg5 Bxg5 16 . hxg5 + Kg7 17 . Nf6 Rh8 18 . Rxh8 Qxh8 19 . f4 Qh2 20 . Qf2 Ng4 21 .  Nxg4 Bxg4 22 . Bxc6 bxc6 23 . Qxd4 + Kg8 24 . Kf1 Re8 25 . Re1 Rxe1 + 26 . Kxe1 Qxg2  27 . Qxa7 Qe4 + 28 . Kd2 Qg2 + 29 . Ke1 Qxb2 30 . Qe3 Qg2 31 . a4 Qd5 32 . Kf2 Qa2 + 33 .  Kg3 Be6 34 . Nf3 Qxa4 35 . Ne5 Qc2 36 . Qd3 Qc1 37 . Qf3 Bd5 38 . Qf2 Qc3 + 39 . Kh2  Be6 40 . Qf3 Qd2 + 41 . Kg3 c5 42 . Qa8 + Kg7 43 . Qa1 Qe3 + 44 . Nf3 + Kh7 45 . Qe5 Qa3  46 . Qd6 Qc1 47 . Qd2 Qf1 48 . Qd6 Qh3 + 49 . Kf2 Bg4 50 . Ng1 Qh2 + 51 . Kf1 Qc2 52 . Ke1 c4 53 . Qf6 Qd1 + 54 . Kf2 Kg8 55 . Qe5 Qb3 56 . Qe8 + Kg7 57 . Qe5 + Kh7 58 . Qd5 Qb2 +  59 . Kg3 Be6 60 . Qf3 Qd2 61 . Ne2 Bd5 62 . Qf2 Qd3 + 63 . Kh2 c3 64 . f5 gxf5 65 . Nxc3  Bc4 66 . Qh4 + Kg8 67 . Qg3 Qd2 + 68 . Kg1 Qd4 + 69 . Kh2 Kg7 70 . Qf3 Kg6 71 . Qc6 + Kxg5 72 . Qg2 + Kf6 73 . Qc6 + Be6 74 . Qf3 Qe5 + 75 . Kg1 f4 76 . Ne4 + Kg6 77 . Qg2 + Kf5 78 .  Nd2 Bd5 79 . Qf2 Qh8 80 . Qc5 Qh1 + 81 . Kf2 Kg4 82 . Qc8 + f5 83 . Qd7 Qg2 + 84 . Ke1  Qg3 + 85 . Kd1 Qg1 + 86 . Kc2 Qc5 + 87 . Kd1 Kg3 88 . Qg7 + Kf2 89 . Qb2 Bf3 + 90 . Nxf3 +  Kxf3 91 . Qc3 + Qe3 92 . Qc6 + Qe4 93 . Qc3 + Kg2 94 . Qb2 + Kg3 95 . Qg7 + Kf2 96 . Qb2 +  Ke3 97 . Qd2 + Kf3 98 . Qc3 + Qe3 99 . Qc6 + Kg3 100 . Qg6 + Kf2 101 . Qxf5 f3 102 . Qh7  Qe2 + 103 . Kc1 Kg1 104 . Qg7 + Qg2 105 . Qd4 + Kf1 106 . Qd1 + Kf2 107 . Qd4 + Kg3 108 .  Qe5 + Kh4 109 . Qh8 + Kg4 110 . Qg7 + Kh3 111 . Qh8 + Kg3 112 . Qe5 + Kg4 113 . Qg7 + Kf5  114 . Qf7 + Ke4 115 . Qe6 + Kd3 116 . Qd5 + Ke3 117 . Qe5 + Kf2 1/2-1/2"

# print(len(customToken.tokenize(test)))

'''dpath = "dataPre/KingBase2019/kingCleanV3.pgn"


dataset = load_dataset("text", data_files=dpath)
d = Dataset.from_file(dpath)
print(d[:2])
s = dataset["train"]["text"]
#print(s[:2])
'''

# %%
