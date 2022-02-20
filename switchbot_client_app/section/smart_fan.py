from switchbot_client.devices import SmartFan
from switchbot_client.devices.status import SmartFanDeviceStatus

from switchbot_client_app.component import (
    gen_button,
    gen_label,
    gen_refresh_button,
    gen_slider,
    gen_turn_on_off_area,
)
from switchbot_client_app.section import DeviceSection


class SmartFanSection(DeviceSection[SmartFan, SmartFanDeviceStatus]):
    def __init__(self, device: SmartFan):
        super().__init__(device)
        self.label_mode = gen_label()
        self.label_speed = gen_label()
        self.label_shake_range = gen_label()
        self.label_shake_center = gen_label()
        self.label_is_shaking = gen_label()
        self.add_widgets(
            gen_turn_on_off_area(device, self.obj()),
            self.label_mode,
            gen_button(device, lambda d: d.set_fan_mode(), "set_fan_mode"),
            self.label_speed,
            gen_button(device, lambda d: d.set_fan_speed(), "set_fan_speed"),
            self.label_shake_range,
            gen_slider(device, 0, 120, lambda d, value: d.set_shake_range(value), self),
            self.label_shake_center,
            self.label_is_shaking,
            gen_refresh_button(self.obj()),
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
