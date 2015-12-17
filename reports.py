# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:35:25 2015

@author: sampathkumarm

purpose : to store reports, requests or completed reports for rollback.
    1. generate a csv report of files 
        a. folder found
        b. file names found
        c. suggested new names
    2. provide user report for manually approval of renames
"""

import os
import csv
import time

reports_dir = 'reports'

def save_filesearch_report(myfiles_search_list)"
    "saves files search report"
    header = [ 'path', 'actual_filename', 'new_suggested_name']
    filename = os.path.join( reports0dir, time.ctime())
    fp = open(filename,'w')
    csv_fp = csv.reader(fp)
    csv_fp.writerow(header)
    csv_fp.writerows(myfiles_search_list)
    fp.flush()
    fp.close()

def read_file_rename_report():
    "read user report and rename-files accorldy"
    pass
