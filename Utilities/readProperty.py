import configparser

#Get the current directory
import os

dirname = os.path.dirname(os.path.abspath('/home/algoworks/PycharmProjects/Pobal_Project_POM/config/config.ini'))

#Create a parser
config = configparser.ConfigParser()

#Read the file (read the configuration file with absolute path)
config.read(dirname + "/config.ini")
# config = configparser.RawConfigParser()
# config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('stageurl', 'baseURL')
        return url

    @staticmethod
    def getEmailid():
        emailid = config.get('logindetails', 'emailid')
        return emailid


    @staticmethod
    def getPassword():
        login_pass = config.get('logindetails', 'login_pass')
        return login_pass

    @staticmethod
    def getCounty_name():
        country_name = config.get('logindetails', 'country_name')
        return country_name

    @staticmethod
    def getPhone():
        phone = config.get('logindetails', 'phone')
        return phone

    # @staticmethod
    # def getBrExtention():
    #     browserExt = config.get('common-info', 'BrExt')
    #     return browserExt


    # @staticmethod
    # def getChromedriver():
    #     chromedriver = config.get('common-info', 'chrome_driver')
    #     return chromedriver
