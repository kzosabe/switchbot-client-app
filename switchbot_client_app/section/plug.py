from typing import Union

from switchbot_client.devices import Plug, PlugMiniJp, PlugMiniUs
from switchbot_client.devices.status import PlugDeviceStatus

from switchbot_client_app.component import Label, RefreshButton, gen_turn_on_off_area
from switchbot_client_app.section import DeviceSection

PlugLike = Union[Plug, PlugMiniJp, PlugMiniUs]


class PlugSection(DeviceSection[PlugLike, PlugDeviceStatus]):
    def __init__(self, device: PlugLike):
        super().__init__(device)
        self.label_power = Label()
        self.add_widgets(
            self.label_power,
            gen_turn_on_off_area(device, self.obj()),
            RefreshButton(self.obj()),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
