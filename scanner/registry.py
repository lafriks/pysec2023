"""Known service registry"""

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
