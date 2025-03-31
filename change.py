def change():
    expense = 23.75
    money = 100
    
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}\n")
    print(f"Vuelto\n\nPesos:")
    vuelto = money - expense
    print(int(vuelto))
    print(f"Centavos:")
    print(int((money - expense - int(vuelto)) *100))
