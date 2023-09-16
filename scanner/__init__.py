"""Network scanner library"""

from .registry import ServiceRegistry

registry = ServiceRegistry()
registry.add("HTTP", [80, 443, 8080])
registry.add("SSH", [22])
registry.add("DNS", [53])

def register_known_service(name, ports):
    """Registers additional service to global service registry"""

    registry.add(name, ports)
