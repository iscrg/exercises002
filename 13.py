import string

with open('input.txt') as file:
    text = file.read()

text = text.split()
res = {}

for word in text:
    if word in res:
        res[word] += 1
    else:
        res[word] = 1

with open('output.txt', 'w+') as file:
    for word in res:
        file.write(f'{word}: {res[word]}\n')
