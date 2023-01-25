

import os
import sys
import pickle
from tqdm import tqdm



prePath = os.path.join("dataPre", "KingBase2019", "kingCleanPre.pgn")

file = open(prePath, "r")

text = file.read()

file.close()

text = text.replace("\n\n\n", " ")
text = text.replace("\n", " ")
text = text.replace("  ", " ")
text = text.replace(" . ", ".")
text = text.replace(". ", ".")
text = text.replace(" .", ".")
text = text.replace(".", ". ")

# print(text[:3000])

ans = {}
ansArr = ["<N>","<unk>","<pad>","<mask>","</N>","K", "Q", "N", "B", "R", "x"," ", "=", "#", "*"]
for i in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    for j in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        ansArr.append(i+j)
ansArr = ansArr + ["a", "b", "c", "d", "e", "f", "g", "h"]
ansArr = ansArr + ["1", "2", "3", "4", "5", "6", "7", "8"]
tarr = text.split(" ")

for i in tqdm(tarr):
    if i in ansArr:
        pass
    else:
        ansArr.append(i)
# #%%
# print(len(ansArr))

# print(ansArr[50:58])

# #%%

# print(ansArr[8740])
# # %%
# if "e4" in ansArr:
#     print("interest")

# print(ansArr.index("1"))


# for i in range(8):
#     if str(i+1) in ansArr:
#         pass
#     else:
#         ansArr.append(str(i+1))


#         if i+j in ansArr:
#             pass
#         else:
#             ansArr.append(i+j)

for i, j in tqdm(enumerate(ansArr)):
    ans[j] = i


postPath = os.path.join("data", "KingBase","tokens", "tokenV1.pkl")

a_file = open(postPath, "wb")
pickle.dump(ans, a_file)
a_file.close()



# postPath = os.path.join("data", "KingBase","tokens", "tokenV1.pkl")
# a_file = open(postPath, "rb")
# output = pickle.load(a_file)
# print(output)
# a_file.close



# print(output["e7"])

