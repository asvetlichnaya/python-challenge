import re
from collections import Counter


def replace_short_forms_in_poem(poem):
    poem = re.sub("aren't", 'are not', poem)
    poem = re.sub("it's", 'it is', poem)
    poem = re.sub("you're", 'you are', poem)
    poem = re.sub("let's", 'lets', poem)
    return poem


def split_poem_into_words(poem):
    return re.split(r'\W+', poem)


def form_vocabulary_list(poem):
    return sorted(list(set(poem)))


def count_words_in_poem(vocabulary, list_of_words):
    x = Counter(list_of_words)
    vocabulary_count = dict()

    for i in x.keys():
        vocabulary_count[i] = x[i]
    return vocabulary_count


zen_of_python = '''aren't it's
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those'''

zen_of_python = zen_of_python.lower()

zen_of_python = replace_short_forms_in_poem(zen_of_python)

poem_words = split_poem_into_words(zen_of_python)

vocabulary_list = form_vocabulary_list(poem_words)
print('Vocabulary is ', vocabulary_list)

print('Count of each word in a poem: ', count_words_in_poem(vocabulary_list, poem_words))