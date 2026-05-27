import csv

with open(r"c:\Users\abija\introducao-aos-algoritimos\introducao-aos-algoritimos\AP12-Spotify\dados.csv", "r", encoding='utf8') as arq, \
    open("musicas_antigas.txt", "w", encoding='utf8') as saida:
    reader = csv.reader(arq)
    next(reader)
    for i, data in enumerate(reader, start=1):
        if len(data) < 15:
            continue
        if int(data[1]) < 1925:
            saida.write(f"{i}- {data[14]} {data[1]}\n")