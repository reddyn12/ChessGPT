from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("tokeniLabV3",unk_token="<unk>", eos_token="</N>", bos_token="<N>", pad_token="<pad>")


s = "1 . d4 </N> "
s = "1 . d4 Nf6 2 . c4 e6 3 . Nc3 Bb4 4 . Qc2 O-O 5 . e4 d5 6 . e5 Nfd7 7 . a3 Be7 8 . cxd5  exd5 9 . Nxd5 c5 10 . Bd3 Kh8 11 . Bxh7 Nc6 12 . Be4 cxd4 13 . Qe2 g6 14 . h4 Ndxe5  15 . Bg5 Bxg5 16 . hxg5 + Kg7 17 . Nf6 Rh8 18 . Rxh8 Qxh8 19 . f4 Qh2 20 . Qf2 Ng4 21 .  Nxg4 Bxg4 22 . Bxc6 bxc6 23 . Qxd4 + Kg8 24 . Kf1 Re8 25 . Re1 Rxe1 + 26 . Kxe1 Qxg2  27 . Qxa7 Qe4 + 28 . Kd2 Qg2 + 29 . Ke1 Qxb2 30 . Qe3 Qg2 31 . a4 Qd5 32 . Kf2 Qa2 + 33 .  Kg3 Be6 34 . Nf3 Qxa4 35 . Ne5 Qc2 36 . Qd3 Qc1 37 . Qf3 Bd5 38 . Qf2 Qc3 + 39 . Kh2  Be6 40 . Qf3 Qd2 + 41 . Kg3 c5 42 . Qa8 + Kg7 43 . Qa1 Qe3 + 44 . Nf3 + Kh7 45 . Qe5 Qa3  46 . Qd6 Qc1 47 . Qd2 Qf1 48 . Qd6 Qh3 + 49 . Kf2 Bg4 50 . Ng1 Qh2 + 51 . Kf1 Qc2 52 . Ke1 c4 53 . Qf6 Qd1 + 54 . Kf2 Kg8 55 . Qe5 Qb3 56 . Qe8 + Kg7 57 . Qe5 + Kh7 58 . Qd5 Qb2 +  59 . Kg3 Be6 60 . Qf3 Qd2 61 . Ne2 Bd5 62 . Qf2 Qd3 + 63 . Kh2 c3 64 . f5 gxf5 65 . Nxc3  Bc4 66 . Qh4 + Kg8 67 . Qg3 Qd2 + 68 . Kg1 Qd4 + 69 . Kh2 Kg7 70 . Qf3 Kg6 71 . Qc6 + Kxg5 72 . Qg2 + Kf6 73 . Qc6 + Be6 74 . Qf3 Qe5 + 75 . Kg1 f4 76 . Ne4 + Kg6 77 . Qg2 + Kf5 78 .  Nd2 Bd5 79 . Qf2 Qh8 80 . Qc5 Qh1 + 81 . Kf2 Kg4 82 . Qc8 + f5 83 . Qd7 Qg2 + 84 . Ke1  Qg3 + 85 . Kd1 Qg1 + 86 . Kc2 Qc5 + 87 . Kd1 Kg3 88 . Qg7 + Kf2 89 . Qb2 Bf3 + 90 . Nxf3 +  Kxf3 91 . Qc3 + Qe3 92 . Qc6 + Qe4 93 . Qc3 + Kg2 94 . Qb2 + Kg3 95 . Qg7 + Kf2 96 . Qb2 +  Ke3 97 . Qd2 + Kf3 98 . Qc3 + Qe3 99 . Qc6 + Kg3 100 . Qg6 + Kf2 101 . Qxf5 f3 102 . Qh7  Qe2 + 103 . Kc1 Kg1 104 . Qg7 + Qg2 105 . Qd4 + Kf1 106 . Qd1 + Kf2 107 . Qd4 + Kg3 108 .  Qe5 + Kh4 109 . Qh8 + Kg4 110 . Qg7 + Kh3 111 . Qh8 + Kg3 112 . Qe5 + Kg4 113 . Qg7 + Kf5  114 . Qf7 + Ke4 115 . Qe6 + Kd3 116 . Qd5 + Ke3 117 . Qe5 + Kf2 1/2-1/2"
out = tokenizer.encode(s)
print(len(out))
# print(out.ids)
# print(out.tokens)

# tokenizer = ByteLevelBPETokenizer.from_file("tokenizerNew/vocab.json", "tokenizerNew/merges.txt")
# t1 = GPT2Tokenizer.from_pretrained("tokenizer")
# t1.add_special_tokens({
#     "eos_token": "</s>",
#     "bos_token": "<s>",
#     "unk_token": "<unk>",
#     "pad_token": "<pad>",
#     "mask_token": "<mask>"
# })
# t2 = ByteLevelBPETokenizer.from_file("tokenizerNewClean/vocab.json", "tokenizerNewClean/merges.txt")

# s = '''1 . c4 e5 2 . g3 Nf6 3 . Bg2 d5 4 . cxd5 Nxd5 5 . Nf3 Nc6 6 . O-O Be7 7 . d4 exd4 8 . Nxd4 Nxd4 9 . Qxd4 Nf6 10 . Qxd8 + Bxd8 11 . Nc3 c6 12 . b4 a6 13 . a4 O-O 14 . Be3 Be7 15 .  b5 axb5 16 . axb5 Bd7 17 . bxc6 Bxc6 18 . Rxa8 Rxa8 19 . Rb1 Rc8 20 . Bh3 Rd8 21 . Bg2 h6 22 . h3 Kf8 23 . Bxc6 bxc6 24 . Rb7 Rc8 25 . Na4 Nd5 26 . Bc5 Bxc5 27 . Nxc5 Rc7  28 . Rb2 Ke7 29 . e4 Nf6 30 . f4 Nd7 31 . Nxd7 Rxd7 32 . Kf2 Rd3 33 . Rb7 + Ke6 34 . Rc7  Rc3 35 . f5 + Kf6 36 . e5 + Kxf5 37 . Rxf7 + Kxe5 38 . Rxg7 Kf6 39 . Rh7 Kg6 40 . Rh8 c5  41 . Rc8 h5 42 . Rg8 + Kf5 43 . Rh8 Kg6 1/2-1/2
# 1 . Nf3 d5 2 . '''

# s = ''' +1/2-1/2
# 1'''

# s = '''1 . d4 d5 2 . Nf3 Nf6 3 . e3 c5 4 . dxc5 Qa5 + 5 . Nbd2 Qxc5 6 . a3 a5 7 . c4 dxc4 8 . Nxc4 Nc6 9 . e4 Ng410 . Ne3 a411 . Qd5 Qb612 . Qb5 Qxb513 . Bxb5 Nxe314 . Bxe3 Bd715 .  Rc1 g616 . Bd2 Bg717 . Bc3 O-O18 . O-O Bxc319 . Rxc3 Ra5 20 . Bc4 Bg4 21 . Ne1 Ne5 22 . f3 Bd7 23 . Be2 Rd8 24 . Nc2 Raa8 25 . Rc1 Rac8 26 . Nb4 Rxc3 27 . Rxc3 Be6 28 .  Nd3 Bc4 29 . Nxe5 Bxe2 30 . Rc7 Ba6 31 . Rxe7 Rd1 + 32 . Kf2 Rd2 + 33 . Kg3 Rxb2 34 .  Nxf7 Rb3 35 . e5 Rxa3 36 . Nd6 Rd3 37 . Kf4 a3 38 . Kg5 a2 39 . Re8 + Kg7 40 . Re7 + Kg8 41 . Re8 +1/2-1/2 <N
# N> 1 . d4 '''
# output = tokenizer.encode(s, is_pretokenized=False)
# o1 = t1(s, add_special_tokens=True, truncation=True, max_length=512*2)
# o2 = t2.encode(s, is_pretokenized=False, add_special_tokens=True)
# print(output.tokens)
# print(output.ids)
# print(o1)
# print(o2.tokens)
# print(o2.ids)
# '''print(o1["input_tokens"])
# print(o1["input_ids"])'''

