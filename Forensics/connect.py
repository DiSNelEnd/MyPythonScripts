import subprocess
import re
from typing import List


def check_active_connections() -> List[dict]:
    output = subprocess.check_output(['netstat','-na']).decode('cp866')

    spaces = re.findall(r'\s+', output)
    strings = output.split('\n')

    for space in spaces:
        for i in range(len(strings)):
            strings[i] = strings[i].replace(space, ' ')
    
    listening = []
    
    print(f"{len(strings)} connections :)")

    for string in strings:
        if string.find('LISTENING') > 0:
            splited = string.split(' ')
            listening.append(dict(type = splited[1], adress = splited[3], status = splited[4].strip()))
    
    return listening

active_connects = check_active_connections()

for connect in active_connects:
    with open('connects.txt', 'wt', encoding='utf-8') as f:
        f.write(f"{connect}\n")

print("End :)")


    


