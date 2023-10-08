with open('input.txt') as file:
    text = file.read().splitlines()

text = list(map(int, text))
text.sort(reverse=True)

with open('output.txt', 'w+') as file:
    for line in text:
        file.write(f'{line}\n')
