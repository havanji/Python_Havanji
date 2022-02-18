print("-----3.24-----")
print("---TTT---")
x = True
y = True
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---FTT---")
x = False
y = True
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---TFT---")
x = True
y = False
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---TTF---")
x= True
y = True
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---FFT---")
x = False
y = False
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---TFF---")
x = True
y = False
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---FTF---")
x = False
y = True
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print("---FFF---")
x = False
y = False
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)
