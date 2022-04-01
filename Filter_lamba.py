from typing import MutableMapping


def run():
    
    my_list1=[1,4,5,6,9,13,19,21]

    # Ejemplo 1
    # Tomaremos los elementos de la lista que no son divisibles entre 2
    odd1_1=[i for i in my_list1 if i%2!=0] # Usando list comprehensions
    odd1_2=list(filter(lambda x: x%2!=0, my_list1)) # usando filters
    print(odd1_1)
    print(odd1_2)


    # Ejemplo 2
    # Tomaremos los elementos de la lista y los elevaremos al cuadrado
    my_list2=[1, 2, 3, 4, 5]
    square1=[i**2 for i in my_list2]  # Con list comprehensions
    square2=list(map(lambda x: x**2 , my_list2))
    print(square1)
    print(square2)

    # Ejemplo 3
    # Tomaremo slos elementos de la lista y los multplicaremos entre si
    my_list3=[2,2,2,2,2]
    mult=1

    for i in my_list3 :
        mult=mult*i
    
    print(mult)


 





if __name__=='__main__':
    run()

