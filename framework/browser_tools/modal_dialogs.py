from selenium.webdriver.common.alert import Alert
from framework.driver.webdriver_singleton import Driver
from tools.logger import Logger


class AlertActions:
    def __init__(self):
        self.driver = Driver().connect()

    def dialog_accept(self):
        Logger(__name__).write_info("dialog accept button is clicked")
        return Alert(self.driver).accept()

    def dialog_text_input(self, text):
        Logger(__name__).write_info(text + " has been sent")
        return Alert(self.driver).send_keys(text)

    def dialog_dismiss(self):
        Logger(__name__).write_info("dialog dismiss button is clicked")
        return Alert(self.driver).dismiss()
