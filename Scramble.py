import json
import os, sys

def load_words():
    try:
        filename = "/Users/NeeruRohilla/Desktop/python/words_dictionary.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)



def permute(a, l, r):
    if l==r:
        #print toString(a)
        #print(english_words)
        if(toString(a) in english_words):
            print(toString(a))
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

def toString(List):
    return ''.join(List)

if __name__ == '__main__':
    english_words = load_words()
    # demo print

string = "new"
n = len(string)
a = list(string)
permute(a, 0, n-1)
print(type(english_words))
#print(english_words["wander"])
print('new' in english_words)
#123456 123 
def combination(hexWord,mandatoryChar):
    for
