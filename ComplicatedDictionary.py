
name = "Macbeth.txt"
handle = open(name)

"""
name = "By the pricking of my thumbs, something wicked this way comes."
handle = name
"""

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)