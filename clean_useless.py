#!/user/bin/python
# -*- coding: utf-8 -*-
# Filename: cleanpyc.py
# Date:2011-03-26

'''
    遍历当前目录,并清理无用文件.
'''

import os
import fnmatch
import sys

'''定义需要清理的文件类型'''
PATTERNS = ['*.pyc','*.py~','*.*~']

def clearpyc(root, patterns=[],single_level=False, yield_folders=False):
    """
    root: 需要遍历的目录
    patterns： 需要查找的文件
    single_level: 是否只遍历单层目录，默认为否
    yield_folders: 是否包含目录本身，默认为否
    """
    S = []
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
            files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern.strip()):# 去除pattern两端的空格
                    S.append(os.path.join(path, name))
        if single_level:
            break
    return set(S)

def run():
    if 2 == len(sys.argv):
        print os.path.join(os.getcwd(), sys.argv[1])
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
    print directory

    for path in clearpyc(directory,PATTERNS):
        print path
        os.remove(path)
if __name__ == '__main__':
    run()
