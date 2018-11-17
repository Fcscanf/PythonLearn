a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [i * i for i in a]
print(b)

students = {
    'Fc': 18,
    'Doc': 20,
    'Re': 16
}

b = {value: key for key, value in students.items()}
print(b)
b = {key for key, value in students.items()}
print(b)
b = (key for key,value in students.items())
for x in b :
    print(x)