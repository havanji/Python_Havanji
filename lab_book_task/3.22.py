print("-----3.22-----")
print("---TTT---")
x = True
y = True
z = True
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---FTT---")
x = False
y = True
z = True
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---TFT---")
x = True
y = False
z = True
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---TTF---")
x= True
y = True
z = False
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---FFT---")
x = False
y = False
z = True
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---TFF---")
x = True
y = False
z = False
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---FTF---")
x = False
y = True
z = False
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print("---FFF---")
x = False
y = False
z = False
print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))
