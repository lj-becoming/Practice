# pprint.pformat()练习
import pprint

cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
p = pprint.pformat(cats)
print(p)
print(type(p))

fileobj = open("my_cats.py", "w")
fileobj.write("cats = " + p + "\n")
fileobj.close()
