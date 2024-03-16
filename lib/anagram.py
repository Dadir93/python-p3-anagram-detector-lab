class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        anagrams = []
        sorted_word = sorted(self.word.lower()) 
        for word in words_list:
            if word.lower() != self.word.lower() and sorted(word.lower()) == sorted_word:
                anagrams.append(word)
        return anagrams
