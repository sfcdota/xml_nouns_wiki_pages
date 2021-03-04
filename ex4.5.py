import wikipediaapi
import os
import ex3
import re

wiki = wikipediaapi.Wikipedia("ru")
print(wiki.page("рис"))