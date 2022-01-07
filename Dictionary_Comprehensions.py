import numpy as np

def run():

    my_dict={}
    vector=[]

    val=[i for i in range(1,101) if i%3!=0]

    for i in range(1,101):
        if i%3!=0:
            my_dict[i]=i**3
    #print(my_dict)


    ## Otra forma de hacerlo
    my_dict_2={i: i**3 for i in range(1,101) if i%3!=0}
    #print(my_dict_2)

    ## Ejemplo:
    # Crear con un dictionary comprehensions un diccionario cuyas llaves
    # sean los 1000 primeros numeros naturales con sus raices cuadradas como valores

    my_dict_3={i: round(np.sqrt(i),2) for i in range(1,1001)}
    print(my_dict_3)


if __name__=='__main__':
    run()
