from django.db import models


# Create your models here.
'''
class Kana(models.Model):
    pinyin = models.CharField(max_lenght=10)
    kanji = models.CharField(max_lenghth=4)
    kana = models.CharField(max_length=30)

    def get_kana(self):
        return self.kanji + " -- " + self.kana_s

    def is_match(self, py):
        if self.pinyin == py:
            return True
        return False
'''
