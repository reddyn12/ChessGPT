from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.implementations import ByteLevelBPETokenizer

dataPath = ["dataPre/KingBase2019/kingCleanV2.pgn"]


tokenizer = Tokenizer(BPE(unk_token="[UNK]", cache_capacity=5000))
trainer = BpeTrainer(vocab_size=5000, min_frequency=2,special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]",
'''
'''],
)
tokenizer.pre_tokenizer = Whitespace()
tokenizer.train(files=dataPath, trainer=trainer)

#tokenizer.save("tokenizerNew/tokenizer-king.json")
tokenizer.save("tokenizerNewClean")
'''
tokenizer = Tokenizer(BPE(unk_token="<UNK>"))
trainer = BpeTrainer(special_tokens=["<UNK>", "<S>", "<N>", "<PAD>", "<MASK>"])

tokenizer.pre_tokenizer = Whitespace()



tokenizer.train(files=dataPath, trainer=trainer)

'''