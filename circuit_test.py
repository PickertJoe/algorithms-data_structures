# A test to ensure proper functioning of the circuit class

from circuit_class import *

# If user enters 0,1,1,1 in the order prompted
# Running the test; end result should be 0, or False
def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


main()
