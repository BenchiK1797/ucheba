class Cars:
    def __init__(self,carBody,motor,color):
        self._carBody = carBody
        self._motor = motor
        self._color = color
    def getCarBody(self):
        return self._carBody
    def getMotor(self):
        return self._motor
    def getColor(self):
        return self._color
    def getInfo(self):
        return [self.getColor(),self.getCarBody(),self.getMotor()]