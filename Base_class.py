import urllib2
import shutil
import os
import logging
from abc import ABCMeta, abstractmethod

logger = logging.getLogger("THIS IS LOGGER")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s, %(name)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('info_logfile.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Base:
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

    @abstractmethod
    def run(self):
        raise NotImplementedError("Must override run")


class Getter(Base):

    def run(self):
        for url in self.URL:
            response = urllib2.urlopen(url)
            if not os.path.exists(self.DIR_PATH):
                os.makedirs(self.DIR_PATH)
            file_name = url[-5:] + '.txt'
            with open(self.DIR_PATH + "/" + file_name, "wb") as txt_file:
                shutil.copyfileobj(response, txt_file)
                del response
                print "Full path of ///{}///  is:  {}".format(file_name,
                                                              os.path.abspath(self.DIR_PATH + "/" + file_name))


class Flexible(Base):

    def run(self):
        for file in self.DIR:
            logger.info("\nCurrent file: {}\nRecorded file: {}\nFunction: {}".format(file, file + "recorded.txt",
                                                                                     self.FUNC))
            with open(file) as open_text:
                for text in open_text:
                    if text.strip() == '':
                        continue
                    mystr = eval(self.FUNC)(text)
                    with open(file + "recorded.txt", "a") as draft:
                        draft.writelines(mystr + "\n")


if __name__ == "__main__":
    flex = Flexible(FUNC='lambda line: line.split()[0]', DIR=['example01', 'example02'])
    flex.run()
    gett = Getter(URL=['https://drive.google.com/uc?export=download&id=1Z_ZNiCTmNeCurEkJKdSdrAcPhOJmR5_U',
                       'https://drive.google.com/uc?export=download&id=1XhHv7dlUFtTJH8YKGFus0jGPKGmuk6_w'],
                  DIR_PATH="data")
    gett.run()
