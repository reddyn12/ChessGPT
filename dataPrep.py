#%%

import os

from tqdm import tqdm
#%%
testParent = "dataPre/KingBase2019/KingBase2019-pgn"
testPaths = os.listdir(testParent)

print(testPaths)
#%%
for testPath in testPaths:
    file = open(testParent+"/"+testPath, "r")
    contents = file.readlines()
    print(len(contents), "len of contents")
    cnt = 0
    fin = ""
    for i in tqdm(contents):
        if i.startswith("["):
            cnt+=1
            
        else:
            fin = fin + i

    print(cnt)
    #print(fin)
    file1 = open("dataPre/KingBase2019/kingCleanPre.pgn", "a")
    file1.write(fin+"\n")
    file.close()
    file1.close()

#%%

def parseGame(s:str):
    temp = s.split("\n\n")
    print(temp)

#%%
s = '''
1.d4 d5 2.Nf3 Nf6 3.e3 c5 4.dxc5 Qa5+ 5.Nbd2 Qxc5 6.a3 a5 7.c4 dxc4 8.Nxc4
Nc6 9.e4 Ng4 10.Ne3 a4 11.Qd5 Qb6 12.Qb5 Qxb5 13.Bxb5 Nxe3 14.Bxe3 Bd7 15.
Rc1 g6 16.Bd2 Bg7 17.Bc3 O-O 18.O-O Bxc3 19.Rxc3 Ra5 20.Bc4 Bg4 21.Ne1 Ne5
22.f3 Bd7 23.Be2 Rd8 24.Nc2 Raa8 25.Rc1 Rac8 26.Nb4 Rxc3 27.Rxc3 Be6 28.
Nd3 Bc4 29.Nxe5 Bxe2 30.Rc7 Ba6 31.Rxe7 Rd1+ 32.Kf2 Rd2+ 33.Kg3 Rxb2 34.
Nxf7 Rb3 35.e5 Rxa3 36.Nd6 Rd3 37.Kf4 a3 38.Kg5 a2 39.Re8+ Kg7 40.Re7+ Kg8
41.Re8+ 1/2-1/2


1.d4 Nf6 2.Nf3 e6 3.c4 c5 4.e3 d5 5.Nc3 cxd4 6.exd4 Bb4 7.cxd5 Nxd5 8.Bd2 
O-O 9.Bd3 Nc6 10.O-O Be7 11.Qe2 Nf6 12.Rfd1 Nb4 13.Bb1 b6 14.Ne4 Nbd5 15.
Ne5 Nxe4 16.Qxe4 f5 17.Qe2 Bb7 18.Nf3 Rf6 19.Bd3 h6 20.a3 Bd6 21.Ba6 Bxa6 
22.Qxa6 Qd7 23.Rac1 Rff8 24.Rc2 Rac8 25.Rdc1 Rxc2 26.Rxc2 Rb8 27.h3 Kf7 
28.Bb4 Nxb4 29.axb4 Rb7 30.d5 Rc7 31.dxe6+ Kxe6 32.Rxc7 Qxc7 33.Qe2+ Kf6 
34.Qd2 Bf4 35.Qd4+ Kg6 36.g4 fxg4 37.Qe4+ Kf6 38.hxg4 Qd6 39.Kg2 g6 40.Nh4
Kg5 41.Kh3 h5 42.Nf3+ Kh6 43.b5 Qf6 44.gxh5 Kxh5 45.Qd5+ Kh6 46.b3 Bd6 47.
Qe4 Kg7 48.Kg4 Be7 49.Qd4 Bc5 50.Qd7+ Kh6 51.Qd2+ Kg7 52.Qd7+ Kh6 53.Qd2+ 
Kg7 54.Qd7+ Kh6 55.Qd2+ Kg7 56.Qd7+ Kh6 57.Qd2+ Kg7 58.Kg3 Qf5 59.Qd8 Qf7 
60.Qd3 Qf6 61.Qd7+ Kh6 62.Qh3+ Kg7 63.Qd7+ Kh6 64.Qh3+ Kg7 65.Qd7+ Kh6 66.
Kg2 Qf4 67.Qh3+ Kg7 68.Qd7+ Kh6 69.Qc8 Kg7 70.Qe6 Kh6 71.Qd7 Qf6 72.Qd2+ 
Kg7 73.Qd5 Qf4 74.Qe5+ Qf6 75.Qc7+ Kh6 76.Qh2+ Kg7 77.Qc7+ Kh6 78.Qh2+ Kg7
79.Qe5 Bd6 80.Qd4 Bc5 81.Qe4 Kh6 82.Qg4 Kg7 83.Qe4 Kh6 84.Kg3 Bd6+ 85.Kh3 
Bc5 86.Kg2 Kg7 87.Qb7+ Kh6 88.Qe4 Kg7 89.Qg4 Kh6 90.Qh3+ Kg7 91.Qd7+ Kh6 
92.Qg4 Kg7 1/2-1/2


1.e4 c5 2.Nf3 g6 3.d4 cxd4 4.Nxd4 Nc6 5.c4 Nf6 6.Nc3 Nxd4 7.Qxd4 d6 8.f3 
Bg7 9.Be3 O-O 10.Qd2 a5 11.Na4 Nd7 12.O-O-O Qc7 13.Kb1 b6 14.h4 Nc5 15.Nc3
f5 16.Bh6 fxe4 17.Bxg7 Kxg7 18.fxe4 Qb7 19.Qd4+ Kg8 20.h5 Ne6 21.Qe3 g5 
22.h6 Qc6 23.Nd5 Rf7 24.Be2 Qc5 25.Qc3 Nf4 26.Bh5 Nxh5 27.Rxh5 e5 28.Rxg5+
Kh8 29.Rxe5 dxe5 30.Qxe5+ Kg8 31.Nf6+ Kh8 32.Rd8+ Qf8 33.Nd5+ 1-0


1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Ndb5 h6 7.Nd6+ Bxd6 8.
Qxd6 Qe7 9.Qxe7+ Kxe7 10.Be3 d6 11.O-O-O Be6 12.f3 a6 13.Be2 Rhc8 14.Kb1 
b5 15.Rd2 Na5 16.Rhd1 Rc6 17.g4 Nc4 18.Bxc4 Bxc4 19.Re1 b4 20.Nd1 h5 21.
Bg5 hxg4 22.fxg4 Ke6 23.b3 Bb5 24.Bxf6 Kxf6 25.a4 bxa3 26.c4 Bxc4 27.bxc4 
Rxc4 28.Ne3 Rb4+ 29.Ka1 Kg5 30.Rf2 Rxe4 31.h4+ Kg6 32.h5+ Kh7 33.Rxf7 d5 
34.g5 Rc8 35.Ka2 Rc3 36.Nxd5 Rc2+ 37.Kxa3 1-0


'''
parseGame(s)
# %%
print(s)
# %%
t = s.replace("\n", " <N> ")
print(t)
# %%
df = open("dataPre/KingBase2019/kingCleanPre.pgn", "r")
d = df.read()
print("changing new line")
newd = d.replace("\n", " <N> ")
print("changing period")
newd = newd.replace(".", ". ")
print("upload newdd")
file = open("dataPre/KingBase2019/kingClean.pgn", "w")
file.write(newd)
df.close()
file.close()


# %%
