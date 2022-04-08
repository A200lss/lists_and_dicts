programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Actualizamos indica
programmer["position"] = "Sr Sofwart Developer"
print(programmer)


#Actualizando utilizando utilizando el metodo update entregando un diccionario con las llaves 
programmer.update({"name": "Alice Smith"})
print(programmer)

# Con update se pueden nuevas llaves con su valor
programmer.update({"Hobies": ["Gatos", "Jugar Playstation", "Mirar las estrellas"]})
print(programmer)
