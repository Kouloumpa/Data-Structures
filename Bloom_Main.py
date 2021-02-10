from Bloom import BloomFilter
from random import shuffle

# lexeis pou thelw na prosthesw sto bloom array
word_present = ['ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε',
                'έξι', 'επτά', 'οχτώ', 'εννέα', 'δέκα']

# lexeis pou thelw na elenxw an uparxoun sto bloom array
word_absent = ['έντεκα', 'δώδεκα', 'δεκατρία', 'δεκατέσσερα', 'δεκαπέντε',
               'δεκαέξι', 'δεκαεπτά', 'δεκαοχτώ', 'δεκαεννέα', 'είκοσι']

n = len(word_present)
# pithanotita sfalmatos (false positive) pou thelw na exw 0<p<1
p = 0.05


bloomf = BloomFilter(n, p)
print("Μέγεθος Bloom Array:{}".format(bloomf.size))
print("Πιθανότητα σφάλματος(false positive):{}".format(bloomf.fp_prob))
print("Αριθμός hash συναρτήσεων:{}".format(bloomf.hash_count))

# prosthikh olwn ton lexewn ston bloom array
for item in word_present:
    bloomf.add(item)

# dhmiourgw mia dokimastikh lista lexewn gia na elenxw
test_words = word_present + word_absent
shuffle(test_words)
for word in test_words:
    if bloomf.check(word):
        print("'{}' Πιθανώς υπάρχει".format(word))
    else:
        print("'{}' Σίγουρα δεν υπάρχει".format(word))
