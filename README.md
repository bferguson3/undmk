# undmk
MSX DMK to DSK converter script

# UNDMK v2.0
<br>
Update history:<br>
2.0 - added ability to split and stitch files by track and side.

## Binary download for Win/Linux<br>
[Download link](http://barelyconsciousgames.com/undmk_10.zip)

## Usage

Command line, convert .DMK to .DSK:<br>
Executable:*<br>
`undmk <DMKFILENAME>.DMK`<br>
Python:<br>
`$ python3 ./undmk.py <DMKFILENAME>.DMK`<br>

*Windows also supports dragging-and-dropping DMK files onto the .exe.*
<br>
Split .DMK into 160xBIN files (two sides, 80 tracks):<br>
`undmk <DMKFILENAME>.DMK -split`<br>
Join split .BIN files in a folder back to DSK:<br>
`undmk <DMKFOLDERNAME> -stitch`<br>


## Output
Normal:<br>
Creates `<DMKFILENAME>.DSK` in the folder it was ran from.<br>
Split:<br>
Creates 160xBIN files in a folder named as the .DMK file given as input.<br>
Stitch:<br>
Creates a .DSK file in the folder it was ran from with files taken from the folder name given as input.<br>


## Notes

Will work for any 512-byte sector length, 720kb capacity disk with "A1 A1 A1 FB" track data headers.<br>
-Line 36 can be changed to `if inbytes[i+3] == 248:` to support A1...F8 track data header.<br>
-Lines 17-19 can be commented out to ignore filesize. <br>
-Line 40, `while t < 512:`, can be adjusted for whatever desired data track sector length. 

(c) 2019 Ben Ferguson
