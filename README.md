time_stemmers
=============

A simple script to time python's stemmers.

**TL;DR:**

1. WordNet lemmatizer with lru_cache is the fastest 'professional' stemmer (0.02 secs / 10K)
2. RegexpStemmer *without* lru_cache is the fastest stemmer but a little troublesome (0.01 secs / 10K)

**Results:**

Here are the reuslts

```
=== stem ===
  0.2942 seconds
  0.0199 seconds
=== WordNetLemmatizer ===
  0.0524 seconds
  0.0200 seconds
=== LancasterStemmer ===
  0.4231 seconds
  0.0203 seconds
=== ISRIStemmer ===
  0.4583 seconds
  0.0201 seconds
=== PorterStemmer ===
  0.1943 seconds
  0.0201 seconds
=== SnowballStemmer ===
  0.1691 seconds
  0.0205 seconds
=== RegexpStemmer ===
  0.0102 seconds
  0.0274 seconds
=== re.split ===
  0.0173 seconds
  0.0201 seconds
```