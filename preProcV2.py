#163 game in Kingcleanpre have *
# not including them in V1


import os
import sys
from tqdm import tqdm
import uuid




prePath = os.path.join("dataPre", "KingBase2019", "kingCleanPre.pgn")
postPath = os.path.join("dataPre", "KingBase2019", "kingV1.pgn")


file = open(prePath, "r")

text = file.read()

games = text.split("\n\n\n")

print(len(games))
# print(games[0:3])
cleanGames = []
err= []
for i in games:
    temp = i.replace("\n", " ")
    temp = temp.replace("  ", " ")
    temp = temp.replace(" . ", ".")
    temp = temp.replace(". ", ".")
    temp = temp.replace(" .", ".")
    temp = temp.replace(".", ". ")
    # if "=" in temp:
    #     err.append(temp)
        
    if "*" not in temp:    
        cleanGames.append(temp)

# print(len(cleanGames))
# print(cleanGames[5])
file.close()
# print(len(err))
# print(err[5:10])
cnt = 0
for i in tqdm(cleanGames):
    # print(cnt)
    # cnt=cnt+1
    p = os.path.join("data", "KingBase","games", str(uuid.uuid4())+".txt")
    fileOut = open(p, "w+")

    fileOut.write(i)
    fileOut.close()
# print(len(cleanGames))
