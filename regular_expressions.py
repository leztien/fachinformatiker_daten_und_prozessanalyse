import re


s = "<b><i>fett und kursiv<\i></b>"
match = re.search(r"<.+>", s)   # greedy
print(match.group())
match = re.search(r"<.+?>", s)  # non-greedy
print(match.group())


codons = "AAATGACCC"
match = re.search(r"\A([ACGT]{3})+\Z", codons)
if match: print(match.group())


s = "123.456.789.000"
match = re.search(r"\A(\d{3}\.)*\d{3}\Z", s)
if match: print(match.group())


s = "Guten Tag, Herr Meier!"
s = "Hallo Monika. Wie geht's?"
match = re.match(r"\A(Guten (Morgen|Tag|Abend)|Hi|Hallo),?.*\Z", s)
if match: print(match.group())


reg = re.compile(r'^[\\t\\n ]+[^A-Z]\.\d{2,3}.+\bword\b.*$')
match = reg.match(r"\t \nz.999### word!")
if match: print(match.group())


s = "123@AF"
reg = re.compile(r"\A(\d+)@([A-Z]{2})\Z")
s = reg.sub("\\1 \\2", s)
print(s)


s = "Apples for 1.99, plums for 25.55 each."
reg = re.compile(r"\d+\.\d{2}")
s = reg.sub(lambda match: "€{:.2f}".format(float(match.group()) * 1.5), s)
print(s)


s = "Alles, was nicht Bestandteil eines Wortes, soll raus!!!"
reg = re.compile(r"\W+")
s = reg.sub(' ', s)
print(s)


s = "Alles, was nicht Bestandteil eines Wortes, soll raus!!!"
reg = re.compile(r"\W+")
l = reg.split(s)
print(l)


s = "Wörter (oder wortähnliche Bestandteile) extrahieren."
l = re.findall(r"\w+", s)
l = re.findall(r"\b\w+\b", s)   # same
print(l)
