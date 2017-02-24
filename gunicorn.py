#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''
import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1


NAME="MBTI"                            # Name of the application
FLASKDIR="/home/ec2-user/MBTI/"         # Django project directory
SOCKFILE="/home/ec2-user/run/gunicorn.sock"        # we will communicte using this unix socket
USER="ec2-user"                                  # the user to run as
GROUP="ec2-user"                                     # the group to run as"
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn

print "Starting $NAME"
name = NAME
user = USER
group = GROUP

if __name__ == '__main__':
    pass
