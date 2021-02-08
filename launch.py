import xkcdpass.xkcd_password as xp
from haiku_generator.gherasim import GherasimGenerator
from haiku_generator.bert import BertGenerator

# get a XKCD password
mywords = xp.generate_wordlist(min_length=3, max_length=8, wordfile='fr-freelang', valid_chars='[a-z]')
raw_password = xp.generate_xkcdpassword(mywords, numwords=4, delimiter='_')

gherasim_generator = GherasimGenerator()
bert_generator = BertGenerator(bert=True)

print(raw_password)

print('#### Gherasim POEM')
print(gherasim_generator.generate_gherasim_haiku(raw_password))
print()

print('#### BERT POEM')
print(bert_generator.generate_bert_haiku(raw_password))
print()
