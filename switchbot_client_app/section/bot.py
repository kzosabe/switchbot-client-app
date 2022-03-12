from switchbot_client.devices import Bot
from switchbot_client.devices.status import BotDeviceStatus

from switchbot_client_app.component import (
    CommandButton,
    Label,
    RefreshButton,
    TurnOnOffArea,
)
from switchbot_client_app.section import DeviceSection


class BotSection(DeviceSection[Bot, BotDeviceStatus]):
    def __init__(self, device: Bot):
        super().__init__(device)
        self.label_power = Label()
        self.add_widgets(
            self.label_power,
            TurnOnOffArea(device, self.obj()),
            CommandButton("press", device.press, self),
            RefreshButton(self.obj()),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
