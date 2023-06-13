import socket


def check_is_open_port(port: int) -> bool:
    opened = False

    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind(('localhost',port))

        soc.listen()
        soc.close()
    except socket.error:
        pass
    else:
        opened = True
    
    return opened

print("Processing... :)")

for i in range(1024,65536):
    with open('ports.txt', 'wt', encoding='utf-8') as f:
        f.write(f"Port {i} is opened - {check_is_open_port(i)}\n")

print("End :)")
