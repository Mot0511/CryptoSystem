import os
import readLines
import hashlib

run = True
while True:
    numBlocks = len(os.listdir('blockchain'))
    for i in range(1, numBlocks):
        lines1 = readLines.lines('blockchain/' + str(i))
        lines2 = readLines.lines('blockchain/' + str(i + 1))

        hash = hashlib.sha256()
        hash.update(bytes(lines1[1] + lines1[2] + lines1[2] + lines1[4], encoding='utf8'))
        hash = hash.hexdigest()

        if (not(hash == lines2[1])):
            run = False
            break

    if (run == False):
        break

print('!!!!!!!ERROR!!!!!!!!!')