# undmk
# usage: $ python3 ./undmk.py <DMKFILENAME>
# (c)2019 ben ferguson

import os
import sys 

input = sys.argv[1]

try:
    filesize = os.path.getsize(input)
except:
    print('Bad filename, try again.')
    sys.exit()

print('DMK filesize: ' + str(filesize))
if filesize != 1049616:
    print("I don't think this is an MSX DMK! Quitting...")
    sys.exit()

def read_dmk(path):
    with open(path, 'rb') as f:
        return f.read()

inbytes = read_dmk(input)

tracksize = inbytes[1]
print('Num of tracks: ' + str(tracksize))

out=[]
i = 16
while i < len(inbytes):
    if inbytes[i] == 161:
        if inbytes[i+1] == 161:
            if inbytes[i+2] == 161:
                if inbytes[i+3] == 251:
                    # found start of track
                    i = i + 4
                    t = 0
                    while t < 512:
                        out.append(inbytes[i])
                        i += 1
                        t += 1
    i += 1

try:
    ofn = os.path.splitext(input)[0]
    fn = ofn+'.DSK'
    fo = open(fn, 'wb')
    ob = bytes(out)
    fo.write(ob)
    print(fn + ' written successfully.')
except:
    print('Write failed - permissions error?')
finally:
    fo.close()
