#!/bin/bash
echo "building .pex executable"

pex . -r requirements.txt -c name_old_repositories.py -o name_old_repositories.pex
