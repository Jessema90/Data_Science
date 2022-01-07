def run():

    #squares=[i**2 for i in range(1,101) if i%3!=0]
    #print(squares)


    # Lista de todos los multiplos de 4, que a la vez son multiplos de 3 y de 9
    lista=[i for i in range(1,100000) if i%36==0]
    print(lista)


if __name__=='__main__':
    run()

