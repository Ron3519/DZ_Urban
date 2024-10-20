class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = ''
                for line in file:
                    if line == '':
                        break
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        line = line.replace(i, ' ')
                    words += line
                all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        word = word.lower()
        file = self.get_all_words()
        result = {}
        for name, words in file.items():
                result[name] = file[name].index(word)


        return result
    def count(self, word):
        word = word.lower()
        result = {}
        file = self.get_all_words()
        i = 0
        for name, words in file.items():
            for j in file[name]:
                if word == j:
                    i += 1
                    result[name] = i
        return result






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

