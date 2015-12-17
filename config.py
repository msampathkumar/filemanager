# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:35:25 2015

@author: sampathkumarm

purpose: save core configuration details for app

"""

import os

parent_folders = [
    '../../myharddisk/',
    ]

cleanup_keywords = []

allowed_keywords = []

def check_parent_folders():
    for _ in parent_folders:
        if not os.path.isdir(_):
            print 'InputError : Parent Folder[{}] is not a directory'.format(_)
            break

if __name__ == '__main__':
    check_parent_folders()