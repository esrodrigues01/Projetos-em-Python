from translate import Translator

s = Translator(from_lang = "english", to_lang = "pt-br")

res = s.translate ("Hello World")


print (res)