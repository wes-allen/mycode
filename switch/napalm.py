#!/usr/bin/python3

from napalm import get_network_driver

##create a driver object (selct the correct driver)

driver = get_network_driver('eos')

##describe where the driver will connect to
switch1 = driver('172.16.2.10', 'admin', 'alta3')

##open the Napalm connection
switch1.open()

response = switch1.get_facts()

if float(response.get("os_version")[0:4]) < 4.15
    print("Switch does NOT meet minimum requirements!")
    switch1.close()
    exit()
else
    print('Switch meets minimum requirements')

##other stuff we want to do to our switch

##print(float(response.get("os_version")[0:4]))


##close connection
switch1.close()
