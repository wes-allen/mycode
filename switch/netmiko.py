#!/usr/bin/python3

from netmiko import ConnectHandler

##describe the device to connect to
##username, password, ip addresses, driver
##two switches...


switches = [{"un": "admin", "pw": "alta3", "ip": "172.16.2.10", "driver": "arista_eos"}, {"un": "admin", "pw": "alta3", "ip": "172.16.2.20", "driver": "arista_eos"}]

##connect to switches - use netmiko

for switch in switches:
    open_connection = ConnectHandler(device_type=switch.get('driver'), ip=switch.get('ip'), username=switch.get('un'), password=switch.get('pw'))
    
    ##issue a command to the switch
    my_command = open_connection.send_command('show ip int brief')
   
    ##display results of command
    print(my_command)


   ##close connection
  ## print(dir(open_connection))
   open_connection.disconnect()
