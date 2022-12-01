from utils import BLACK, WHITE


class ForGroundBackGroundColor:
    def __init__(self):
        self.forgroundColor = WHITE
        self.backgroundColor = BLACK

    def setForegroundColor(self, FGcolor):
        self.forgroundColor = FGcolor

    def setBackgroundColor(self, BGcolor):
        self.backgroundColor = BGcolor

    def getForegroundColor(self):
        return self.forgroundColor

    def getBackgroundColor(self):
        return self.backgroundColor