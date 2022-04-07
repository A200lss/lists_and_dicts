todo_list = ["estudiar python", "sacar la basura", "alimentar a Boby", "Recibir el bono", "barrer la entrada"]

def check_if_exist(check, list):
    if check in list:
        return

if check_if_exist("Comer pastel", todo_list):
    print("Tienes cosas por hacer")
else:
    print("Sin bono sigo en cama")