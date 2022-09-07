list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["Naufal", "Fadli", "Abyan", "Desta"]
list_mix = [20, "Arya", True, "Bryan"]

print("Data sebelum diubah:", list_string)
list_string[0] = "REndra"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_string)
list_string[1] = "Jamil"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_string)
list_string[2] = "Fadil"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_string)
list_string[3] = "Wicak"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_mix)
list_mix[0] = 40
print("Data setelah diubah:",list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[1] = "Fadlan"
print("Data setelah diubah:",list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[2] = "False"
print("Data setelah diubah:",list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[3] = "Zayn"
print("Data setelah diubah:",list_mix)

#perulangan  for

x = ["Naufal", "Fadli", "Abyan", "Desta"]
for y in x:
    print(y)
print("\n")
for i in list_string:
    print(i)
print("\n")
for a in list_mix:
    print(a)
print("\n")
for c in list_integer:
    print(c)

 
