import os
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QScrollArea
from switchbot_client import SwitchBotClient

from switchbot_client_app.section import gen_section


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        print(f"executable path: {os.getcwd()}")
        local_config_path = os.path.join(os.getcwd(), "config.yml")
        if os.path.exists(local_config_path):
            client = SwitchBotClient(config_file_path=local_config_path)
        else:
            client = SwitchBotClient()
        for device in client.devices():
            layout = QtWidgets.QVBoxLayout()
            section = gen_section(self, layout, device)
            if section is not None:
                self.layout().addWidget(section)


def run():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    scroll = QScrollArea()
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    scroll.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
