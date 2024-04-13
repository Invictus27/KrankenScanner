import socket

# variable for colored text
blue = "\033[94m"
green = "\033[92m"
red = "\033[91m"
normal = "\033[0m"

#Main scanning function
def Scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        s.connect((ip, port))
        print(f"{green}[*] Port {port} is open{normal}")
        s.close()
    except socket.error:
        print(f"{red}[*] Port {port} is closed{normal}")

# List of common ports to scan
common_ports = [21, 22, 80, 443, 8080, 1433, 5060, 137, 139, 162, 161, 53, 23, 3306, 5432]

print(f"{blue}######Port-Scanner#######{normal}")
print(f"{blue}[*]Credit: Invictus27{normal}")
print(f"{blue}[*] This tool is for educational purposes only.{normal}")
print(f"{blue}[*] The developer does not support illegal use of this script.{normal}")
ip = input(f"{blue}[*] Enter IP address of the target: {normal}")

# Iterate through the common ports and perform the scan
for port in common_ports:
    Scan(ip, port)
