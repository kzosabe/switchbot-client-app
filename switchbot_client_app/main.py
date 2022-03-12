import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from switchbot_client import SwitchBotClient

from switchbot_client_app.constants import APP_VERSION
from switchbot_client_app.factory import gen_section


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        print(f"executable path: {os.getcwd()}")
        local_config_path = os.path.join(os.getcwd(), "config.yml")
        if os.path.exists(local_config_path):
            client = SwitchBotClient(config_file_path=local_config_path)
        else:
            client = SwitchBotClient()
        for device in client.devices():
            section = gen_section(device)
            if section is not None:
                self.layout().addWidget(section)
            else:
                print(f"no available section: {device.device_type}")


def run():
    app = QApplication([])
    window = QMainWindow()
    widget = MyWidget()
    widget.setBaseSize(QSize(800, 600))
    scroll = QScrollArea()
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    scroll.setBaseSize(QSize(800, 600))
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    widget.setContentsMargins(32, 8, 32, 8)
    window.setCentralWidget(scroll)
    window.setWindowTitle(f"switchbot-client-app v{APP_VERSION}")
    window.resize(QSize(400, 600))
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
