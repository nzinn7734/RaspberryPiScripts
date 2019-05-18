#!/usr/bin/env python

import os

print("Please enter 1 for unsuccessful SSH attempts and 2 for successful SSH attempts.")
option = int(raw_input())
if option == 1:
  os.system('cat /var/log/auth.log* | grep "Failed password"')
elif option == 2:
  os.system('cat /var/log/auth.log* | grep "Accepted password"')
else:
  print("Invalid operation try again")

