with open('input.txt') as file:
    text = file.read().splitlines()

struct = {
    'title': text[0],
    'h1': text[1],
    'p': text[2:]
}

with open('index.html', 'w+') as file:
    file.write('<!DOCTYPE html>\n')
    file.write('<html>\n')

    file.write('<head>\n')
    file.write(f'<title>{struct["title"]}</title>\n')
    file.write('</head>\n')

    file.write('<body>\n')
    file.write(f'<h1>{struct["h1"]}</h1>\n')
    for line in struct['p']:
        file.write(f'<p>{line}</p>\n')
    file.write('</body>\n')

    file.write('</html>\n')
