from allpairspy import AllPairs

parameters = [
    ["NO", "NDEF", "YES"],
    ["NO", "NDEF", "YES"],
    ["12KEY", "NOKEYS", "QWERTY", "NDEF"],
    ["NO", "NDEF", "YES"],
    ["LAND", "PORT", "SQR", "NDEF"],
    ["MASK", "NO", "NDEF", "YES"],
    ["LRG", "MASK", "NORM", "SML", "NDEF"],
    ["FNGR", "NTOUCH", "STYLUS", "NDEF"],
]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))