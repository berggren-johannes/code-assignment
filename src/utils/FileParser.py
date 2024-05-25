class FileParser:
    def __init__(self, text):
        self.text = text
        self.prefix = "foo"
        self.suffix = "bar"

    def get_raw(self):
        return self.text
    
    def get_parsed(self):
        return self.text.split()
    
    def get_most_common_word(self):
        words = self.get_raw()
        words = words.split()

        if len(words) == 0:
            raise ValueError("No words found")

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

        print(word_count)

        if len(word_count) > 1:
            multiple_words = [(word_count.keys())[0]]
            word_keys = (word_count.keys())

            for i in range(1, len(word_keys)):
                if word_count[word_keys[i]] == word_count[word_keys[i - 1]]:
                    multiple_words.append(word_keys[i])
                else:
                    break
            return multiple_words
                
        most_common_word = [list(word_count.keys())[0]]

        return most_common_word
    
    def sandwich_word(self, word):
        return f"{self.prefix}{word}{self.suffix}"