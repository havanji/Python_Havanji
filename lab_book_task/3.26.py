print("-----3.26-----")
print("---TTT---")
x = True
y = True
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---FTT---")
x = False
y = True
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---TFT---")
x = True
y = False
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---TTF---")
x = True
y = True
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---FFT---")
x = False
y = False
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---TFF---")
x = True
y = False
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---FTF---")
x = False
y = True
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print("---FFF---")
x = False
y = False
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))
