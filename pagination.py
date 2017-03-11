paging_text = open('h1.txt', 'r').read()


def parse(text, chars_limit):
        part_text = []
        first_index = 0
        last_index = 0
        symbols = ['.', '!', '?', '."', '?"', '!"']
        while True:
            last_index = 0
            part = text[first_index:first_index + chars_limit]
            for s in symbols:
                index = part.rfind(s)
                if index > last_index:
                    last_index = index
            last_index += 2
            part_text.append(paging_text[first_index:first_index + last_index])
            first_index += last_index
            if len(text) < first_index:
                return part_text

print(parse(paging_text, 10))
