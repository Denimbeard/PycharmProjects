n = int(input('Provide a number: '))
nums = []

for i in range(1, n+1):
    nums.append(i)
print(*nums, sep=", ")
