import getpass
from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}

def acces_netmiko():
    with ConnectHandler(**router) as net_connect:
         print("Connected to remote router.")

         print("Getting router's date...")
         dte_cmd = "show clock"
         dte_out = net_connect.send_command(dte_cmd)
         print("Date below: ", dte_out)

         print("Getting network interfaces...")
         nic_cmd = "show ip interface brief"
         nic_out = net_connect.send_command(nic_cmd)

         with open("interface_list.txt", "w") as f:
             f.write(nic_out)

         print("Done.")

print("Hello, Git! Working on it...")
acces_netmiko()
