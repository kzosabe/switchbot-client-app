from switchbot_client.devices import Bot
from switchbot_client.devices.status import BotDeviceStatus

from switchbot_client_app.component import (
    gen_command_button,
    gen_label,
    gen_turn_on_off_area,
)
from switchbot_client_app.section import DeviceSection


class BotSection(DeviceSection[Bot, BotDeviceStatus]):
    def __init__(self, device: Bot):
        super().__init__(device)
        self.label_power = gen_label()
        self.add_widgets(
            self.label_power,
            gen_turn_on_off_area(device, self.obj()),
            gen_command_button(device.press, "press", self),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
