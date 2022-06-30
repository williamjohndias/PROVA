word = input("Digite uma palavra: ")

acount, ecount, icount, ocount, ucount, consoantes = 0, 0, 0, 0, 0, 0

for i in list(word):
    if str.lower(i) == "a":
        acount+=1

    if str.lower(i) == "e":
        ecount+=1

    if str.lower(i) == "i":
        icount+=1

    if str.lower(i) == "o":
        ocount+=1

    if str.lower(i) == "u":
        ucount+=1

    if str.lower(i) != "a" and str.lower(i) != "e" and str.lower(i) != "i" and str.lower(i) != 'o' and str.lower(i) != 'u':
        consoantes+=1


print(f"Letras A: {acount}\nLetras E: {ecount}\nLetras I: {icount}\nLetras O: {ocount}\nLetras U: {ucount}")
print(f"consoantes: {consoantes}")
