# Utiliza las palabras clave try , except y raise, para elevar un error si el usuario ingresa un
# numero negativo en nuestro programa de divisiones
def divisor(num):

    try:
        if num<3:
            raise ValueError("Debes ingresar un numero positivo")
    
        divisors=[]
        for i in range(1,num+1):
            if num%i==0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    num=(input("Ingresa un numero: "))
    assert num.isnumeric() , "Debes ingresar un numero"
    print(divisor(int(num)))
    print("Terminó mi programa")



if __name__ =='__main__':

    run()