#LING123, March 13, 2019: Regular expression examples 

# match a regex, print matching strings
import re
regex = r"[ab]*bab[ab]*"
texts = ("bbbaaab", "babbaaabbb", "abbbbab", "aBAba", "dbabe")
for text in texts:
    match = re.match(regex, text)
    if match:
        print(text)

# search for a regex anywhere in a string
import re
regex = r"[ab]*bab[ab]*"
texts = ("bbbaaab", "babbaaabbb", "abbbbab", "aBAba", "dbabe")
for text in texts:
    match = re.search(regex, text)
    if match:
        print(text)

# add flag to ignore case
import re
regex = r"[ab]*bab[ab]*"
texts = ("bbbaaab", "babbaaabbb", "abbbbab", "aBAba", "dbabe")
for text in texts:
    match = re.search(regex, text, re.I)
    if match:
        print(text)

# find all matching substrings in a string
import re
text = "June 24, August 9 and December 12, 2019"
regex = r"\w+ \d+"
matches = re.findall(regex, text)
for match in matches:
    print(match)

# remove tags (underscore followed by non-blank)
import re
text = "many_AP industry_NN trade_NN associations_NNS are_BER developing_VBG campaigns_NNS to_TO protect_VB or_CC enhance_VB the_AT share_NN of_IN the_AT consumer's_NN$ dollar_NN being_BEG spent_VBN on_IN their_PP$ particular_JJ products_NNS ._."
regex = r"_\S+"
print(re.sub(regex, r"", text))

# specify groups in a regex, resulting in a tuple
import re
text = "June 24, August 9 and December 12, 2019"
regex = r"([a-zA-Z]+) (\d+)"
matches = re.findall(regex, text)
for match in matches:
    print(match)
    print(match[1], match[0])

# substitute parts of a string using regex groups
import re
text = "June 24, August 9 and December 12, 2019"
regex = r"([a-zA-Z]+) (\d+)"
print(re.sub(regex, r"\2th of \1", text))
# Exercise: write additional substitutions that also produce "1st" and "2nd"
