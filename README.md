# undmk
MSX DMK to DSK converter script

# UNDMK v1.0


## Usage:

Command line:<br>
`undmk <DMKFILENAME>.DMK`

Windows also supports dragging-and-dropping DMK files.


## Output:

`<DMKFILENAME>.DSK`


## Notes:

Will work for any 512-byte sector length, 720kb capacity disk with "A1 A1 A1 FB" track data headers.<br>
-Line 36 can be changed to `if inbytes[i+3] == 248:` to support A1...F8 track data header.<br>
-Lines 17-19 can be commented out to ignore filesize. <br>
-Line 40, `while t < 512:`, can be adjusted for whatever desired data track sector length. 

(c) 2019 Ben Ferguson
