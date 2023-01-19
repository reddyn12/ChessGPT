from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import GPT2Tokenizer

tokenizer = ByteLevelBPETokenizer.from_file("tokenizerNew/vocab.json", "tokenizerNew/merges.txt")
t1 = GPT2Tokenizer.from_pretrained("tokenizer")
t1.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})
t2 = ByteLevelBPETokenizer.from_file("tokenizerNewClean/vocab.json", "tokenizerNewClean/merges.txt")

s = '''1 . c4 e5 2 . g3 Nf6 3 . Bg2 d5 4 . cxd5 Nxd5 5 . Nf3 Nc6 6 . O-O Be7 7 . d4 exd4 8 . Nxd4 Nxd4 9 . Qxd4 Nf6 10 . Qxd8 + Bxd8 11 . Nc3 c6 12 . b4 a6 13 . a4 O-O 14 . Be3 Be7 15 .  b5 axb5 16 . axb5 Bd7 17 . bxc6 Bxc6 18 . Rxa8 Rxa8 19 . Rb1 Rc8 20 . Bh3 Rd8 21 . Bg2 h6 22 . h3 Kf8 23 . Bxc6 bxc6 24 . Rb7 Rc8 25 . Na4 Nd5 26 . Bc5 Bxc5 27 . Nxc5 Rc7  28 . Rb2 Ke7 29 . e4 Nf6 30 . f4 Nd7 31 . Nxd7 Rxd7 32 . Kf2 Rd3 33 . Rb7 + Ke6 34 . Rc7  Rc3 35 . f5 + Kf6 36 . e5 + Kxf5 37 . Rxf7 + Kxe5 38 . Rxg7 Kf6 39 . Rh7 Kg6 40 . Rh8 c5  41 . Rc8 h5 42 . Rg8 + Kf5 43 . Rh8 Kg6 1/2-1/2
1 . Nf3 d5 2 . '''

s = ''' +1/2-1/2
1'''

s = '''1 . d4 d5 2 . Nf3 Nf6 3 . e3 c5 4 . dxc5 Qa5 + 5 . Nbd2 Qxc5 6 . a3 a5 7 . c4 dxc4 8 . Nxc4 Nc6 9 . e4 Ng410 . Ne3 a411 . Qd5 Qb612 . Qb5 Qxb513 . Bxb5 Nxe314 . Bxe3 Bd715 .  Rc1 g616 . Bd2 Bg717 . Bc3 O-O18 . O-O Bxc319 . Rxc3 Ra5 20 . Bc4 Bg4 21 . Ne1 Ne5 22 . f3 Bd7 23 . Be2 Rd8 24 . Nc2 Raa8 25 . Rc1 Rac8 26 . Nb4 Rxc3 27 . Rxc3 Be6 28 .  Nd3 Bc4 29 . Nxe5 Bxe2 30 . Rc7 Ba6 31 . Rxe7 Rd1 + 32 . Kf2 Rd2 + 33 . Kg3 Rxb2 34 .  Nxf7 Rb3 35 . e5 Rxa3 36 . Nd6 Rd3 37 . Kf4 a3 38 . Kg5 a2 39 . Re8 + Kg7 40 . Re7 + Kg8 41 . Re8 +1/2-1/2 <N
N> 1 . d4 '''
output = tokenizer.encode(s, is_pretokenized=False)
o1 = t1(s, add_special_tokens=True, truncation=True, max_length=512*2)
o2 = t2.encode(s, is_pretokenized=False, add_special_tokens=True)
print(output.tokens)
print(output.ids)
print(o1)
print(o2.tokens)
print(o2.ids)
'''print(o1["input_tokens"])
print(o1["input_ids"])'''

