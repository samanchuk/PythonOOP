class Words:
    def __init__(self, s=None):
        if s:
            self.words = s.split()
        else:
            self.words = []

    def __str__(self):
        return ' '.join(self.words)

    def __repr__(self):
        ret_str = ''
        for number, word in enumerate(self.words):
            ret_str += '|({0}) {1}'.format(number, word)
        return ret_str + '|'

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        if isinstance(self.words[item], list):
            return Words(' '.join(self.words[item]))
        else:
            return self.words[item]

    def __sub__(self, other):
        return self.words.pop(other)

    def __add__(self, other):
        self.words.append(other)


income_string = 'word word2 word3'

new_str = Words(income_string)

print(repr(new_str))
print(repr(str(new_str)))
print(new_str[0:2])
new_str.__add__('word4')
print(new_str + 'word5')

for i in new_str:
    print(i, end=' ')