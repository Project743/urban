class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        replace_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = file.read().lower().lower()
                for i in replace_list:
                    text = text.replace(i, '')
                all_words[name] = text.split()
        return all_words

    def find(self, word):
        find_word = {}

        for k, v in self.get_all_words().items():
            if word.lower() in v:
                find_word[k] = v.index(word.lower()) + 1
        return find_word

    def count(self, word):
        count_word = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                count_word[k] = v.count(word.lower())
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
