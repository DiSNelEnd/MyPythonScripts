import argparse
import random
import re


class Parser:
    
    def __init__(self): 
        parser = argparse.ArgumentParser()

        parser.add_argument("-i", "--interface", dest="interface", help="Interface for change mac address (ipconfig) :)")
        parser.add_argument("-m", "--mac", dest="newMac", help=" New MAC address :)")
        parser.add_argument("-f", "--field", dest="fieldNumb", help="Type field number here :)")

        options = parser.parse_args()
        self.__pattern_mac= r'(\w{2}:){5}\w{2}'
        
        if not options.interface:
            parser.error(":( Please specify an interface, use --help or -h for more info")
        elif not options.newMac or not re.match(self.__pattern_mac,options.newMac):
            cond= input("Generate random MAC y/n? :) > ")
            if cond == 'y':
                options.newMac = self.__get_random_mac()
                print (f"New MAC -> {options.newMac} :)")
            else:
                parser.error(":( Please specify a new MAC address, use --help or -h for more info")
        
        self.__interface = options.interface
        self.__mac = options.newMac
        self.__field = options.fieldNumb

    @property
    def interface(self) -> str:
        return self.__interface
    
    @property
    def new_mac(self) -> str:
        return re.match(self.__pattern_mac,self.__mac).group(0)
    
    @property
    def field(self) -> str:
        return self.__field

    def __get_random_mac(self):
        oui_list = [
            ["CC", "46", "D6"],
            ["3C", "5A", "B4"],
            ["3C", "D9", "2B"],
            ["24", "46", "CB"]
        ]
        nic_specific_rnd =[
            "%02x" % (random.randint(1,255)),
            "%02x" % (random.randint(1,255)),
            "%02x" % (random.randint(1,255)),
        ]

        rnd_oui = oui_list[random.randrange(0,len(oui_list))]
        return ":".join(rnd_oui + nic_specific_rnd)
