from typing import Union

from switchbot_client.devices import Meter, MeterPlusJp, MeterPlusUs
from switchbot_client.devices.status import MeterDeviceStatus

from switchbot_client_app.component import Label, RefreshButton
from switchbot_client_app.section import DeviceSection

MeterLike = Union[Meter, MeterPlusJp, MeterPlusUs]


class MeterSection(DeviceSection[MeterLike, MeterDeviceStatus]):
    def __init__(self, device: MeterLike):
        super().__init__(device)
        self.label_temperature = Label()
        self.label_humidity = Label()
        self.add_widgets(self.label_temperature, self.label_humidity, RefreshButton(self.obj()))
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_temperature.setText(f"temperature: {status.temperature}")
        self.label_humidity.setText(f"humidity: {status.humidity}")
