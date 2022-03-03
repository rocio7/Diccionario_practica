#1 Actualizar valores en diccionarios y listas


x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x[1][0]= 15

print(x)
#1.2
estudiantes [0]['last_name']='Bryant'

print(estudiantes)
#1.3
directorio_deportes ['fútbol'][0]='Andrés'

print(directorio_deportes)
#1.4
z[0]['y']='30'
print(z)

# 2.Iterar a través de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes):
    cadena=""
    for e in estudiantes:
        for k,v in e.items():
            cadena=cadena+k + " - "+ v+", "
        print(cadena)
        cadena=""


iterateDictionary(estudiantes)

# 3. Obtener valores de una lista de diccionarios

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',estudiantes)
iterate_dictionary2('last_name',estudiantes)


# def iterateDictionary2 (estudiantes):
#     for e in estudiantes:
#         for name in e.values():
#             print(name)

# iterateDictionary2 (estudiantes)




#4.Iterar a través de un diccionarios con valores de lista

dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(diccionario):
    for k,v in diccionario.items():
        print("--------------")
        print(f"{len(v)} {k.upper()}")
        for i in range(0, len(v)):
            print(v[i])
print_info(dojo)
