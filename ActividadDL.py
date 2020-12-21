res = str(input("Comes frutas?"))

if res == "no": print("Necesitas comer mas frutas..")
else:
    x = int(input("Cuantas veces a la semana comes frutas?")) 
    if x >= 5:
        print("Sigue asi!")
        if int(input("Cuantas frutas comes al dia?")) >= 2: print("Comes saludable")
        else: print("Te recomendaria comer una fruta mas")
    elif 5<x>2: print("Come mas frutas a la semana..")
    else: print("Necesitas comer frutas...")
