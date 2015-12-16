########################################################################
########## GOAL :: Focus on a single file functionality ###############
#### Filename clean - up task
# file names starting with year is not good
# filename should be only lower-caps 
# un-necesary symbols and charecter are to be cleaned up
# -------------------------- pending
# -------------------------- pending
# file starting with number is not good like 01, 02, 03,..
# folder-names should not be part of filename
# with-in same-folder - if all are having a common name
#
# Cleanup_keywords like - episode, season,.. can be kept as optional
# Allowed_keywords like dvdrip, website, torrent,.. can be removed
# 
# file-properties are to be added 
#       extension-type, size, bit-rate, resolution
#
#
# dependency file :: config.py
########################################################################


import os
import re


def get_normalised_filename(filename):
    "clean-up filename"
    # break this function in to pieces
    # make this funciton in to a class
    year = re.findall('(\d{4})', filename)
    for _ in year:
        filename = filename.replace(_, ' ')
    
    new_name = re.findall('([a-zA-Z0-9]+)', filename)
    
    if '.' in filename:
        file_extension = new_name.pop()

    new_name = [ _.lower() for _ in new_name if _ not in year ]
    
    year = '-'.join(year)
    
    new_name.append(year)
    
    new_filename = ' '.join(new_name).strip()
    
    if '.' in filename:
        new_filename = new_filename + '.' + file_extension

    return new_filename


