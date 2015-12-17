# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:35:25 2015

@author: sampathkumarm

purpose:

"""
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

from __future__ import division

import os
import re

year_regex = '(?:(?:19|20)[0-9]{2})'

filename_regex = '([a-zA-Z0-9]+)'

def get_file_extension(filename):
    filename = filename.strip()
    ext = ''
    if '.' in filename:
        ext = filename.split('.')[-1]
        filename = filename.rstrip('.'+ ext)
        return filename, ext
    else:
        return filename, ext

def set_file_extension(filename, ext):
    if ext:
        return '{}.{}'.format(filename, ext)
    else:
        return filename

def fix_filename_startingwith_number(filename):
    "file starting with number"
    search_res = re.search('\d*', filename)
    if search_res:
        number = search_res.group()
        filename = filename.lstrip(number).strip()
        filename = '{} {}'.format(filename, number)
    return filename

filename = r"../../myharddisk/beethovens-9th-symphony-dublin-con.mp3"

def get_cleanfilename(filename):
    new_name = re.findall( filename_regex, filename.lower())
    new_filename = ' '.join(new_name)
    return new_filename
    
def fix_filenames_with_year(filename):
    "puts any year b/w[1900-2099] number present to last"
    
    "also cleans off non-alpha numeric stuff"
    years = re.findall(year_regex, filename)
    for _ in years:
        filename = filename.replace( _, ' ')
    new_name = re.findall( filename_regex, filename)
    new_name = [ _.lower() for _ in new_name if _ and _ not in years ]
    years = '-'.join(years)
    new_name.append(years)    
    new_filename = ' '.join(new_name).strip()
    return new_filename

def get_file_size(filename): 
    size = 0
    try:
        st = os.stat(filename)
        size = st.st_size / ( 1024 * 1024)
    except:
        print "failed to fetch size for ['{}']".format(filename)
    return size

def main(filename):
    # strip extension
    filename, ext = get_file_extension(filename)
    # file starting with year :: reset here
    # file starting with random symbols :: fixed here
    filename = fix_filenames_with_year(filename)
    # file starting with number :: fixed here
    filename = fix_filename_startingwith_number(filename) # last fns
    # add extension
    filename = set_file_extension(filename, ext)
    return filename

def get_normalised_filename(filename):
    return main(filename)
    
def testing():
    assert get_file_extension('12 angry men.avi') == ('12 angry men', 'avi')
    assert fix_filename_startingwith_number('12 angry men') == 'angry men 12'
    assert fix_filenames_with_year('1990 guido adventures') == \
    'guido adventures 1990'
    assert get_cleanfilename(
        '#$%%!@1990#@!#12!@#(angry*&)(#$)men(&*#dual-audio.eng.hin') ==\
        '1990 12 angry men dual audio eng hin'