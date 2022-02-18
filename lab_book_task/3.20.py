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
