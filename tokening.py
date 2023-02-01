
from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.pre_tokenizers import ByteLevel
import os
import sys
# from tqdm import tqdm
# Maybe charecter tokenize?
#
#753

path = os.listdir("data/KingBase/games")
npath =[]
for i in (path):
    npath.append("data/KingBase/games/"+i)
path = npath
print(len(path))
# path = "dataPre/KingBase2019/kingCleanV3.pgn"
tokenizer = ByteLevelBPETokenizer()
# print(tokenizer.pre_tokenizer)
# tokenizer.pre_tokenizer = ByteLevel()
#                           2202209
tokenizer.train(files=path, vocab_size=5000, min_frequency=1, show_progress=True ,special_tokens=[
    "<N>",
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>"
])

tokenizer.save_model("testToken")


