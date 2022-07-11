word = input("Digite uma palavra: ")
palavra = word.lower()
letraa = palavra.count('a')
letrae = palavra.count('e')
letrai = palavra.count('i')
letrao = palavra.count('o')
letrau = palavra.count('u')
vogais = letraa + letrae + letrai + letrao + letrau
print('VOGAIS: ', vogais)
consoantes = word.count("") - vogais - 1
print('CONSOANTES', consoantes)
