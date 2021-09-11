import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from switchbot_client import SwitchBotAPIClient, DeviceType, RemoteType


class MyWidget(QtWidgets.QWidget):

    def gen_button(self, client, device, command):
        device_name = device["deviceName"]
        device_id = device["deviceId"]
        button = QtWidgets.QPushButton(f"{device_name} - {command}")

        def click():
            print(device_id, client.devices_commands(device_id, command))

        button.clicked.connect(click)
        return button

    def gen_section(self, parent_layout, client, device):
        layout = QtWidgets.QVBoxLayout(self)
        if "deviceType" in device:
            if device["deviceType"] == DeviceType.METER:
                status = client.devices_status(device["deviceId"]).body["temperature"]
                label = QtWidgets.QLabel(f"{status}", alignment=QtCore.Qt.AlignCenter)
                layout.addWidget(label)
        elif "remoteType" in device:
            if device["remoteType"] in [RemoteType.LIGHT, RemoteType.AIR_CONDITIONER]:
                layout.addWidget(self.gen_button(client, device, "turnOn"))
                layout.addWidget(self.gen_button(client, device, "turnOff"))

        box = QtWidgets.QGroupBox(title=device["deviceName"])
        box.setLayout(layout)
        parent_layout.addWidget(box)

    def __init__(self):
        super().__init__()
        client = SwitchBotAPIClient()
        response = client.devices()
        physical_devices = response.body["deviceList"]
        remote_devices = response.body["infraredRemoteList"]

        self.layout = QtWidgets.QVBoxLayout(self)

        for device in physical_devices:
            self.gen_section(self.layout, client, device)

        for device in remote_devices:
            self.gen_section(self.layout, client, device)


def run():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(300, 600)
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
