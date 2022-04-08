programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto itera sobre las llaves, pero podría ser cualquer nombre: ej attr
for key in programmer:
    print(key)

# Podriamos imprimir los 
for key in programmer:
    print(programmer[key])

for key, value in programmer.items():
    print(key, ":", value)