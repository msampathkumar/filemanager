# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:35:25 2015

@author: sampathkumarm

purpose:

"""

########################################################################
###### GOAL :: Get Extracted, Transformed Data and Present views ######
#
# import numpy
# group by - names
# group by - year
# list of names - need to be cleaned up ### clears same-file issue
#
# save a csv-file of what has happened !!
########################################################################



import os
import re

from get_file_info import get_normalised_filename

from config import allowed_keywords, cleanup_keywords, parent_folders

source = parent_folders[0]


def get_all_files(sources):
    all_files = []
    for source in sources:
        all_files.extend(get_source_files(source))
    return all_files

def get_source_files(source):
    source_files = [(root, file_name)
                    for root, subFolders, files in os.walk(source)
                    for file_name in files
                   ]
    return source_files

def test():
    filename = '1&`~-+=hum#ne$aap+see_pyar|kiya.2015?hindi-eng^dual#audio .mkv'
    print get_normalised_filename(filename)



# find same-files in multiples places
# find files with matching names


all_files = get_all_files(parent_folders)
all_files.sort(key= lambda x:x[-1])
all_only_filenames = [ ( _[1], get_normalised_filename(_[1])) \
     for _ in all_files]



































