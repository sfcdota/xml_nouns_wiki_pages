import pymorphy2
import re
import os
import ex2

morph = pymorphy2.MorphAnalyzer()
with open('parsed_text.txt', "r", encoding="utf-8") as inputFile:
    with open('parsed_nouns.txt', "w", encoding="utf-8") as output:
        words = re.findall(r'\w+', inputFile.read().lower())
        output.write(os.linesep.join({p.normal_form for w in words for p in morph.parse(w) if 'NOUN' == p.tag.POS and 'Abbr' not in p.tag and p.score > 0.2}))