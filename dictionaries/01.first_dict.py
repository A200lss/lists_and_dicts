# Los diccionarios son estruturs similares a las listas o arreglos, pero se accede a sus 
#elementos mediante "llaves" o "keys" y no por sus índice

# Ejemplo
# Definimos un diccionario utilizando llaves o "curly braces"

programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]

}

# Accedemos a los elementos por la llave
print(programmer["name"])
# No podemos acceder por los indices
#print(programmer[0])
print(programmer["position"])
print(programmer["skills"])

# Tambien podemos acceder a sus elementos por su metodo get()
print(programmer.get("position"))

# Son de tipo <class 'dict'> para
print(type(programmer))

# Podemos acceder a todas sus llaves con el metodo keys
keys = programmer.keys()
print(keys)