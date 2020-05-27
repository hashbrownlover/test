import itertools

def hammingDistance(first, second):
    result = 0
    for i in range(len(first)):
        if (first[i] != second[i]):
            result += 1
    return result

def allPossibleKmers(pattern, d):
    x = itertools.product("ACTG", repeat = k)
    kmers = ["".join(p) for p in x]

    result = {}
    for kmer in kmers:
        result[kmer] = 0

    return result

# naive implementation of generating all kmers
def frequentWordsWithMismatches(text, k, d):
    allKmers = allPossibleKmers(text, k)

    for i in range(len(text) - k):
        pattern = text[i:i+k]
        for kmer in allKmers:
            if (hammingDistance(pattern, kmer) <= d):
                allKmers[kmer] += 1

    maxCount = max(allKmers.values())

    result = []
    for key, value in allKmers.items():
        if (value == maxCount):
            result.append(key)

    return result

with open("rosalind_ba1i.txt") as f:
    text = f.readline().strip()
    numbers = f.readline().split()
    k = int(numbers[0])
    d = int(numbers[1])

print(frequentWordsWithMismatches(text, k, d))
