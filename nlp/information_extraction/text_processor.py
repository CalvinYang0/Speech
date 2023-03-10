class TextProcessor:
    def __init__(self):
        pass

    def information_extraction(self, text):
        pass

    @staticmethod
    def find_keyword_in_list(sentence, keyword_list):
        for word in sentence:
            if word in keyword_list:
                return word
        return None
