def attack(castle):
    print('Atacar {}'.format(castle))

castle="Loimbard"

if castle == "Camelot" or "Loimbard":
    attack(castle)
else:
    attack("niguem")


tipo = type(22.4)
print(tipo)
if str(tipo).find("float"):
    print("Valor")
else:
    print("Quantidade")