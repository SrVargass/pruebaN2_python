diccionario={}
t={}
for x in range(5):
    capital=input("ingrese una capital:")
    pais=input("ingrese pais de la capital:")
    diccionario[capital]=pais 
print("")

turista=input("INGRESE EL NOMBRE DEL TURISTA:")
procedencia=input("ingrese la capital de procedencia:")
t[turista]=procedencia


for capital in diccionario: 
    if capital == procedencia:
        pais_turista = diccionario[capital]
        break
print("El turista con nombre:", turista, "\nEs de la capital:" ,procedencia,"\nsu país es:" ,pais_turista)
