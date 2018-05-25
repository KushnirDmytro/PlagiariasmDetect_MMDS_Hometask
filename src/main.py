
import os
from unicodedata import normalize
import re
import random



def string_to_number (str):
    # genearating unique number for input string
    return sum( [ (ord(ch) - ord(' ')) * 40^k for k,ch in enumerate(str)] )


SHINGLE_SIZE = 7
random.seed(42)
MAX_NUMBER = string_to_number('z' * SHINGLE_SIZE)
NUMBER_OF_HASH_FUNCTIONS = 100

class document:

    def __init__(self, name='unknown', shingle_set=set()):
        self.name = name
        self.shingles = shingle_set
        self.signatures_list = []



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

def jaccard_sim_of_sets(s1, s2):
    return len(s1.intersection(s2)) / len(s1.union(s2))

def minhashing(shingles, k):
    pass



files = os.listdir('../data')
print(files)

docs_list = []

for file in files:

    #TODO move to read-file function
    f = open( '../data/' + file, 'r', encoding="UTF-8", errors='ignore')

    f_str = f.read()

    f_str = re.sub('[^a-zA-Z0-9 ]', "", f_str)
    f_str = re.sub(" +", " ", f_str).lower()

    shingles = line_shingler(f_str, SHINGLE_SIZE)

    # f_str.replace("\r", " ")
    print()
    print()
    print (file)
    print()
    print(f_str)
    print()

    document_shingled = line_shingler(f_str, 7)

    docs_list.append(
        document(file, document_shingled )
    )


docs_list = sorted(docs_list, key=lambda doc: doc.name)


for indx, doc_1 in enumerate(docs_list):
    for doc_2 in docs_list[indx:]:
        if doc_1.name != doc_2.name:
            simialrity = jaccard_sim_of_sets (doc_1.shingles, doc_2.shingles)
            if simialrity > 0.5:
                print ( " doc1 [{}]  doc2 [{}] sim [{}]%".format(doc_1.name, doc_2.name, simialrity))


# now need to transform to signatures and chech them





def get_random_hashes(max_number):
    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    c = random.randint(1, max_number)
    return lambda x: x*x*a + x*b + c % (max_number+1) #avoiding possible colisions


hash_F_list = []


for _ in range(NUMBER_OF_HASH_FUNCTIONS):
    hash_F_list.append(get_random_hashes(MAX_NUMBER))






def shingles_to_signatures(docs_set, number_of_signatures):
    # as this task is not about primes and to save computing power : https://www.bigprimes.net/archive/prime/10001/
    # list_of_primes = [
    #     15485867, 15486277, 15486727, 15487039,
    #     15485917, 15486281, 15486739, 15487049,
    #     15485927, 15486283, 15486749, 15487061,
    #     15485933, 15486287, 15486769, 15487067,
    #     15485941, 15486347, 15486773, 15487097,
    #     15485959, 15486421, 15486781, 15487103,
    #     15485989, 15486433, 15486791, 15487139,
    #     15485993, 15486437, 15486803, 15487151,
    #     15486013, 15486451, 15486827, 15487177,
    #     15486041, 15486469, 15486833, 15487237,
    #     15486047, 15486481, 15486857, 15487243,
    #     15486059, 15486487, 15486869, 15487249,
    #     15486071, 15486491, 15486871, 15487253,
    #     15486101, 15486511, 15486883, 15487271,
    #     15486139, 15486517, 15486893, 15487291,
    #     15486157, 15486533, 15486907, 15487309,
    #     15486173, 15486557, 15486917, 15487313,
    #     15486181, 15486571, 15486929, 15487319,
    #     15486193, 15486589, 15486931, 15487331,
    #     15486209, 15486649, 15486953, 15487361,
    #     15486221, 15486671, 15486967, 15487399,
    #     15486227, 15486673, 15486997, 15487403,
    #     15486241, 15486703, 15487001, 15487429,
    #     15486257, 15486707, 15487007, 15487457,
    #     15486259, 15486719, 15487019, 15487469]

    """
    :param shingles_set: set of shingles (substrings of length k from initial data)
    hash_fn is replaced by ordinary primes to avoid collisions at all (except of extreme size sets cases)
    :return: set of similar size to initial but with numbers (signatures) instead of strings
    """


    for sh in docs_set:
        for shingle in sh.shingles:
            number = string_to_number(shingle)
            new_signature = MAX_NUMBER + 2
            for hash_F in hash_F_list:
                new_signature = min (new_signature,  hash_F(number))
            sh.signatures_list.append(new_signature)

shingles_to_signatures(docs_list, 5)

for d in docs_list:
    print (d.name)
    print (len(d.shingles))
    print (len(d.signatures_list))
    print(d.signatures_list)