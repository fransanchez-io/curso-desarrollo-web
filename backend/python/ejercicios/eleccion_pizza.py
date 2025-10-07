pizza_vegana= "vegana"
pizza_novegana= "no vegana"

pizza=input("Que pizza quieres, tenemos vegana y no vegana: ")

if pizza==pizza_vegana:
    print("Los ingredientes de la pizza vegana son: Pimineto y tofu")
    ingrediente=input("Cual es el que quiere: ")
    print("Pizza vegana con mozzarella, tomate y ", end="")
    if ingrediente=="Pimiento":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Los ingredientes de la pizza no vegana son: peperoni, jamon y salmon")
    ingrediente=input("Cual es el que quiere: ")
    print("Pizza no vegana con mozzarella, tomate y ", end="")
    if ingrediente=="peperoni":
        print("Peperoni")
    elif ingrediente=="jamon":
        print("Jamon")
    else:
        print("salmon")