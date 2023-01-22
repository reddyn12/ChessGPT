


tokens =["K", "Q", "N", "B", "R", "x", ".", " ", "O-O", "O-O-O", "+", "1-0", "0-1", "1/2-1/2"]

for i in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    for j in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        tokens.append(i+j)


tokens = tokens + ["a", "b", "c", "d", "e", "f", "g", "h"]

#may need to go to 250
for i in range(100):
    tokens.append(str(i))




# t = [1,2,3]
# t= t+ [1,2,5,7]
# print(t)

#print(len(tokens), "token Length")

dictToken = {}

for i,j in enumerate(tokens):
    dictToken[j] = i

print(tokens[40], "id to token")

test ="1 . d4 Nf6 2 . Nf3 e6 3 . c4 c5 4 . e3 d5 5 . Nc3 cxd4 6 . exd4 Bb4 7 . cxd5 Nxd5 8 . Bd2  O-O 9 . Bd3 Nc6 10 . O-O Be7 11 . Qe2 Nf6 12 . Rfd1 Nb4 13 . Bb1 b6 14 . Ne4 Nbd5 15 .  Ne5 Nxe4 16 . Qxe4 f5 17 . Qe2 Bb7 18 . Nf3 Rf6 19 . Bd3 h6 20 . a3 Bd6 21 . Ba6 Bxa6  22 . Qxa6 Qd7 23 . Rac1 Rff8 24 . Rc2 Rac8 25 . Rdc1 Rxc2 26 . Rxc2 Rb8 27 . h3 Kf7  28 . Bb4 Nxb4 29 . axb4 Rb7 30 . d5 Rc7 31 . dxe6 + Kxe6 32 . Rxc7 Qxc7 33 . Qe2 + Kf6  34 . Qd2 Bf4 35 . Qd4 + Kg6 36 . g4 fxg4 37 . Qe4 + Kf6 38 . hxg4 Qd6 39 . Kg2 g6 40 . Nh4 Kg5 41 . Kh3 h5 42 . Nf3 + Kh6 43 . b5 Qf6 44 . gxh5 Kxh5 45 . Qd5 + Kh6 46 . b3 Bd6 47 .  Qe4 Kg7 48 . Kg4 Be7 49 . Qd4 Bc5 50 . Qd7 + Kh6 51 . Qd2 + Kg7 52 . Qd7 + Kh6 53 . Qd2 +  Kg7 54 . Qd7 + Kh6 55 . Qd2 + Kg7 56 . Qd7 + Kh6 57 . Qd2 + Kg7 58 . Kg3 Qf5 59 . Qd8 Qf7  60 . Qd3 Qf6 61 . Qd7 + Kh6 62 . Qh3 + Kg7 63 . Qd7 + Kh6 64 . Qh3 + Kg7 65 . Qd7 + Kh6 66 .  Kg2 Qf4 67 . Qh3 + Kg7 68 . Qd7 + Kh6 69 . Qc8 Kg7 70 . Qe6 Kh6 71 . Qd7 Qf6 72 . Qd2 +  Kg7 73 . Qd5 Qf4 74 . Qe5 + Qf6 75 . Qc7 + Kh6 76 . Qh2 + Kg7 77 . Qc7 + Kh6 78 . Qh2 + Kg7 79 . Qe5 Bd6 80 . Qd4 Bc5 81 . Qe4 Kh6 82 . Qg4 Kg7 83 . Qe4 Kh6 84 . Kg3 Bd6 + 85 . Kh3  Bc5 86 . Kg2 Kg7 87 . Qb7 + Kh6 88 . Qe4 Kg7 89 . Qg4 Kh6 90 . Qh3 + Kg7 91 . Qd7 + Kh6  92 . Qg4 Kg7 1/2-1/2"




#test = "1 . d4 Nf6 2 . Nf3 e6 3 . c4 c5 4 . e3 d5 5 . Nc3 cxd4 6 . exd4 Bb4 7 . cxd5 Nxd5 8 . Bd2"



# 546 "words" - 1347 tokens
#test = "1 . d4 Nf6 2 . c4 e6 3 . Nc3 Bb4 4 . Qc2 O-O 5 . e4 d5 6 . e5 Nfd7 7 . a3 Be7 8 . cxd5  exd5 9 . Nxd5 c5 10 . Bd3 Kh8 11 . Bxh7 Nc6 12 . Be4 cxd4 13 . Qe2 g6 14 . h4 Ndxe5  15 . Bg5 Bxg5 16 . hxg5 + Kg7 17 . Nf6 Rh8 18 . Rxh8 Qxh8 19 . f4 Qh2 20 . Qf2 Ng4 21 .  Nxg4 Bxg4 22 . Bxc6 bxc6 23 . Qxd4 + Kg8 24 . Kf1 Re8 25 . Re1 Rxe1 + 26 . Kxe1 Qxg2  27 . Qxa7 Qe4 + 28 . Kd2 Qg2 + 29 . Ke1 Qxb2 30 . Qe3 Qg2 31 . a4 Qd5 32 . Kf2 Qa2 + 33 .  Kg3 Be6 34 . Nf3 Qxa4 35 . Ne5 Qc2 36 . Qd3 Qc1 37 . Qf3 Bd5 38 . Qf2 Qc3 + 39 . Kh2  Be6 40 . Qf3 Qd2 + 41 . Kg3 c5 42 . Qa8 + Kg7 43 . Qa1 Qe3 + 44 . Nf3 + Kh7 45 . Qe5 Qa3  46 . Qd6 Qc1 47 . Qd2 Qf1 48 . Qd6 Qh3 + 49 . Kf2 Bg4 50 . Ng1 Qh2 + 51 . Kf1 Qc2 52 . Ke1 c4 53 . Qf6 Qd1 + 54 . Kf2 Kg8 55 . Qe5 Qb3 56 . Qe8 + Kg7 57 . Qe5 + Kh7 58 . Qd5 Qb2 +  59 . Kg3 Be6 60 . Qf3 Qd2 61 . Ne2 Bd5 62 . Qf2 Qd3 + 63 . Kh2 c3 64 . f5 gxf5 65 . Nxc3  Bc4 66 . Qh4 + Kg8 67 . Qg3 Qd2 + 68 . Kg1 Qd4 + 69 . Kh2 Kg7 70 . Qf3 Kg6 71 . Qc6 + Kxg5 72 . Qg2 + Kf6 73 . Qc6 + Be6 74 . Qf3 Qe5 + 75 . Kg1 f4 76 . Ne4 + Kg6 77 . Qg2 + Kf5 78 .  Nd2 Bd5 79 . Qf2 Qh8 80 . Qc5 Qh1 + 81 . Kf2 Kg4 82 . Qc8 + f5 83 . Qd7 Qg2 + 84 . Ke1  Qg3 + 85 . Kd1 Qg1 + 86 . Kc2 Qc5 + 87 . Kd1 Kg3 88 . Qg7 + Kf2 89 . Qb2 Bf3 + 90 . Nxf3 +  Kxf3 91 . Qc3 + Qe3 92 . Qc6 + Qe4 93 . Qc3 + Kg2 94 . Qb2 + Kg3 95 . Qg7 + Kf2 96 . Qb2 +  Ke3 97 . Qd2 + Kf3 98 . Qc3 + Qe3 99 . Qc6 + Kg3 100 . Qg6 + Kf2 101 . Qxf5 f3 102 . Qh7  Qe2 + 103 . Kc1 Kg1 104 . Qg7 + Qg2 105 . Qd4 + Kf1 106 . Qd1 + Kf2 107 . Qd4 + Kg3 108 .  Qe5 + Kh4 109 . Qh8 + Kg4 110 . Qg7 + Kh3 111 . Qh8 + Kg3 112 . Qe5 + Kg4 113 . Qg7 + Kf5  114 . Qf7 + Ke4 115 . Qe6 + Kd3 116 . Qd5 + Ke3 117 . Qe5 + Kf2 1/2-1/2"

def tokenHelp(s):
    try:
        if s=="":
            return []
        t = dictToken[s]
        print(s, "IN DICT")
        #print(t, "Found token")
        return [t]
    except KeyError as e:
        print(s, "not in dict")
        
        return tokenHelp(s[0]) + tokenHelp(s[1:])

def tokenize(game):
    ans = []
    subGame = game.split(" ")

    for i in subGame:
        ans = ans + tokenHelp(i)
        ans = ans + tokenHelp(" ")
    return ans

    # ind=0
    # curr=0

    # while(ind<len(game)):
    #     print(game[ind])
    #     ind=ind+1

temp  =tokenize(test)
print(temp)
print(len(temp))
print(len(test.split(" ")))
#print(tokenize("exd4"))