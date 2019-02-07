import urllib2
import shutil
import os


class Getter:
    def __init__(self, URL):
        self.URL = URL
        self.DIR_PATH = 'data'

    def get_file(self):
        for url in self.URL:
            response = urllib2.urlopen(url)
            if not os.path.exists(self.DIR_PATH):
                os.makedirs(self.DIR_PATH)
            file_name = url[-5:] + '.txt'
            with open(self.DIR_PATH + "/" + file_name, "wb") as txt_file:
                shutil.copyfileobj(response, txt_file)
                del response
                print "Full path of ///{}///  is:  {}".format( file_name,os.path.abspath(self.DIR_PATH + "/" + file_name))


if __name__ == "__main__":
    ALLURL = 'https://drive.google.com/uc?export=download&id=1Z_ZNiCTmNeCurEkJKdSdrAcPhOJmR5_U', 'https://drive.google.com/uc?export=download&id=1XhHv7dlUFtTJH8YKGFus0jGPKGmuk6_w'
    get = Getter(URL=[x for x in ALLURL])
    get.get_file()
