import os
import readLines

numBlocks = len(os.listdir('blockchain'))
for i in range(0, numBlocks):
    readLines.lines('blockchain/' + str(i))