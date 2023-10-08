with open('input.txt') as file:
    text = file.readlines()

with open('output.txt', 'w+') as file:
    for line in text:
        if line[0] == 'A':
            file.write(line)
