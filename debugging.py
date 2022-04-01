# Utiliza las palabras clave try , except y raise, para elevar un error si el usuario ingresa un
# numero negativo en nuestro programa de divisiones



def divisor(num):

    # try:
    #     if num<3:
    #         raise ValueError("Debes ingresar un numero positivo")
    
    #     divisors=[]
    #     for i in range(1,num+1):
    #         if num%i==0:
    #             divisors.append(i)
    #     return divisors
    # except ValueError as ve:
    #     print(ve)

    # Usando assert statements
    assert num>0, "Debes ingresar un numero positivo"
    divisors=[]
    for i in range(1,num+1):
         if num%i==0:
                divisors.append(i)
    return divisors

def run():
    try:
        num=int(input("Ingresa un numero: "))
        print(divisor(num))
        print("Finished the program")
    except ValueError :
        print("Debes ingresar un numero")

# Usando assert statements








if __name__=="__main__":
    run()

