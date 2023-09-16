"""Example on using classes, exceptions"""

class ServiceRegistry:
    """Generic service information registry"""

    def __init__(self):
        self.__registry = {}

    def add(self, name, known_ports):
        """Add a new service to registry"""
        if name in self.__registry:
            raise ValueError(f"service '{name}' is already in registry")

        self.__registry[name] = known_ports

    def ports(self, name):
        """Get list of known ports for sepcific service"""

        if not name in self.__registry:
            raise KeyError(f"service '{name}' is not known")

        return self.__registry[name]

class HostNotFoundException(Exception):
    """Host not found exception"""

    def __init__(self, host):
        super().__init__(f"host '{host} not found")

class Scenario:
    """Exercise scenario"""

    def __init__(self, registry):
        self.__targets = {}
        self.__registry = registry

    def add(self, host, services):
        """Add a new target """

        if not host in self.__targets:
            self.__targets[host] = services
            return

        self.__targets = list(set(self.__targets[host]).union(set(services)))

    def ports(self, host):
        """Get specific host ports"""

        if not host in self.__targets:
            raise HostNotFoundException(host)

        ports = set([])
        for service in self.__targets[host]:
            ports = ports.union(set(self.__registry.ports(service)))

        return list(ports)


registry = ServiceRegistry()
registry.add("HTTP", [80, 443, 8080])
registry.add("SSH", [22])
registry.add("DNS", [53])
try:
    registry.add("DNS", [54])
except ValueError:
    print("Service DNS already exists in registry")

s = Scenario(registry)
s.add("test.localhost.lan", ["HTTP", "SSH"])
print(s.ports("test.localhost.lan"))
try:
    print(s.ports("ns.localhost.lan"))
except HostNotFoundException as e:
    print(e)
