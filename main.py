'''
2.1 Feladat
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!

2.2 Feladat
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő szavakat is elfogadja.
'''

lista = []
while True:
    beker = input('Kis "a" betűvel kezdődő szavak: ')
    if beker == "":
        break
    if beker[0] == "a" or beker[0] == "A":
        lista.append(beker)
print(lista)
