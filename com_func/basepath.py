from com_func.confread import config
import os

class TestPath(object):

    def __init__(self) :
        self.BasePth = os.getcwd()
        self.WebDrive = os.path.join(os.sep, self.BasePth, config.get("ENV", "drive_path"))
        self.Brown = config.get("ENV", "brown_path").replace("\\", os.sep)
        print(self.WebDrive, self.Brown)


testpath = TestPath()