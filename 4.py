fn = input('Type in the filename: ')
num = int(input('Type in the number of line: '))

try:
    with open(file=fn) as file:
        text = file.read().splitlines()
        print(text[num - 1])
except FileNotFoundError:
    print('File not found!')
except IndexError:
    print('Line not found!')
