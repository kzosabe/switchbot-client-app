from typing import Generic, List

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from switchbot_client.devices.status import DeviceStatus

from switchbot_client_app.object import AnyDevice, AnyDeviceStatus, DeviceStatusObject


class DeviceSection(QtWidgets.QGroupBox, Generic[AnyDevice, AnyDeviceStatus]):
    def __init__(self, device: AnyDevice):
        super().__init__(title=device.device_name)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.valueUpdated = QtCore.Signal(DeviceStatus)
        self.__obj: DeviceStatusObject = DeviceStatusObject(device)
        self.__obj.valueUpdated.connect(self.update_status)

    def obj(self) -> DeviceStatusObject[AnyDevice, AnyDeviceStatus]:
        return self.__obj

    def init_status(self):
        self.__obj.update_immediately()

    def add_widget(self, widget: QtWidgets.QWidget):
        self.layout().addWidget(widget)

    def add_widgets(self, *widgets: List[QtWidgets.QWidget]):
        for widget in widgets:
            self.layout().addWidget(widget)

    @Slot(DeviceStatus)
    def update_status(self):
        pass
