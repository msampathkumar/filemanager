########################################################################
########## GOAL :: store all configuration details here ################
#
#
# -------------------------- pending
# -------------------------- pending
# check if 'cleanup_keywords' & 'allowed_keywords' are exclusive
# check if provided parent folders exist
########################################################################

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