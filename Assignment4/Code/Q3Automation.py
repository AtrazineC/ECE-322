from allpairspy import AllPairs
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("Page1")
empty = "N/A"

parameters = [
    ["NO", "NDEF", "YES"],
    ["NO", "NDEF", "YES"],
    ["12KEY", "NOKEYS", "QWERTY", "NDEF"],
    ["NO", "NDEF", "YES"],
    ["DPAD", "NONAV", "TRKBALL", "NDEF", "WHEEL"],
    ["LAND", "PORT", "SQR", "NDEF"],
    ["MASK", "NO", "NDEF", "YES"],
    ["LRG", "MASK", "NORM", "SML", "NDEF"],
    ["FNGR", "NTOUCH", "STYLUS", "NDEF"],
]

# Excel headers
sh.write(0, 0, "Case")
sh.write(0, 1, "HKBH")
sh.write(0, 2, "KBH")
sh.write(0, 3, "KB")
sh.write(0, 4, "NVH")
sh.write(0, 5, "NV")
sh.write(0, 6, "OR")
sh.write(0, 7, "SLL")
sh.write(0, 8, "SLS")
sh.write(0, 9, "TS")

def write(line, a, b, c, d, e, f, g, h, i):
    sh.write(line + 1, 0, line + 1)
    sh.write(line + 1, 1, a)
    sh.write(line + 1, 2, b)
    sh.write(line + 1, 3, c)
    sh.write(line + 1, 4, d)
    sh.write(line + 1, 5, e)
    sh.write(line + 1, 6, f)
    sh.write(line + 1, 7, g)
    sh.write(line + 1, 8, h)
    sh.write(line + 1, 9, i)

for i, pairs in enumerate(AllPairs(parameters)):
    write(i, pairs[0], pairs[1], pairs[2], pairs[3], pairs[4], pairs[5], pairs[6], pairs[7], pairs[8])

book.save("Q3Cases.xls")
