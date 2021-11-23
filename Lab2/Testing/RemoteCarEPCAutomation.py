import subprocess

# use python 2.7

# Build some arrays with your desired testing values
remoteCarEPC = [-1, 1, -1.1, 1.1];

#loop through all combination of EPC values
for x in remoteCarEPC:
    for y in remoteCarEPC:
        print(x, y)