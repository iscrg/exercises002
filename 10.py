with open('input.txt') as file:
    text = file.read().splitlines()

with open('simple/output.txt', 'w+') as file:
    for i in range(1, len(text), 2):
        file.write(f'{text[i]}\n')
