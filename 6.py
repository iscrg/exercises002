def readfile():
    fn = input('Type in the filename: ')

    try:
        with open(file=fn) as file:
            text = file.read().splitlines()
            return text
    except FileNotFoundError:
        print('File not found!')
        return readfile()


def printline(text):
    num = int(input('Type in the number of line: '))

    try:
        print(text[num - 1])
    except IndexError:
        print('Line not found!')
        return printline(text)


printline(readfile())
