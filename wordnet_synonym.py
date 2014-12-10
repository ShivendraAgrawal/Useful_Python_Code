__author__ = 'ags7kor'

from pattern.en import tag as tagEN
from collections import defaultdict, Counter
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from pprint import pprint
from Util import Utility
from nltk import stem
import os,csv,xlrd,operator,pickle,ast,pickle,nltk
import timing
from itertools import chain
from nltk.corpus import wordnet as wn

def similar_to(word):
    for ss in wn.synsets(word):
        print(ss)
        for sim in ss.similar_tos():
            print('    {}'.format(sim))

def hyper_hypo(word):
    for i,j in enumerate(wn.synsets(word)):
        print "Meaning",i, "NLTK ID:", j.name()
        print j.lemma_names() + [l.name().split(".")[0] for l in j.similar_tos()]
        print
        # print [l.name().split(".")[0] for l in j.similar_tos()]
        # print "Hypernyms:",  [l.lemma_names() for l in j.hypernyms()]
        # print ", ".join(list(chain(*[l.lemma_names() for l in j.hypernyms()])))
        # print "Hyponyms:", [l.lemma_names() for l in j.hyponyms()]


if __name__ == '__main__':

    # similar_to('small')
    #
    # print "========================================================="

    hyper_hypo('small')