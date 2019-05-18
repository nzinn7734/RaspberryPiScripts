#!/usr/bin/env python

import os

#Run this as admin.

print("Enabling SSH....")
os.system('systemctl enable ssh')
print("Starting SSH....")
os.system('systemctl start ssh')
print("Done")


