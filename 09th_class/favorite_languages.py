
# 有序字典
from collections import OrderedDict


favortive_languages = OrderedDict()

favortive_languages['pingping'] = 'C++'
favortive_languages['yaya'] = 'Java'
favortive_languages['lihong'] = 'Python'

for name, language in favortive_languages.items():
    print(name.title() + "'s favortive language is " + language)