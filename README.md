Extract-All
===========
This script extracts all data to desired directory.

If archive names and their contents are bad named, script creates folders for each archives and seperate their datas.

In my case('ABC ABC_...rar'), I used name and surname('ABC ABC').


Note: Patool is required. You can install terminal via ```pip install patool``` or you can get check from https://github.com/wummel/patool.

```python
#-*-coding: utf-8-*-
__author__ = 'sakkas45'
import os
import glob
import patoolib

in_folder = '/path/to/archives' # input folder
out_folder = '/path/to/' # output folder
os.chdir(in_folder) # change directory to input folder

types = ['rar', 'tar.gz', 'zip'] # archive types

files = [] # archives
for extension in types:
    files.extend(glob.glob('*.'+extension))

for f in files:
    out_dir = out_folder + f[0:f.index('_')] # if file name like 'ABC ABC_...rar' , it takes ABC ABC
    if not os.path.exists(out_dir): # if directory not exist, creates directory
        os.makedirs(out_dir)
    patoolib.extract_archive(f, outdir=out_dir) # extracts archives to desired directory
```
