import subprocess

# use python 2.7

# Build some arrays with your desired testing values
droneEPC = [0, 100, -1, 101];

#loop through all combination of EPC values
for x in droneEPC:
    for y in droneEPC:
        for z in droneEPC:
            print(x, y, z)