#%%
from tokenizers import ByteLevelBPETokenizer


#%%

path = "dataPre/KingBase2019/kingCleanPre.pgn"

#%%

tokenizer = ByteLevelBPETokenizer()
tokenizer.train(files=path, vocab_size=2000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>"
])

tokenizer.save_model("tokenizer")


# %%

s='''

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nf6 5.Nxf6+ gxf6 6.Nf3 Bg4 7.c3 e6 8.Bf4
Bd6 9.Bxd6 Qxd6 10.Qb3 Nd7 11.Be2 O-O-O 12.O-O-O Rhg8 13.g3 h5 14.Rhe1 
Bxf3 15.Bxf3 h4 16.Kb1 f5 17.c4 Kb8 18.a4 Rh8 19.a5 a6 20.d5 cxd5 21.cxd5 
e5 22.Rc1 Nc5 23.Qc3 Ne4 24.Bxe4 fxe4 25.Rxe4 hxg3 26.hxg3 f6 27.Rd1 Rc8 
28.Qb3 Rc5 29.Rb4 Qd7 30.Ra4 Rb5 31.Qc4 Rc8 32.Qe4 Qd6 33.f4 Rcc5 34.fxe5 
fxe5 35.Rc4 Rxd5 36.Rxd5 Rxd5 37.Rb4 Qc5 38.Ra4 Qb5 39.Ka2 Rd3 40.Qb4 Qxb4
41.Rxb4 Rxg3 42.Rc4 Rg7 43.Kb3 Rc7 44.Kc3 Kc8 45.Kd3 Rxc4 46.Kxc4 Kc7 47.
Kd5 e4 48.Kxe4 Kc6 49.Kd4 Kb5 50.Kd3 Kxa5 51.Kc3 Ka4 52.Kc4 b5+ 53.Kc3 a5 
54.Kc2 b4 55.Kc1 Kb3 56.Kb1 a4 57.Ka1 Kc2 58.Ka2 a3 0-1
'''

t = tokenizer.encode(s)
print(t.ids)
print(t.tokens)
# %%
