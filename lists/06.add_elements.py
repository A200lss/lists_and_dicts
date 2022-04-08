todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

# Agrega un item en el índice del primer parámetro, desplazando los otros items
todo_list.insert(2, "bañarme")

# Agrega al final
todo_list.append("Ver Friends")

print(todo_list)

# Mezclar
movies = ["El día de la idependencia", "Aerican Pie", "Scary Movie"]

books = ["Harry Potter", "The Bro Code", "Como entrenar a tu dragón"]

# Entregar al final todo el arreglo entregado como parámetro
movies.extend(books)

print(movies)

print(books)