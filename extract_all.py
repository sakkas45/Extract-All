#-*-coding: utf-8-*-
__author__ = 'sakkas45'
import os
import glob
import patoolib

in_folder = '/path/to/archives'  # input folder
out_folder = '/path/to/'  # output folder
os.chdir(in_folder)  # change directory to input folder

types = ['rar', 'tar.gz', 'zip']  # archive types

files = []  # archives
for extension in types:
    files.extend(glob.glob('*.'+extension))

for f in files:
    out_dir = out_folder + f[0:f.index('_')]  # if file name like 'ABC ABC_...rar' , it takes ABC ABC
    if not os.path.exists(out_dir):  # if directory not exist, creates directory
        os.makedirs(out_dir)
    patoolib.extract_archive(f, outdir=out_dir)  # extracts archives to desired directory
