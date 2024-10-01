try:
  numero = int (input("Digite um número: "))
  print(numero)

except ZeroDivisionError:
  print("Divisão por zero não é possivel")

except ValueError: 
  print("Digite um valor valido.")

except:
  print("Erro inesperado")

finally:
  print("Sempre executa")