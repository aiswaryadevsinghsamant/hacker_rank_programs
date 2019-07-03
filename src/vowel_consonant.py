class VowelConsonant:
    def __init__(self, new_str):
        self.new_string = new_str

    def filter_vowel(self):
        s = filter(lambda a: True if a not in ['a', 'e', 'i', 'o', 'u'] else False, self.new_string)
        return ''.join(s)

    def filter_consonant(self):
        s = filter(lambda b: True if b in ['a', 'e', 'i', 'o', 'u'] else False, self.new_string)
        return ''.join(s)


# line = VowelConsonant("hjklnmaepjiou")
var = VowelConsonant("HackerRank")
# print(line.filter_vowel())
# print(line.filter_consonant()) 
print(var.filter_vowel())
print(var.filter_consonant())
