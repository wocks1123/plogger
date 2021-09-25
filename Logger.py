import logging
import logging.handlers

def get_logger(name, file_name):
    _log = logging.getLogger(name)
    logLevel = logging.DEBUG
    logFileName = file_name
    # LogFormat = logging.Formatter('[%(process)d|%(thread)d|%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s: %(message)s')
    # logFormat = logging.Formatter('%(levelname)s||%(asctime)s||%(message)s')

    # Console
    consoleHandler = logging.StreamHandler()
    # consoleHandler.setFormatter(LogFormat)

    # File
    fileHandler = logging.FileHandler(logFileName)
    # fileHandler.setFormatter(logFormat)

    _log.setLevel(logLevel)
    # _log.addHandler(consoleHandler)
    _log.addHandler(fileHandler)
    return _log

class Logger:
    def __init__(self, file_name, *, write_mode=True):

        self.write_mode = write_mode
        if write_mode:
            with open(file_name, "w") as fp:
                fp.write("")
        else:
            self.fp = open(file_name, "r")
            self.length = len(self.fp.readlines())
            print("length", self.length)

        self.objs = dict()
        self.__logger = get_logger("logger", file_name)

    def get_line_from(self, idx):
        self.fp.seek(0)
        for pos, l_num in enumerate(self.fp):
            if pos == idx:
                return l_num.rstrip().lstrip()
        return None

    def get_object_from(self, idx):
        line = self.get_line_from(idx)
        if not line:
            return None

        keys, _, values = line.partition("||")
        keys = eval(keys)
        values = values.split("%%")

        res_dict = dict()
        for k, v in zip(keys, values):
            loaded = eval(v)
            # print("v", loaded)
            # print("v", loaded["type"], loaded["value"])
            res_dict[k] = loaded["value"]
        return res_dict

    def __del__(self):
        if not self.write_mode:
            self.fp.close()

    def add(self, key, value):
        self.objs[key] = {"value": value, "type": type(value).__name__}

    def append_line(self):
        key_str = str(list(self.objs.keys()))
        val_str = "%%".join(list(map(str, self.objs.values())))

        self.__logger.debug(key_str + "||" + val_str)
        self.objs = {}