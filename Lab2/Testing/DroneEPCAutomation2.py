import subprocess
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("Page1")

# Build some arrays with your desired testing values
droneEPC = [0, 100, -1, 101];

# Excel headers
sh.write(0, 0, "TestID")
sh.write(0, 1, "Desc.")
sh.write(0, 2, "X1")
sh.write(0, 3, "X2")
sh.write(0, 4, "X3")
sh.write(0, 5, "Expected")
sh.write(0, 6, "Actual")

#loop through all combination of EPC values
counter = 1
for x in droneEPC:
    for y in droneEPC:
        for z in droneEPC:
            sh.write(counter, 0, counter)
            sh.write(counter, 1, "EPC case")
            sh.write(counter, 2, x)
            sh.write(counter, 3, y)
            sh.write(counter, 4, z)
            if x < 0 or y < 0 or z < 0:
                sh.write(counter, 5, "ERROR: Invald argument - negative value")
            elif x + y + z > 100:
                sh.write(counter, 5, "Failure!")
            else:
                sh.write(counter, 5, "Success!")
            counter += 1

book.save("DroneEPC.xls")