def run():

        Letra=(input("Ingresa una letra: "))
        #Check_letter=type(Letra)

        Check_letter=Letra.isdigit()

        if(Check_letter==True):
            print("No es una letra")
        else:
            print("Es una letra")


if __name__=='__main__':
    run()