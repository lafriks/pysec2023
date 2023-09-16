"""Example on custom packages"""

from scanner.scenario import Scenario

s = Scenario()
s.add("test.localhost.lan", ["HTTP", "SSH"])
print(s.ports("test.localhost.lan"))
