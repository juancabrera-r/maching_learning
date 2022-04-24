from greets import grettings
from translate import Translator

translator = Translator(to_lang='pt')

for g in grettings:
    print(translator.translate(g).title())