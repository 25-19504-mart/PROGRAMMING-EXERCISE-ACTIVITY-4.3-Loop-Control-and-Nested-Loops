n = int(input("Size: "))

while n < 1 or n > 10:
    n = int(input("Size: "))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(f"{row * col:4}", end="")
    print()