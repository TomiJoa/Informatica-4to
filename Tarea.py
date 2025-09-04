lis={}
precio=0
seguir="si"
print("Debe escribir continuar o comprar para usar el sistema")
while seguir == "si":
    con=input("Continuar o comprar:")
    if con=="continuar":
        prod=input("Producto a comprar:")
        pre=int(input("Precio del producto:"))
        lis[prod] = pre
        print(lis)
        precio+=lis.get(prod)
    elif con=="comprar":
        seguir=1
        print("Lista:", lis.keys())
        print("Precio total:$"+str(precio))
    else:
        print("error")
