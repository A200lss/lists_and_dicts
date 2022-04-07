todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

for todo in todo_list:
    print(todo)

index = 0
while index < len(todo_list):
    print(todo_list[index])
    index += 123

# El indice termina  en 5 por la ultima interacción
print(index)

# Utilizandio list comprehension
[print(todo) for todo in todo_list]
