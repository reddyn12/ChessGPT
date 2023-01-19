# import sys

# sys.path.insert(0, "D:/Code/ChessGPT/custom")
#CHECK ORIGINAL Tokenizer wit new tokes, maybe faster times

from customTokenImp import CustByteLevelBPETokenizer

path = "dataPre/KingBase2019/kingCleanV3.pgn"

tokenizer = CustByteLevelBPETokenizer()

tokenizer.train(files=path, vocab_size=5000, min_frequency=2, special_tokens=[
    "<N",
    "\nN>",
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>"
])

tokenizer.save_model("tokenizerV2")


