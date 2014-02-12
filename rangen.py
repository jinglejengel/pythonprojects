#!/usr/bin/env/python
#
# Generates a list of 500000 random strings of a size specified in the genRandom function

import string
import random

def genRandom(size = 8, gen = string.ascii_letters + string.digits + string.punctuation ):
    return ''.join(random.choice(gen) for x in range(size))

listwords = []
while len(listwords) < 500000:
	listwords.append(genRandom())
