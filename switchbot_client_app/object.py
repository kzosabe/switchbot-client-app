from typing import Generic, TypeVar

from PySide6 import QtCore
from PySide6.QtCore import QTimer, Signal
from switchbot_client.devices import SwitchBotDevice
from switchbot_client.devices.status import DeviceStatus

AnyDevice = TypeVar("AnyDevice", bound=SwitchBotDevice)
AnyDeviceStatus = TypeVar("AnyDeviceStatus", bound=DeviceStatus)


class DeviceStatusObject(QtCore.QObject, Generic[AnyDevice, AnyDeviceStatus]):
    value_changed = Signal(DeviceStatus)

    def __init__(self, device: AnyDevice):
        super().__init__()
        self.device = device
        self.__status = None

    def status(self) -> AnyDeviceStatus:
        if self.__status is None:
            self.update_immediately()
        return self.__status  # type: ignore

    def update_immediately(self):
        self._update()

    def update(self):
        # FIXME: wait for execution delay
        timer = QTimer(self)
        timer.setInterval(1000)
        timer.setSingleShot(True)
        timer.timeout.connect(self._update)
        timer.start()

    def _update(self):
        self.__status = self.device.status()
        self.value_changed.emit(self.__status)
