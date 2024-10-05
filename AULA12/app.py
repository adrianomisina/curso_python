# open("caminho", "r")

# Mode
# r - leitura
# a - Append / Incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura  + Escrita

# arquivo = open("AULA12/text.txt", "r")
arquivo = open("AULA12/text.txt", "a")

# print(arquivo.readable())
# print(arquivo.read())

# ler a 1ª linha do arquivo
# print(arquivo.readline())
# depois de ler a 1ª le as demais na ordem
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# ['Pynthon\n', 'JavaScript\n', 'Java\n', 'C#\n', 'Node\n', 'R\n', 'React\n', 'Angular\n', 'Vue\n', 'Golang\n'] \n quebra de linha

# print(lista)
# print(lista[3])

# arquivo.write("\nSQL")
# arquivo.write("C++\n")

# arquivo.close()

# import os

# if os.path.exit("AULA12/text.txt"):
#   os.remove("AULA12/text.txt")
# else: 
#   print("Arquivo não existe")  

# remover pasta apenas se tiver vazia:

# os.rmdir("AULA12/nova-pasta")