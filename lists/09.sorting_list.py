fruits = ["Mango", "Piña", "Durazno", "Plátano", "Arándanos"]

# El metodo sort() es destructivo. odifica la lista originala
fruits.sort()

print(fruits)

fruits.sort(reverse = True)

print(fruits)

grades = [10, 9, 10, 9, 8, 8, 5]

grades.sort(reverse = True)

print(grades)

cat_bag = ["hola", 12, True]

# NO es posibe comparar enteros con stringa de
print(cat_bag)

veggies = ["papas",  "Quinoa", "choclo", "Papas"]

veggies.sort(key = str.lower)

print(veggies)

def strLength(elem):
    return len(elem)

fruits.sort(key = strLength, reverse = True)

print(fruits)



