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


1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.Qe2 Qe7 6.d3 Nf6 7.Bg5 Nbd7 8.Nc3
Qxe2+ 9.Bxe2 h6 10.Bd2 Nb6 11.a4 a5 12.Nb5 Kd8 13.c4 Nbd7 14.d4 Ne4 15.Be3
c6 16.Nc3 Nxc3 17.bxc3 Be7 18.Bd3 Kc7 19.Kd2 b6 20.Rab1 Ba6 21.h4 Nf6 22.
Bf4 c5 23.Rb2 Rhe8 24.Rhb1 Rab8 25.Ne5 Nh5 26.Bh2 cxd4 27.cxd4 Bxh4 1-0


1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 g6 5.Nf3 Bg7 6.Na3 cxd4 7.Bc4 Qe4+ 8.Be3 
Nh6 9.Bd3 Qd5 10.Bc4 Qe4 11.Bd3 Qd5 12.Bc4 Qa5 13.Bb5+ Nc6 14.Nxd4 O-O 15.
Nxc6 bxc6 16.Be2 Nf5 17.Nc4 Qd5 18.O-O Ba6 19.Nd2 Nxe3 20.fxe3 Bd3 21.Nf3 
Bf5 22.Nd4 Be4 23.Bf3 Rab8 24.Qe2 a5 25.Bxe4 Qxe4 26.Nb3 Qe5 27.Rad1 a4 
28.Nd4 Rb6 29.Rf3 Qc5 30.Qc2 e5 31.Ne2 Rfb8 32.Rb1 Qc4 33.a3 Bf8 34.Rff1 
Bc5 35.Kf2 Qh4+ 36.Ng3 f5 37.Kg1 Bxe3+ 38.Kh1 Bf4 0-1


1.c4 c5 2.Nf3 g6 3.d4 Bg7 4.e4 d6 5.d5 e6 6.Nc3 Ne7 7.Be2 h6 8.dxe6 Bxe6 
9.Nb5 Nc8 10.Bf4 O-O 11.O-O Bxb2 12.Bxh6 a6 13.Bxf8 Bxa1 14.Qxa1 Kxf8 15.
Nc3 Nd7 16.Nd5 Kg8 17.Qc1 Bxd5 18.cxd5 Nf6 19.Ng5 Qe7 20.Bd3 b5 21.f4 Nb6 
22.Rf3 Re8 23.Qf1 Nh5 24.h4 Nd7 25.e5 dxe5 26.f5 Nf4 27.fxg6 fxg6 28.Be4 
Qd6 29.g3 Nh5 30.Nf7 Qb6 31.d6 c4+ 32.Kh2 Kg7 33.Qc1 Nf4 34.Ng5 Qxd6 35.
gxf4 exf4 36.Qxf4 Ne5 37.Kg2 b4 38.Nf7 Qc7 39.Qh6+ 1-0


1.d4 Nf6 2.Nf3 g6 3.c4 Bg7 4.Nc3 O-O 5.e4 d6 6.h3 e5 7.d5 a5 8.Be2 Na6 9.
Bg5 Qe8 10.Nd2 Nd7 11.g4 Ndc5 12.a3 Bd7 13.Qc2 f5 14.Be3 Qe7 15.O-O-O f4 
16.Bxc5 Nxc5 17.Rdg1 a4 18.g5 f3 19.Bf1 Rf4 20.Nd1 Ra6 21.Ne3 Rb6 22.h4 
Rb3 23.h5 c6 24.hxg6 hxg6 25.Nxb3 axb3 26.Qb1 Nxe4 27.Rh2 Qd8 28.Bd3 Nc5 
29.Bxg6 e4 30.Bxe4 Rxe4 31.g6 Qe7 32.Rh5 Rxe3 0-1


1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 c5 5.cxd5 Nxd5 6.e4 Nxc3 7.bxc3 cxd4 8.
cxd4 Bb4+ 9.Bd2 Bxd2+ 10.Qxd2 O-O 11.Rc1 b6 12.Bd3 Ba6 13.O-O Qd7 14.Rfd1 
Bxd3 15.Qxd3 Qb7 16.d5 exd5 17.exd5 Nd7 18.Ng5 Nf6 19.Rc6 h6 20.Rxf6 hxg5 
21.Rf5 f6 22.d6 Qd7 23.h4 gxh4 24.Rh5 Qe6 25.Rxh4 f5 26.Qh3 Rad8 27.Rd3 
Qe1+ 28.Kh2 Qe5+ 29.f4 Qf6 30.Re3 g6 31.Re7 Rf7 32.Re6 Qg7 33.Rxg6 Qxg6 
34.Rh8+ Kg7 35.Rxd8 Qh7 36.Qxh7+ Kxh7 37.d7 1-0


1.d4 Nf6 2.Nf3 e6 3.g3 b6 4.Bg2 Bb7 5.O-O d5 6.c4 Be7 7.cxd5 exd5 8.Nc3 
O-O 9.Ne5 c6 10.f4 c5 11.e3 Re8 12.Qb3 Na6 13.Bd2 Nc7 14.Rad1 c4 15.Qc2 b5
16.g4 Nd7 17.g5 f6 18.gxf6 Nxf6 19.Kh1 Rf8 20.Bf3 Nfe8 21.Rg1 Qd6 22.Be1 
Rd8 23.Qg2 Bc8 24.a4 a6 25.Na2 Qh6 26.axb5 axb5 27.Nb4 Bh3 28.Qg3 Bxb4 29.
Bxb4 Nd6 30.Ba5 Nde8 31.Ra1 Ra8 32.Bb4 Rxa1 33.Rxa1 Rf6 34.Be7 Rb6 35.Bc5 
Rb7 36.e4 Be6 37.f5 dxe4 38.fxe6 exf3 39.Qxf3 Nxe6 40.Qxb7 1-0



'''

t = tokenizer.encode(s)
print(t.ids) 
print(t.tokens)
# %%
