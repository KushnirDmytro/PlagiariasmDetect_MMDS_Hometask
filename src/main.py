
import os
from unicodedata import normalize
import re

class document:

    def __init__(self, name='unknown', shingle_set=set()):
        self.name = name
        self.shingles = shingle_set



def read_file(file_name):
    """
    reads file
    :return: string_representation of a file content (all delims replaced woth spaces)
    """
    file_string = ""
    return file_string

def line_shingler(line, k):
    s = set()
    end = k
    while end <= len(line):
        s.add(line[end-k:end])
        end +=1

    return s

def similarity_of_bare_sets(s1, s2):
    return len(s1.intersection(s2)) / len(s1.union(s2))

def minhashing(shingles, k):
    pass



files = os.listdir('../data')
print(files)

shingles_sets_list = []

for file in files:

    f = open( '../data/' + file, 'r', encoding="UTF-8", errors='ignore')

    f_str = f.read()

    f_str = re.sub('[^a-zA-Z0-9 ]', "", f_str)
    f_str = re.sub(" +", " ", f_str).lower()

    shingles = line_shingler(f_str, 7)

    # f_str.replace("\r", " ")
    print()
    print()
    print (file)
    print()
    print(f_str)
    print()

    document_shingled = line_shingler(f_str, 7)

    shingles_sets_list.append(
        document(file, document_shingled )
    )



for indx, doc_1 in enumerate(shingles_sets_list):
    for doc_2 in shingles_sets_list[indx:]:
        if doc_1.name != doc_2.name:
            simialrity = similarity_of_bare_sets (doc_1.shingles, doc_2.shingles)
            if simialrity > 0.5:
                print ( " doc1 [{}]  doc2 [{}] sim [{}]%".format(doc_1.name, doc_2.name, simialrity))

