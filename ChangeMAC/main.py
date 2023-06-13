import subprocess
from parserMAC import Parser
import os


def change_mac_unix(interface, newMac):
    if not do_root_permission:
        print(":( Faild to get root permission")
        exit(1)

    print(":) Changing MAC address for " + interface + " to " + newMac)
    print()
    print (":) Shoting down " + interface)

    subprocess.call("sudo ifconfig " + interface + " down", shell=True)

    print(":) Changing MAC to " + newMac)

    subprocess.call("sudo ifconfig " + interface + " hw ether" + newMac, shell=True)

    print(":) Powering UP " + interface)

    subprocess.call("sudo ifconfig " + interface + " up", shell=True)

    print("End :)")

    subprocess.call("sudo ifconfig " + interface, shell=True)

def do_root_permission():
    if os.getevid() != 0:
        ret = subprocess.call("sudo -n true >> /dev/null", shell=True)

        if ret != 0:
            print (":( This operation require root permission")
            msq = "[sudo] password for %u: "
            ret = subprocess.call("sudo -v -p '%s'" % msq, shell=True)
            return ret == 0

    return True

parser= Parser()
change_mac_unix(parser.interface, parser.new_mac)