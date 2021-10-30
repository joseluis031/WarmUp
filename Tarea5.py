Mi_edad = 18
Hambre = Mi_edad
Dinero_inicial = 2000
Precio_inicial_helado = 100
Helados_comidos = 0
while (Hambre) < 85 and (Dinero_inicial-Precio_inicial_helado) > 0 :
    Dinero_inicial = Dinero_inicial - Precio_inicial_helado
    Precio_inicial_helado = Precio_inicial_helado + (Precio_inicial_helado *0.2)
    Helados_comidos = Helados_comidos + 1
    Hambre = Hambre + Mi_edad
    if (Hambre + Mi_edad) >= 100:
        break
print ("Nivel de satisfaccion:" + str(Hambre))
print ("Helados comidos:" + str(Helados_comidos))
print ("Dinero restante:" + str(Dinero_inicial))