occured = set()

for a in range(2,101):
    for b in range(2,101):
        occured.add(a**b)

print(len(occured))
