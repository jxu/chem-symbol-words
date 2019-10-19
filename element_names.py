import re, sys
abbr = list(map(str.strip, open("elements_abbr.txt").readlines()))
regex = re.compile(r"\b(" + '|'.join(abbr) + r")+\b", re.I)
words = [w.strip() for w in open(sys.argv[1]).readlines() if '\'' not in w]
for result in regex.finditer(' '.join(words)):
    print(result.group(0))
