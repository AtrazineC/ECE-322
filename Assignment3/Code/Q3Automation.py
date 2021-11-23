import subprocess
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("Page1")

# Build some arrays with your desired testing values
counter = 1
x = [9, 8, 1, 0]
y = [7, 6, -1, -2]
z = [7, 6, 0, -1]

# Excel headers
sh.write(0, 0, "TestID")
sh.write(0, 1, "Desc.")
sh.write(0, 2, "x")
sh.write(0, 3, "y")
sh.write(0, 4, "z")
sh.write(0, 5, "Expected")

#checker function
def check(a, b, c):
    return (a+b>=0) and (b<6) and (a-b-2<=0) and (a>1) and (c>0) and (c<6)

def run_check_and_write(a, b, c, message):
    global counter
    sh.write(counter, 0, counter)
    sh.write(counter, 1, message)
    sh.write(counter, 2, a)
    sh.write(counter, 3, b)
    sh.write(counter, 4, c)
    if check(a, b, c):
        sh.write(counter, 5, "In domain")
    else:
        sh.write(counter, 5, "Out of domain")
    counter += 1

# valid case
valid_a = 3
valid_b = 3
valid_c = 3

run_check_and_write(valid_a, valid_b, valid_c, "Valid case")

#loop through all combination of EPC values
for a in x:
    for b in y:
        for c in z:
            run_check_and_write(a, b, c, "EPC case")

book.save("Q3EPC.xls")