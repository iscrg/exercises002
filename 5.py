def readfile():
    fn = input('Type in the filename: ')

    try:
        with open(file=fn) as file:
            text = file.read().splitlines()
            return text
    except FileNotFoundError:
        print('File not found!')
        return readfile()


try:
    text = readfile()

    num = int(input('Type in the number of line: '))
    print(text[num - 1])
except IndexError:
    print('Line not found!')
