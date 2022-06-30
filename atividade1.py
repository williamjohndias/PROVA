x = 0
lista = []
while True:
    n = int(input('Digite um número: [ %s ]: ' % x))
    if x == 5:
      print('FIM DA LISTA')
      break
    else:
      lista.append(n)
      x += 1

print('Esses são os números que você digitou: ', lista)
rev = lista[:]
rev.reverse()
print('Essa é a lista reversa: ', rev)
diferenca = max(lista) - min(lista)
print(f"A diferença entre o maior valor {max(lista)} e o menor valor {min(lista)} foi de: ",diferenca)
