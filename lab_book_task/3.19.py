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
