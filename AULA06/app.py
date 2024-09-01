familia = ["Adriano","Misina", "Jane", "Kenzo", "Melissa", "Horito", "Misina"]

# print(familia)

# # pegar por indice da colection 

# print(familia[0])
# print(familia[1])
# print(familia[2])
# print(familia[3])
# print(familia[4])

# # print(familia[5]) 
# #     print(familia[5])
# # IndexError: list index out of range

# # pegar indice de trás para frente
# print(familia[-1])
# print(familia[-2])
# print(familia[-3])
# print(familia[-4])
# print(familia[-5])

# # começando de indice especifico
# print(familia[2:])

# #retorna até 4, excluido o 4
# print(familia[2:4])

# print(familia)
# familia[3] = "Pipi"
# print(familia)

# familia.extend(["Vovó", "Vovô"])
# print(familia)

# familia.append("Cunha")
# print(familia)

# familia.insert(5, "Gato")
# print(familia)

# #remove o ultimo da lista
# familia.pop()
# print(familia)

# #remover qualquer outro elemento
# familia.remove("Gato")
# print(familia)

# # Removendo "Vovó" e "Vovô"
# familia = [membro for membro in familia if membro not in ["Vovó", "Vovô"]]
# print(familia)

# # familia.clear() - limpa alista
# print(familia)

# #retorna um indice específico
# print(familia.index("Pipi"))

# #retorna quantos elementos passado tem na lista
# print(familia.count("Misina"))

# idade_familia = [42, 36, 8, 11, 3]
# print(idade_familia)

# familia.sort()
# idade_familia.sort()

# print(familia)
# print(idade_familia)

# idade_familia.reverse()
# print(idade_familia)

# familia.reverse()
# print(familia)

familia2 = familia.copy()
print(familia2)

familia.remove("Misina")
print(familia)
print(familia2)

#tuple - imutáveis
coordenadas = (-49, -36)
coordenadas.pop()
coordenadas[0] = -47
print(coordenadas)