#!/usr/bin/env python

import os

print("Please enter the SSID of the wireless network:")
ssid = str(raw_input())
print("Please enter the password for the network:")
key = str(raw_input())

# Now create the entry in the wpa_supplicatn.conf file with encrypted key
os.system('echo "{}" | wpa_passphrase "{}" >> /etc/wpa_supplicant/wpa_supplicant.conf'.format(key, ssid))

# Now remove the plaintext password
os.system('sed -i "/#/d" /etc/wpa_supplicant/wpa_supplicant.conf')
