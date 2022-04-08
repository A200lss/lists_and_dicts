programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]

}

keys = programmer.keys()
values = programmer.values()
items = programmer.items()

print(keys)
print(values)
print(items)

# Estamos agregando un nuevo items

programmer["dream"] = "Be a Python pro"

#Las llaves se actualizan considerando la nueva llave y valor agregados

print(keys)