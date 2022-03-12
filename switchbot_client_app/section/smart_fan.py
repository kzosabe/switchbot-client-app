from switchbot_client.devices import SmartFan
from switchbot_client.devices.status import SmartFanDeviceStatus

from switchbot_client_app.component import (
    Button,
    Label,
    RefreshButton,
    Slider,
    TurnOnOffArea,
)
from switchbot_client_app.section import DeviceSection


class SmartFanSection(DeviceSection[SmartFan, SmartFanDeviceStatus]):
    def __init__(self, device: SmartFan):
        super().__init__(device)
        self.label_mode = Label()
        self.label_speed = Label()
        self.label_shake_range = Label()
        self.label_shake_center = Label()
        self.label_is_shaking = Label()
        self.add_widgets(
            TurnOnOffArea(device, self.obj()),
            self.label_mode,
            Button(device, lambda d: d.set_fan_mode(), "set_fan_mode"),
            self.label_speed,
            Button(device, lambda d: d.set_fan_speed(), "set_fan_speed"),
            self.label_shake_range,
            Slider(device, 0, 120, lambda d, value: d.set_shake_range(value), self),
            self.label_shake_center,
            self.label_is_shaking,
            RefreshButton(self.obj()),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_mode.setText(f"mode: {status.mode}")
        self.label_speed.setText(f"speed: {status.speed}")
        self.label_shake_range.setText(f"shake_range: {status.shake_range}")
        self.label_shake_center.setText(f"shake_center: {status.shake_center}")
        self.label_is_shaking.setText(f"is_shaking: {status.is_shaking}")
