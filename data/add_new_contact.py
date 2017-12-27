# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 7), lastname=random_string("lastname", 10))
    for i in range(5)
]