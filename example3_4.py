"""Example on using list, set, dict, tuple, for, while, if constructs"""

# dict
services = {
    "HTTP": [80, 443, 8080],
    "SSH": [22],
    "DNS": [53]
}

# list
servers = [
    {"name": "test.localhost.lan", "services": ["HTTP", "SSH"]},
    {"name": "dns.localhost.lan", "services": ["DNS", "SSH"]}
]

server_ports = []

# for loop
for server in servers:
    # set
    ports = set([])
    for service in server["services"]:
        ports = ports.union(set(services[service]))
    server_ports.append((server["name"], list(ports)))

all_ports = []

# range loop
for i in range(0, len(server_ports), 1):
    # tuple
    server_name, ports = server_ports[i]
    print(f"Server '{server_name}' has ports: {', '.join(map(str, ports))}")
    all_ports.append(ports)

ports = set([])

# while loop
i = 0
while i < len(all_ports):
    if len(ports) == 0:
        ports = set(all_ports[i])
    else:
        ports = ports.intersection(all_ports[i])
    i += 1

if len(ports) == 0:
    print("Servers has no common ports")
else:
    print(f"All servers has common ports: {', '.join(map(str, ports))}")
