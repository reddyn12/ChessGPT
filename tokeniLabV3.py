from tokenizers.implementations import ByteLevelBPETokenizer



dpath = "dataPre/KingBase2019/kingCleanV2.pgn"

tokenizer = ByteLevelBPETokenizer()

tokenizer.train(files=dpath, vocab_size=5000, min_frequency=2, special_tokens=[
    "<N>",
    "<pad>",
    "</N>",
    "<unk>",
    "<mask>",
])

tokenizer.save_model("tokeniLabV3")