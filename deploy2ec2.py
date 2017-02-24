#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.project import rsync_project

__author__ = 'BuGoNee'

'''
Some Explaination should be in here.
'''

env.key_filename=['/home/lu/aws/nadileaf-spiders.pem']
env.hosts = [
    'ec2-user@54.223.80.254',
            ]

def update_setting_remote():
    print "remote update"
    with cd('~/MBTI'):   #cd用于进入某个目录
        run('ls -l | wc -l')  #远程操作用run
        #run('ls -l ')  #远程操作用run
def deploy2ec2():
    remote_dir = '~/'
    loc = '~/nadileaf/MBTI'
    exclude = ['ff','.git']
    rsync_project(local_dir=loc, remote_dir=remote_dir, exclude=exclude)
#deploy2ec2()
