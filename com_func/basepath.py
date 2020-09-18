from com_func.confread import config
import os

class TestPath(object):

    def __init__(self) :
        self.BasePth = os.getcwd()
        self.ScreenShot = os.path.join(os.sep, self.BasePth, "screenshot")


testpath = TestPath()