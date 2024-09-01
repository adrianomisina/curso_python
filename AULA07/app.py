# def big_mac():
#   print("sanduiche big mac")

# print("inicio")
# big_mac()
# print("fim")

def fazer_big_mac(nome):
  print(f'sanduiche big mac de {nome}')
# fazer_big_mac("Adriano")
# fazer_big_mac("Takashi")
# fazer_big_mac("Misina")

def fazer_batata(tamanho):
  print(f'batata {tamanho}')

def preparar_refrigerante(tipo, tamanho):
  print(f"{tipo} {tamanho}")

# fazer_big_mac("Adriano")
# fazer_batata("média")
# preparar_refrigerante("Sprit", "média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
  fazer_big_mac(nome)
  fazer_batata(tamanho_batata)
  preparar_refrigerante(tipo_refri, tamanho_refri)

# fazer_combo_big_mac("Adriano", "Batata Grande", "Coca", "Media")

def soma_num(num1, num2):
  return num1 + num2

resultado = soma_num(15, 20)

# print(resultado)

def maior_num(lista_num):
  lista_num.sort()
  lista_num.reverse()
  maior_num = lista_num[0]
  return maior_num

resultado = maior_num([321, 654, 68478, 798, 2, 165, -1, 52, -46, 3654, 2, 7])
print(resultado)