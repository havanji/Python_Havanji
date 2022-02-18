print("ЗАВДАННЯ З КНИГИ")
print("-----3.1-----")
a = True
b = False
c = False

print(a or b)
print(a and b)
print(b or c)

print("-----3.2-----")
x = False
y = True
z = False

print(x or z)
print(x and y)
print(x and z)

print("-----3.3-----")
a = True
b = False
c = False

print(not a and b)
print(a and not b)
print(a and b or c)

print("-----3.4-----")
x = True
y = True
z = False

print(not x and y)
print(x or not y)
print((x or y) and z)

print("-----3.5-----")
a = True
b = False
c = False

print(a or b and not c)
print(not a and not b)
print(not (a and c) or b)
print(a and not b or c)
print(a and (not b or c))
print(a or (not(b and c)))

print("-----3.6-----")
x = False
y = False
z = True

print(x or y and not z)
print(not x and not y)
print(not (x and z) or y)
print(x and not y or z)
print(x and (not y or z))
print(x or (not(y or z)))

print("-----3.7-----")
a = True
b = False
c = False

print(a or not (a and b) or c)
print(not a or a and (b or c))
print((a or b and not c) and c)

print("-----3.8-----")
x = False
y = True
z = False

print(x and not (z or y) or not z)
print(not x or x and (y or z))
print((x or y and not z) and z)

print("-----3.9-----")
x = True
y = False
z = False
print(not x or not y or not z)
print((not x or not y) and (x or y))
print(x and y or x and z or not z)

print("-----3.10-----")
a = False
b = False
c = True
print((not a or not b) and not c)
print((not a or not b) and (a or b))
print(a and b or a and c or not c)

print("-----3.11-----")
print("---а---")
x = 1
y = -1
if x ** 2 + y ** 2 <= 4:
    print(True)
else:
    print(False)
print("---б---")
x = 1
y = 2
if x >= 0 or y ** 2 != 4:
    print(True)
else:
    print(False)
print("---в---")
x = 1
y = 2
if x >= 0 and y ** 2 != 4:
    print(True)
else:
    print(False)
print("---г---")
x = 2
y = 1
if x * y != 0 and y > x:
    print(True)
else:
    print(False)
print("---д---")
x = 2
y = 1
if x * y != 0 or y < x:
    print(True)
else:
    print(False)
print("---е---")
x = 2
y = 1
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)
print("---ж---")
x = 1
y = 2
if not x * y < 0 or y > x:
    print(True)
else:
    print(False)

print("-----3.12-----")
print("---а---")
x = 1
y = -1
if x ** 2 - y ** 2 <= 0:
    print(True)
else:
    print(False)
print("---б---")
x = 2
y = -2
if x >= 2 or y ** 2 > 4:
    print(True)
else:
    print(False)
print("---в---")
x = 2
y = 2
if x >= 0 and y ** 2 > 4:
    print(True)
else:
    print(False)
print("---г---")
x = 1
y = 2
if x * y != 4 and y > x:
    print(True)
else:
    print(False)
print("---д---")
x = 2
y = 1
if not x * y != 0 or y < x:
    print(True)
else:
    print(False)
print("---е---")
x = 1
y = 2
if not x * y < 1 and y > x:
    print(True)
else:
    print(False)
print("---ж---")
x = 2
y = 1
if not x * y < 0 or y > x:
    print(True)
else:
    print(False)

print("-----3.13-----")
print("-----TT-----")
a = True
b = True
print(not (a and b))
print(not a or b)
print(a or not b)

print("-----TF-----")
a = True
b = False
print(not (a and b))
print(not a or b)
print(a or not b)

print("-----FF-----")
a = False
b = False
print(not (a and b))
print(not a or b)
print(a or not b)

print("-----FT-----")
a = False
b = True
print(not (a and b))
print(not a or b)
print(a or not b)

print("-----3.14-----")
print("-----TT-----")
x = True
y = True
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----TF-----")
x = True
y = False
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----FF-----")
x = False
y = False
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----FT-----")
x = False
y = True
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----3.15-----")
print("-----TT-----")
a = True
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----TF-----")
a = True
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----FF-----")
a = False
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----FT-----")
a = False
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----3.16-----")
print("-----TT-----")
x = True
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----TF-----")
x = True
y = False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----FF-----")
x = False
y = False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----FT-----")
x = False
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----3.17-----")
print("-----TT-----")
a = True
b = True
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----TF-----")
a = True
b = False
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----FF-----")
a = False
b = False
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----FT-----")
a = False
b = True
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----3.18-----")
print("-----TT-----")
x = True
y = True
print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print("-----TF-----")
x = True
y = False
print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print("-----FF-----")
x = False
y = False
print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print("-----FT-----")
x = False
y = True
print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print("-----3.19-----")
print("-----TT-----")
a = True
b = True
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

print("-----TF-----")
a = True
b = False
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

print("-----FF-----")
a = False
b = False
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

print("-----FT-----")
a = False
b = True
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

print("-----3.20-----")
print("-----TT-----")
x = True
y = True
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

print("-----TF-----")
x = True
y = False
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

print("-----FF-----")
x = False
y = False
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

print("-----FT-----")
x = False
y = True
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

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
x = True
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
x = True
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
x= True
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

print("-----3.27-----")
print("а")
if x > 2 and y > 3:
    print(True)
else:
    print(False)
print("б")
if x > 1 or y > -2:
    print(True)
else:
    print(False)
print("в")
if x >= 0 and y > 5:
    print(True)
else:
    print(False)
print("г")
if x > 3 or y < -1:
    print(True)
else:
    print(False)
print("д")
if x > 3 and y < 10:
    print(True)
else:
    print(False)
print("е")
if not x > 2:
    print(True)
else:
    print(False)
print("ж")
if not x > 2 and x < 5:
    print(True)
else:
    print(False)
print("з")
if 10 < x and x <= 20:
    print(True)
else:
    print(False)
print("и")
if 0 < y <= 4 and x < 5:
    print(True)
else:
    print(False)

print("-----3.28-----")
print("а")
print("б")
print("в")
print("г")
print("д")
print("е")
print("ж")
print("з")
print("и")

print("-----3.29-----")
print("а")
print("б")
print("в")
print("г")
print("д")
print("е")
print("ж")
print("з")
print("и")

print("-----3.30-----")
print("а")
print("б")
print("в")
print("г")
print("д")
print("е")
print("ж")
print("з")
print("и")

print("-----3.31-----")
print("а")
print("б")
print("в")
print("г")
print("д")
print("е")
print("ж")
print("з")
print("и")

