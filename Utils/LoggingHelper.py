import logging


class loggingHelper:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler('GameOfTomer.log')
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s -  - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)


        consolehandler=logging.StreamHandler()
        consolehandler.setFormatter(formatter)


        # add the handlers to the logger
        self.logger.addHandler(handler)
        self.logger.addHandler(consolehandler)

    def log_info(self, msg):
        self.logger.info(msg);

    def log_error(self, msg):
        self.logger.error(msg);

    def log_warn(self, msg):
        self.logger.warn(msg);

    def log_debug(self, msg):
        self.logger.debug(msg);
