def change():
    expense = 23.75
    money = 100

    print(f"Ingresar gasto: \n{expense}")
    print(f"Dinero recibido \n{money}\n")
    print(f"Vuelto \n\nPesos:")
    total_int = int(money) - int(expense) - 1
    print(total_int)
    print(f"Centavos:")
    resto_float = int((money - expense - total_int) *100)
    print(resto_float)
