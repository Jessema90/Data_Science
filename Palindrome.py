# def palindrome(string):
#     try:
#         if len(string)==0:
#             raise ValueError("No se puede ingresar una cadena vacia")
#         return string==string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False


## Usando assert statements

# Definición Numero 1
#def palindrome(string):

#    return string==string[::-1]


def palindrome(string):

    assert len(string)>0, "No se puede ingresar una cadena vacia"
    return string==string[::-1]

def run():
    
     try:
         print(palindrome(""))
     except TypeError:
         print("Solo se pueden ingresar strings")


if __name__ =='__main__':

    run()