import configparser

read_ini = configparser.RawConfigParser()
read_ini.read(r"..\Configuration\config.ini")

# print(read_ini.get("common data", "url"))
# print(read_ini.get("common data", "username"))
# print(read_ini.get("common data", "password"))
# print(read_ini.get("driver path", "chrome_driver"))

class ReadProperty:
    @staticmethod
    def GetUrl():
        return read_ini.get("common data", "url")

    @staticmethod
    def GetUsername():
        return read_ini.get("common data", "username")

    @staticmethod
    def GetPassword():
        return read_ini.get("common data", "password")

    @staticmethod
    def GetChromeDriver():
        return read_ini.get("driver path", "chrome_driver")

    @staticmethod
    def GetChromeDriverBeta():
        return read_ini.get("driver path", "chrome_driver_beta")

    @staticmethod
    def GetEdgeDriver():
        return read_ini.get("driver path", "edge_driver")

    @staticmethod
    def GetFirefoxDriver():
        return read_ini.get("driver path", "firefox_driver")