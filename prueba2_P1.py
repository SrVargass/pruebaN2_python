lista=[]
nota=float(input("ingrese una nota(ingrese 0 para finalizar):"))
while nota!=0:
    lista.append(nota)
    nota=float(input("ingrese una nota(ingrese 0 para finalizar):"))
    
print("1) la cantidad de notas son",len(lista))

suma=0
for x in lista:
      suma+=x
print("2) el promedio de las notas ingresadas son:",suma/len(lista))

cont=0
cont2=0
for x in lista:
    if x<4.0:
        cont=cont+1
    elif x>=4.0:
        cont2=cont2+1

print("3) la notas que fueron menor a 4.0 son:",cont)
print("4) las notas que fueron mayor o igual a 4.0 son:",cont2)