print("-----3.23-----")
print("---TTT---")
a = True
b = True
c = True
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---FTT---")
a = False
b = True
c = True
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---TFT---")
a = True
b = False
c = True
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---TTF---")
a = True
b = True
c = False
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---FFT---")
a = False
b = False
c = True
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---TFF---")
a = True
b = False
c = False
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---FTF---")
a = False
b = True
c = False
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("---FFF---")
a = False
b = False
c = False
print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)
