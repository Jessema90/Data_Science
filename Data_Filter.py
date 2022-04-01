DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    # 1) Todos los desarrolladores de python
    all_python_devs=[worker["name"] for worker in DATA if worker['language']=='python']

    # Otra forma de hacerlo para encontrar  aquellos que trabajen el lenguaje python

    all_python_devs_2=list(filter(lambda worker : worker['language']=='python',DATA))
    all_python_devs_2=list(map(lambda worker: worker['name'], all_python_devs_2))
    for worker in all_python_devs_2:
        print(worker)


    # 2) Todos los trabajadores de platzi
    #all_platzi_workers=[worker["name"] for worker in DATA if worker['organization']=='Platzi']

    all_platzi_workers_2=list(filter(lambda worker : worker['organization']=='Platzi',DATA))
    all_platzi_worker_2=list(map(lambda worker : worker['name'], DATA))

    print("**************TRABAJADORES DE PLATZI***********")
    #for worker in all_platzi_worker_2:
    #    print(worker)

    # 3) Vamos a buscar los adultos o los mayores de 18

    # Usando list comprehensions
    #all_adults_1=[worker['name'] for worker in DATA if worker['age']>=18]

    #print("********Trabajadores mayores de 18 años********")
    #for worker in all_adults_1:
    #    print(worker)

    # Usando filter
    #all_adults=list(filter(lambda worker : worker['age']>=18, DATA))
    #adults=list(map(lambda worker:worker['name'], all_adults))
    #print(all_adults)
    #print(adults)

    # Para cada uno de los trabajadores y diccionaries, voy a agregar a ese nuevo diccionario
    # en un diccionario nuevo el valor true/false dependiendo de la edad del trabajador

    print("*****Ensayos con list comprehensions ****")

    DATA_BACK=DATA
    
    #old_people_2=[{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    #old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    #old_people=[{worker: {"old":worker["age"]>=70}} for worker in DATA_BACK]

    #old_people = [worker['name'] for worker in DATA if worker ['age'] > 70 ]

    #for worker in old_people:
    #    print(worker)

    #print(old_people_2)

    #for worker in DATA_BACK:
        #print(worker["age"])

    #print(DATA_BACK)
        #DATA_BACK["age"]=old_people[worker]  
    #print(DATA)

    #valor=DATA[1]
    #valor["Age"]=(valor)    
    #print((DATA['name']))

    old_people=list(map(lambda worker: worker | {"old":worker['age']>70},DATA))
    #old_people=list(map(lambda worker: worker | {"old":worker['age']>70},DATA))
    #for worker in old_people:
#    print(worker)

    # Usando List Comprehensions
    old_people_2 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    for worker in old_people_2:
        print(worker)

    #print(DATA)
    #for worker in all_platzi_workers:
    #    print(worker)
    
    # Lista de todos los adultos
    #for worker in adults:
    #    print(worker)
        
    #for worker in old_people:
    #    print(worker)


if __name__=='__main__':

    run()

    



