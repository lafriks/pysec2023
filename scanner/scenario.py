"""Scenario"""

from . import registry

class HostNotFoundException(Exception):
    """Host not found exception"""

    def __init__(self, host):
        super().__init__(f"host '{host} not found")

class Scenario:
    """Exercise scenario"""

    def __init__(self):
        self.__targets = {}

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
            ports = ports.union(set(registry.ports(service)))

        return list(ports)
