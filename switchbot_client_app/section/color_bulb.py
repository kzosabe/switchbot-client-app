from switchbot_client.devices import ColorBulb
from switchbot_client.devices.status import ColorBulbDeviceStatus

from switchbot_client_app.component import (
    gen_color_slider,
    gen_label,
    gen_slider,
    gen_turn_on_off_area,
)
from switchbot_client_app.section import DeviceSection


class ColorBulbSection(DeviceSection[ColorBulb, ColorBulbDeviceStatus]):
    def __init__(self, device: ColorBulb):
        super().__init__(device)
        self.label_power = gen_label()
        self.label_brightness = gen_label()
        self.label_color_hex = gen_label()
        self.label_color_temperature = gen_label()
        self.add_widgets(
            self.label_power,
            gen_turn_on_off_area(device, self.obj()),
            self.label_brightness,
            gen_slider(device, 1, 100, lambda d, value: d.set_brightness(value), self.obj()),
            self.label_color_hex,
            gen_color_slider(device, lambda d, r, g, b: d.set_color_by_number(r, g, b), self.obj()),
            self.label_color_temperature,
            gen_slider(
                device, 2700, 6500, lambda d, value: d.set_color_temperature(value), self.obj()
            ),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
        self.label_brightness.setText(f"brightness: {status.brightness}")
        self.label_color_hex.setText(f"color_hex: {status.color_hex}")
        self.label_color_temperature.setText(f"color_temperature: {status.color_temperature}")
