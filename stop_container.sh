#!/bin/bash
set -e

# Stop the running container(s) (if any)
# Use `docker ps -q` to get only container IDs and capture output safely.
containerid=$(docker ps -q)

if [ -z "$containerid" ]; then
	echo "No running containers to stop."
	exit 0
fi

docker rm -f $containerid
