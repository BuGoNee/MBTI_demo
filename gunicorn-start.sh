#!/bin/bash

NAME="MBTI"                            # Name of the application
FLASKDIR=/home/ec2-user/MBTI/          # Django project directory
SOCKFILE=/home/ec2-user/run/gunicorn.sock         # we will communicte using this unix socket
USER=ec2-user                                     # the user to run as
GROUP=ec2-user                                     # the group to run as
NUM_WORKERS=5                                     # how many worker processes should Gunicorn spawn

echo "Starting $NAME"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your gunicorn
exec gunicorn app:app -b 0.0.0.0:8080 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE
