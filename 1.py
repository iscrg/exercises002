with open('input.txt') as file:
    text = file.read()

text = text.upper()

with open('output.txt', 'w+') as file:
    file.write(text)