import bluetooth

target_name = "My Phone"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"
    
    
    
# package required for 'pand' command
# sudo apt-get install bluez-compat
 
# connect to phone and sets up network interface
#sudo pand --connect target_address -n
 
# show networks
#ifconfig
 
# set dhclient to use bnep0 
#sudo dhclient bnep0
