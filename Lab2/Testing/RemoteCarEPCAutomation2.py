import subprocess
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("Page1")

# Build some arrays with your desired testing values
remoteCarEPC = [-1, 1, -1.1, 1.1];

# Excel headers
sh.write(0, 0, "TestID")
sh.write(0, 1, "Desc.")
sh.write(0, 2, "x")
sh.write(0, 3, "y")
sh.write(0, 4, "Expected")
sh.write(0, 5, "Actual")

#loop through all combination of EPC values
counter = 1
for x in remoteCarEPC:
    for y in remoteCarEPC:
        sh.write(counter, 0, counter)
        sh.write(counter, 1, "EPC case")
        sh.write(counter, 2, x)
        sh.write(counter, 3, y)
        if (x*x + y*y > 1):
            sh.write(counter, 4, "Out of range!")
        else:
            sh.write(counter, 4, "Ok.")
        counter += 1

book.save("RemoteCarEPC.xls")