x = int(input())
a = (x % 10) * 100
b = ((x // 10) % 10) * 10
c = (x // 100)
print ((a + b + c) * 2)