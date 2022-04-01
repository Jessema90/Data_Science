import numpy as np
import os


HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |  
      |
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |  
  |   |
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
  |   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
 /|   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
 /|\  |
      |
      |
      |
      |
=========''', '''
  +---+
  |   | 
  |   |
  O   |
 /|\  |
  |   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
 /|\  |
  |   |
 /    |
      |
      |
=========''', '''
  +---+
  |   |
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
      |
=========''']


def run():
    
    read()
    Words=read()
    Option_list=list(range(len(Words)+1))
    RandWord=np.random.choice(Option_list)
    Palabra_Nueva=[]
    Opciones=len(HANGMANPICS)
    Palabraf=Words[RandWord]
    Palabra=list(Palabraf)
    Value=len(Palabra)-1
    negativo=0
    Count=0
    Conteo=0

    Palabra_Nueva=np.full(Value,"_")
    for j in range(Value):
        print(Palabra_Nueva[j],end=' ')
    print("\n")
    print(negativo,"\n")

    while (negativo<Opciones):
        Count=0
        os.system("cls")
        print("**************Bienvenidos al Juego del Ahorcado****************** \n ")
        print(" *** Adivina la palabra  **** \n ")
        print(HANGMANPICS[negativo], "\n")
        Conteo=0
        
        for j in range(Value):
            print(Palabra_Nueva[j],end=' ')
        print("\n")

        Letra=(input("Ingresa una letra: "))
        for h in range(Value):
            if(Palabra[h]==Letra):
                Palabra_Nueva[h]=Letra
                Count=Count+1
           
            print(Palabra_Nueva[h],end=' ')
            print("\n")
            #print(negativo)
            
            if(Palabra[h]==Palabra_Nueva[h]):
                Conteo=Conteo+1

        if(Count==0):
            negativo=negativo+1
           
        if (Conteo==Value) :
            os.system ("cls") 
            print("**************Bienvenidos al Juego del Ahorcado****************** \n ")
            print(" Haz Ganado , la palabra era: ",Palabraf )
            break

        if (negativo==Opciones-1):
            os.system ("cls") 
            print("**************Bienvenidos al Juego del Ahorcado****************** \n ")
            print(HANGMANPICS[len(HANGMANPICS)-1], "\n")
            print(" Haz perdido")
            break

def read():
    Words_2={}
    words=[]
    with open("./Files/data.txt","r",encoding="utf-8") as f:
        for name in (f):
            words.append(name) 
    Values=len(words)
    Names_Dict={word  for word  in words}

    for i in range(Values):
        Words_2[i]=words[i]


    return Words_2


if __name__=='__main__':
    os.system ("cls") 
    print("**************Bienvenidos al Juego del Ahorcado****************** \n ")
    print(" *** Adivina la palabra  **** \n ")
    run()


