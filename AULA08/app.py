# tenho_sede = False

# if tenho_sede:
#   print("beber agua")

# print("Vida que segue")

# esta_frio = True

# if esta_frio:
#   print("Vestir um casaco")
# else:
#   print("Vestir camiseta")

tenho_sede = True
tenho_fome = True
estou_em_dieta = True

# OR
# if tenho_sede or tenho_fome:
#   print("vou na cosinha")
# else:
#   print("ficar vendo netflix")

# AND
# if tenho_sede and tenho_fome:
#   print("vou fazer sanduiche e coca")
# else:
#   print("não tenho fome e não tenho sede")


#ELIF

if tenho_sede and tenho_fome:
  print("pegar uma coca e fazer um lanche")
elif   tenho_sede and not(tenho_fome):
  if(estou_em_dieta):
    print("tomar água")
  print("Tomar uma coquinha apenas")
elif not(tenho_sede) and tenho_fome:
  print("Só fazer um sanduiche")
else:
  print("ficar vendo netflix")
