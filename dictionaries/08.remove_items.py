programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Metodo pop en los diccionarios retiene las llaves a eliminar
programmer.pop("position")
print(programmer)

#position = programmer.pop("position")
#print(programmer)
#print(position)

#Eliminar el diccionario completo
del programmer

#print(programmer)

programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]

}

# Vaciar el contenido del diccionario pero manteniendo la variable
programmer.clear()

print(programmer) #Esto es lo que imprime {}


