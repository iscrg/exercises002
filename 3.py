with open('input.txt') as file:
    text = file.read().splitlines()

res = ''

for line in text:
    res += line[-1]

with open('output.txt', 'w+') as file:
    file.write(res)
