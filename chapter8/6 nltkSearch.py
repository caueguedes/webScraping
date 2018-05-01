from nltk.book import *
from nltk import ngrams


fourgrams =  ngrams(text6, 4)
for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)


# from nltk.book import *
# from nltk import FreqDist
# from nltk import ngrams
#
#
# fourgrams = ngrams(text6, 4)
# fourgramsDist = FreqDist(fourgrams)
# fourgramsDist[("father", "smelt", "of", "elderberries")]
# print(fourgramsDist[("father", "smelt", "of", "elderberries")])

# from nltk.book import text6
# from nltk import FreqDist
# from nltk import bigrams
#
#
# bigrams = bigrams(text6)
# bigramDist = FreqDist(bigrams)
# bigramDist[("Sir", "Robin")]
# print(bigramDist[("Sir", "Robin")])

# from nltk.book import *
# from nltk import FreqDist
#
# fdist = FreqDist(text6)
# print(fdist.most_common(10))


