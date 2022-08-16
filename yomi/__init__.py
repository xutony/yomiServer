# import io
from . import Kana

Kana_Table = []

with open("kanji.txt", 'r', encoding='utf-16') as f:
    lines = f.readlines()
    for line in lines:
        token = line.strip('\n').split('\t')
        k = Kana.Kana(token[0], token[1], token[2])
        Kana_Table.append(k)
f.close()
