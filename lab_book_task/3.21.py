print("-----3.21-----")
print("---TTT---")
a = True
b = True
c = True
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---FTT---")
a = False
b = True
c = True
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---TFT---")
a = True
b = False
c = True
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---TTF---")
a = True
b = True
c = False
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---FFT---")
a = False
b = False
c = True
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---TFF---")
a = True
b = False
c = False
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---FTF---")
a = False
b = True
c = False
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))

print("---FFF---")
a = False
b = False
c = False
print(not (a or not b and c))
print(a and not(b or not c))
print(not (not a or b and c))
