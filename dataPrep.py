import os
import tqdm

testParent = "dataPre/KingBase2019/KingBase2019-01"
testPaths = os.listdir(testParent)

print(testPaths)
for testPath in testPaths:
    file = open(testParent+"/"+testPath, "r")
    contents = file.readlines()
    print(len(contents), "len of contents")
    cnt = 0
    fin = ""
    for i in contents:
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