#listeyi düzleştiren (flatten) fonksiyon
giris = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
new = []

def flatten(x):
    for i in x:
        if type(i)==list:
            flatten(i)
        else:
            new.append(i)
flatten(giris)
print(new)

# Verilen listenin içindeki elemanları tersine döndüren fonksiyon

input2 = [[1, 2], [3, 4], [5, 6, 7]]
liste = []

def rever(a):
    for i in a:
        if type(i)==list:
            i.reverse()
            liste.append(i)
rever(input2)
print(liste)