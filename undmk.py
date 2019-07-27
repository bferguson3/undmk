# undmk

# usage: $ python3 ./undmk.py <DMKFILENAME>

# v2: added ability to split and stitch files.
# SPLIT:
#  $ python3 ./undmk.py <DMKFILENAME> -split
# STITCH:
#  $ python3 ./undmk.py <SPLITFOLDERNAME> -stitch

# (c)2019 ben ferguson

import os
import sys 
import math 

input = sys.argv[1]

mode = 'normal'
i = 2
while i < len(sys.argv):
    if sys.argv[i] == '-stitch':
        mode = 'stitch'
    if sys.argv[i] == '-split':
        mode = 'split'
    i += 1


def read_dmk(path):
    with open(path, 'rb') as f:
        return f.read()
#

def normal_undmk(input, split=False):

    try:
        filesize = os.path.getsize(input)
    except:
        print('Bad filename, try again.')
        sys.exit()

    print('DMK filesize: ' + str(filesize))
    if filesize != 1049616:
        print("I don't think this is an MSX DMK! Quitting...")
        sys.exit()

    inbytes = read_dmk(input)

    tracksize = inbytes[1]
    print('Num of tracks: ' + str(tracksize))

    if split == False:
        write_one_file(inbytes, input)
    else:
        write_split_file(inbytes, input)
#

def write_split_file(inbytes, input):
    out = []
    i = 16
    while i < len(inbytes):
        if inbytes[i] == 161:
            if inbytes[i+1] == 161:
                if inbytes[i+2] == 161:
                    if inbytes[i+3] == 251:
                        # found start of track
                        tr = [] 
                        i = i + 4
                        t = 0
                        while t < 512:
                            tr.append(inbytes[i])
                            i += 1
                            t += 1
                        out.append(tr)
        i += 1
    ofn = os.path.splitext(input)[0]
    try:
        os.mkdir(ofn)
    except:
        print('directory already exists. continuing..')
    i = 0 
    while i < len(out)/18:
        j = 0
        fn = ofn+'_' + str(i) + 'A'+ '.BIN'
        fo = open(ofn+'/'+fn, 'wb')    
        while j < 9:
            ob = bytes(out[(i*18)+j])
            fo.write(ob)
            j += 1
        fo.close() 
        fn = ofn+'_' + str(i) + 'B'+ '.BIN'
        fo = open(ofn+'/'+fn, 'wb')    
        while j < 18:
            ob = bytes(out[(i*18)+j])
            fo.write(ob)
            j += 1
        fo.close() 

        i += 1
    print(ofn + ' files written successfully.')

def write_one_file(inbytes, input):

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

#

if mode == 'normal':
    normal_undmk(input)

if mode == 'split':
    normal_undmk(input, True)

if mode =='stitch':
    #print('ok')
    filelist = []
    if os.path.exists(input):
        #print(os.path)
        for r, d, f in os.walk(input):
            for c in f:
                filelist.append(input + '/' + str(c))
            out = []
            i = 0
            while i < 80:
                for c in filelist:
                    if c == input + '/' + input + '_' + str(i) + 'A' + '.BIN':
                        f = open(input + '/' + input + '_' + str(i) + 'A' + '.BIN', 'rb')
                        inb = f.read()
                        f.close()
                        out.append(inb)
                for c in filelist:
                    if c == input + '/' + input + '_' + str(i) + 'B' + '.BIN':
                        f = open(input + '/' + input + '_' + str(i) + 'B' + '.BIN', 'rb')
                        inb = f.read()
                        f.close()
                        out.append(inb)
                i += 1
        #ofn = os.path.splitext(input)[0]
        fn = input +'.DSK'
        fo = open(fn, 'wb')
        #ob = bytes(out)
        for c in out:
            fo.write(c)
        print(fn + ' written successfully.')
        fo.close()
    else:
        print('directory does not exist.')
        sys.exit()