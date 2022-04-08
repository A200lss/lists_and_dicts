from xml.etree.ElementTree import Element


todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

# Podemos eliminar un elemnto en particulare
todo_list.remove("Recibir el bono")

print(todo_list)

# el metodo pop() remueve el último y lo retorna
element = todo_list.pop(2)

print(todo_list)

print(element)

# Lo elimina totalmente
del todo_list

todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

# Elimina un elemnto en particular
del todo_list[1]

todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

# Limpia toda la lista pero no la elimina de la lista
todo_list.clear()

print(todo_list)

