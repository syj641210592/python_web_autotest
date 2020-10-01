from com_func.confread import config
import os

class TestPath(object):

    def __init__(self) :
        self.BasePath = os.getcwd()
        self.ScreenShot = os.path.join(os.sep, self.BasePath, "screenshot")
        self.ReportPath = os.path.join(os.sep, self.BasePath, config.get("ENV", "report_path"))
        self.LogDirPath = os.path.join(os.sep, self.BasePath, config.get("ENV", "log_path"))
testpath = TestPath()