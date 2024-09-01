minha_string = "qualquer texto u u u"

print(minha_string)
print(type(minha_string))

print(f"concatenar {minha_string} em string")

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())
print(minha_string.strip())
print(minha_string.replace("qualquer", "meu"))
print(minha_string.replace("u", "U" ,3))

print(len(minha_string))
print(minha_string[12])
print(minha_string.index("texto"))


x = "texto" in minha_string
print(x)

minhas_linhas = "\n linha 1,\n linha 2, \n linha 3"
print(minhas_linhas)