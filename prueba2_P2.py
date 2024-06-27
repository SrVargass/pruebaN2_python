lista=[]
for x in range(10):
 precio=int(input("ingrese el precio del producto:CLP "))
 lista.append(precio)
 
dolar=1/950

nueva_lista=[]

for x in lista:
    res=(dolar)*x
    nueva_lista.append(res)

print(nueva_lista)


