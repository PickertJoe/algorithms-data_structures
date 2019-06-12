# Replica of the circuit model built in Chapter 1 of the text


class LogicGate():
    """A master class to serve as a parent for later gates"""

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """A class to simulate gates requiring two streams of input"""

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Please enter Pin A input for gate " + self.getLabel() + ": "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        return int(input("Please enter Pin B input for gate " + self.getLabel() + ": "))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pibB == None:
                self - pinB = source
            else:
                raise RunetimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """A class to similuate gates requiring only one stream of input"""

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Please enter Pin input for gate " + self.getLabel() + ": "))


class AndGate(BinaryGate):
    """A class to simulate a gate requiring both inputs to be T to pass T"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA
        b = self.getPinB
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """A class to simulate a gate requiring only one input to be T to pass T"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA
        b = self.getPinB
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """A class to simulate a gate that reverses the boolean of the input it receives"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPin

        if a == 1:
            return 0
        else:
            return 1


class Connector:
    """A class to link the inputs and outputs of the appropriate gates"""

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNestPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
