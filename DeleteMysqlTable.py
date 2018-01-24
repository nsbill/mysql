#!/usr/bin/env python3
#import sys
#sys.path.insert(0, '/app/db')
from mysql_select import query_with_delete
#import subprocess

while True:
    user = query_with_delete()
    print(user)
