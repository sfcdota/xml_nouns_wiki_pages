import wikipedia
import os
import ex3
import re
import warnings
from urllib.parse import quote

wikipedia.set_lang("ru")
warnings.catch_warnings()
warnings.simplefilter("ignore")
with open('parsed_nouns.txt', "r", encoding="utf-8") as inputFile:
    with open('wiki_links.txt', "w", encoding="utf-8") as output:
        words = re.findall(r'\w+', inputFile.read())
        for w in words:
            output.write("{}: ".format(w))
            links = []
            try:
                output.write("{}{}\n".format(wikipedia.page(w, None, True).url, os.linesep))
            except wikipedia.exceptions.DisambiguationError as e:
                print("Возникла ошибка неоднозначности. Введенное слово = {}{}Список предредложенных заголовков страниц:{}{}".
                      format(w, os.linesep, e.options, os.linesep))
                found = False
                for i in e.options:
                    try:
                        output.write("[НЕОДНОЗНАЧНАЯ, АВТО] {}{}\n".format(wikipedia.page(i, redirect=True).url, os.linesep))
                        found = True
                        break
                    except wikipedia.exceptions.DisambiguationError as e:
                        continue
                if not found:
                    output.write("[НЕОДНОЗНАЧНАЯ, РУЧН] https://ru.wikipedia.org/wiki/{}{}".format(quote(w), os.linesep))