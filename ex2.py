import xml.etree.ElementTree as eT
text = "".join(eT.parse('kek2.xml').getroot().itertext())
with open('parsed_text.txt', "w", encoding="utf-8") as file:
    file.write(text)
