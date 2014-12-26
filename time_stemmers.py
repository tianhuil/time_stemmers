from nltk.stem import (WordNetLemmatizer, LancasterStemmer,
  ISRIStemmer, PorterStemmer, SnowballStemmer, RegexpStemmer)
from stemming.porter2 import stem
import re
from functools32 import lru_cache
from time import time

stemmers = [
  ('stem', stem),
  ('WordNetLemmatizer', WordNetLemmatizer().lemmatize),
  ('LancasterStemmer', LancasterStemmer().stem),
  ('ISRIStemmer', ISRIStemmer().stem),
  ('PorterStemmer', PorterStemmer().stem),
  ('SnowballStemmer', SnowballStemmer('english').stem),
  ('RegexpStemmer', RegexpStemmer('ing$|s$|e$|able$', min=4).stem),
  ('re.sub', lambda x: re.compile('ing$|s$|e$|able$').sub('', x)),
]

for name, stem in stemmers:
  print '===', name, '==='
  t=time()
  [stem('france') for _ in xrange(10000)]
  print "  %.4f seconds" % (time()-t)

  lru_stem = lru_cache(maxsize=50)(stem)
  t=time()
  [lru_stem('france') for _ in xrange(10000)]
  print "  %.4f seconds" % (time()-t)
