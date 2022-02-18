print("-----3.25-----")
print("---TTT---")
a = True
b = True
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---FTT---")
a = False
b = True
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---TFT---")
a = True
b = False
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---TTF---")
a = True
b = True
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---FFT---")
a = False
b = False
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---TFF---")
a = True
b = False
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---FTF---")
a = False
b = True
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print("---FFF---")
a = False
b = False
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))
