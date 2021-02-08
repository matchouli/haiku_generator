import xkcdpass.xkcd_password as xp
from haiku_generator.gherasim import GherasimGenerator

# get a XKCD password
mywords = xp.generate_wordlist(min_length=3, max_length=8, wordfile='fr-freelang', valid_chars='[a-z]')
raw_password = xp.generate_xkcdpassword(mywords, numwords=4).split(' ')
print(raw_password)

gherasim_generator = GherasimGenerator()

print(gherasim_generator.generate_gherasim_haiku(raw_password))
print()
