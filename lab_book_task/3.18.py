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
