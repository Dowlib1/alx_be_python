n = 10
while True:
    n += 1
    if n % 3 == 0:
        continue
    if n >= 20:
        break
    print(n, end=" ")
print()
for i in range(5, -4, -2):
    print(i, end=' ')
 