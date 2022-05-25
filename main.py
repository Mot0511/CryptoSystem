import hashlib
import os
import readLines

sender = input('Отправитель: ')
money = input('Кол-во: ')
to = input('Получатель: ')

filesStr = os.listdir('blockchain')
files = []

hash = hashlib.sha256()
if (filesStr == []):
    hash.update(bytes('0' + sender + money + to, encoding='utf8'))
    hash = hash.hexdigest()

    block = open(f'blockchain/1', 'w')
    block.write(hash + '\n' + '0' + '\n' + sender + '\n' + money + '\n' + to)

else:
    for i in filesStr:
        files.append(int(i))

    maxFile = max(files)

    prevHash = open(f'blockchain/{maxFile}', 'r')
    prevHashText = []
    for i in prevHash:
        prevHashText.append(i.strip())

    hash.update(bytes(prevHashText[0] + sender + money + to, encoding='utf8'))
    hash = hash.hexdigest()

    block = open(f'blockchain/{str(maxFile + 1)}', 'w')
    block.write(hash + '\n' + prevHashText[0] + '\n' + sender + '\n' + money + '\n' + to)
