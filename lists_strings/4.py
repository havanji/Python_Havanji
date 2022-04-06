things = ["wallet", "mirror", "umbrella"]

new_things = list(map(str.capitalize, things))
print(new_things)

new_things = list(map(str.upper, things))
print(new_things)

del things[2]
print(things)
