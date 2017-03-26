class Pagination:
    def __init__(self, book, chars_limit):
        self.book = book
        self.chars_limit = chars_limit
        self.pages = self.parse()
        self.current_page = 0
        self.bookmark = 0

    def parse(self):
        part_text = []
        first_index = 0
        last_index = 0
        symbols = ['.', '!', '?', '."', '?"', '!"']
        while len(self.book) > first_index:
            part = self.book[first_index:first_index + self.chars_limit]
            for s in symbols:
                index = part.rfind(s)
                if index >= last_index:
                    last_index = index
            last_index += 2
            part_text.append(self.book[first_index:first_index + last_index])
            first_index = first_index + last_index + 1
        return part_text

    def check_if_page_exist(self, page_num):
        return True if 0 <= page_num <= len(self.pages) else False

    def get_page_number(self):
        if self.check_if_page_exist(self.current_page):
            return self.current_page

    def print_page(self):
        if self.check_if_page_exist(self.current_page):
            return self.pages[self.current_page]

    def move_to_page(self, page_num):
        if self.check_if_page_exist(page_num):
            self.current_page = page_num
            return True
        else:
            return False

    def move_back(self):
        if self.check_if_page_exist(self.current_page - 1):
            self.current_page -= 1
            return True
        else:
            return False

    def move_forward(self):
        if self.check_if_page_exist(self.current_page + 1):
            self.current_page += 1
            return True
        else:
            return False

    def move_forward_pages(self, page_amount):
        if self.check_if_page_exist(self.current_page + page_amount):
            self.current_page += page_amount
            return True
        else:
            return False

    def move_back_pages(self, page_amount):
        if self.check_if_page_exist(self.current_page - page_amount):
            self.current_page -= page_amount
            return True
        else:
            return False

    def move_to_first_page(self):
        self.current_page = 0

    def move_to_last_page(self):
        self.current_page = len(self.pages) - 1


text = open('h1.txt', 'r').read()

book = Pagination(text, 1000)

book.move_to_page(5)
#book.move_forward()

print(book.print_page(), '\n Page:', book.get_page_number())
book.move_to_first_page()
print(book.print_page(), '\n Page:', book.get_page_number())
book.move_to_last_page()
print(book.print_page(), '\n Page:', book.get_page_number())
