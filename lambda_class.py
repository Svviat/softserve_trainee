import logging

logger = logging.getLogger("THIS IS LOGGER")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s, %(name)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('study/info_logfile.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Firstask:
    def __init__(self, first_file, second_file, func):
        self.first_file = first_file
        self.second_file = second_file
        self.func = func

        logger.info("\nCurrent file: {}\nRecorded file: {}\nFunction: {}".format(self.first_file, self.second_file,
                                                                                 self.func))

    def rewrite(self):
        with open(self.first_file) as open_text:
            for text in open_text:
                if text.strip() == '':
                    continue
                mystr = eval(self.func)(text)
                with open(self.second_file, "a") as draft:
                    draft.writelines(mystr + "\n")


task = Firstask('study/example02', 'study/test513.txt', 'lambda line: line.split()[0]')
task.rewrite()
