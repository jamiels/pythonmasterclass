f = open('hamlet.txt', 'r')
f.seek(10)
substring = f.read(5)

print(substring)
f.seek(0)
substring = f.read(5)
print(substring)
f.close()
