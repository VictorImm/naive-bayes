import numpy as np
from pandas import read_csv

def laplacianSmoothing(df, naive, probL, probTL):
    # akses tiap kolom
    for i in range (2, 9):
        # ambil nilai unik kolom
        temp = (np.unique(df.iloc[:, i]))
        status = 0
        # akses tiap nilai unik
        for j in temp:
            # cek apakah ada nilai 0 di dalam prob positive
            if 0 in naive[j]:
                for k in temp:
                    naive[k][0] += 1
                    naive[k][0] /= (probL+len(temp))
                status = 1
                break
        else:
            if status == 0:
                for k in temp:
                    naive[k][0] /= probL
        
        status = 0

        # akses tiap nilai unik
        for j in temp:
            # cek apakah ada nilai 0 di dalam prob negative
            if 0 in naive[j]:
                for k in temp:
                    naive[k][1] += 1
                    naive[k][1] /= (probTL+len(temp))
                status = 1
                break
        else:
            if status == 0:
                for k in temp:
                    naive[k][1] /= probTL
    
    return naive

def naiveBayes(data):
    df = read_csv('dataset naive bayes.csv')

    naive = {}

    probL = 0
    probTL = 0
    for i in range(28):
        if df.iloc[i][9] == 'L':
            probL += 1
        elif df.iloc[i][9] == 'TL':
            probTL += 1

    # cek tiap column
    for i in range(2, 9):
        # cek tiap row
        for j in range(28):
            # cek duplikat key
            if df.iloc[j][i] not in naive:
                
                countL = 0
                countTL = 0
                
                # training
                for k in range(28):
                    if df.iloc[k][9] == 'L' and df.iloc[k][i] == df.iloc[j][i]:
                        countL += 1
                    elif df.iloc[k][9] == 'TL' and df.iloc[k][i] == df.iloc[j][i]:
                        countTL += 1

                naive[df.iloc[j][i]] = [countL, countTL]

    naive = laplacianSmoothing(df, naive, probL, probTL)

    probL /= 28
    probTL /= 28

    for i in range(7):
        probL *= naive[data[i]][0]
        probTL *= naive[data[i]][1]

    if probL > probTL:
        return "Layak"
    else:
        return "Tidak layak"

# data = [None]*8
# data[0] = str(input("Masukkan nama : "))
# data[1] = str(input("Masukkan pekerjaan : "))
# data[2] = str(input("Masukkan usia : "))
# data[3] = str(input("Masukkan status : "))
# data[4] = str(input("Masukkan penghasilan : "))
# data[5] = str(input("Masukkan kendaraan : "))
# data[6] = str(input("Masukkan kepemilikan : "))
# data[7] = str(input("Masukkan kondisi atap : "))