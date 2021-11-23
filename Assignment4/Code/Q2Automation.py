import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("Page1")
empty = "N/A"

line = 1
counter = 1
A = [0, 1, 2, 3, 4]
B = ["A", "B", "C", "D", "E"]
C = [100, 200, 300]
D = [7, 8, 9, 10, 11]
E = ["Y", "N"]
F = ["\\alpha", "\\beta", "\\gamma"]

# Excel headers
sh.write(0, 0, "Test ID")
sh.write(0, 1, "A")
sh.write(0, 2, "B")
sh.write(0, 3, "C")
sh.write(0, 4, "D")
sh.write(0, 5, "E")
sh.write(0, 6, "F")

def write(a, b, c, d, e, f):
    global line, counter
    sh.write(line, 0, counter)
    sh.write(line, 1, a)
    sh.write(line, 2, b)
    sh.write(line, 3, c)
    sh.write(line, 4, d)
    sh.write(line, 5, e)
    sh.write(line, 6, f)
    line += 1
    counter += 1

def empty_row():
    global line
    line += 1

# X
for a in A:
    for d in D:
        for e in E:
            write(a, empty, empty, d, e, empty)

# Y
empty_row()
for b in B:
    write(empty, b, empty, empty, empty, empty)

# Z
empty_row()
for c in C:
    for f in F:
        write(empty, empty, c, empty, empty, f)

book.save("Q2Cases.xls")
