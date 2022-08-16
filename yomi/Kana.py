class Kana:
    def __init__(self, pinyin, kanji, kana_s):
        self.pinyin = pinyin
        self.kanji = kanji
        self.kana_s = kana_s

    def get_kana(self):
        return self.kanji + " -- " + self.kana_s

    def is_match(self, py):
        if self.pinyin == py:
            return True
        else:
            return False
