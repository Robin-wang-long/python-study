import re

text = 'alp.bate...gamma delta'
print(re.split('[\. ]+',text))
print(re.split('[\. ]+',text,maxsplit=2))
pat = '[a-zA-Z]+'
print(re.findall(pat,text))
pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat,'Mr.Dong',text))
s = 'a s d'
print(re.sub('a|s|d','good',s))
s = "It's a very good good idea"
print(re.sub(r'(\b\w+) \1',r'\1',s))
