"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

import os
import nltk
import sys
from collections import Counter

if __name__ == '__main__':
    stop_words = set(nltk.stopwords.words('english'))
    if len(sys.argv) > 1:
        if os.path.isfile(file := sys.argv[1]):
            with open(file, encoding='UTF-8') as file_name:
                words = file_name.read().split()
            word_tokens = nltk.word_tokenize(words)
            not_stop_words = []
            for i in word_tokens:
                if i not in stop_words:
                    not_stop_words.append(i)
            sorted_words = str(Counter(not_stop_words).most_common(100))
            print(sorted_words)
        else:
            print('Error: File doesnt exists')
