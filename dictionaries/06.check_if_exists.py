programmer = {
    "name": "Alice",
    "position": "Full Stack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto al abuscar  en el directorio, se busca por las llaves
if "position" in programmer:
    print("Existe la posición")

# No va a buscar directamente en los valores
if "Alice" in programmer:
    print("Alice está presente")

# De esta forma podeos buscar en los valores
if "Alice" in programmer.values():
    print("Alice esta en los valores")

