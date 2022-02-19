from switchbot_client.devices import Humidifier
from switchbot_client.devices.status import HumidifierDeviceStatus

from switchbot_client_app.component import gen_button, gen_label, gen_turn_on_off_area
from switchbot_client_app.section import DeviceSection


class HumidifierSection(DeviceSection[Humidifier, HumidifierDeviceStatus]):
    def __init__(self, device: Humidifier):
        super().__init__(device)
        self.label_power = gen_label()
        self.label_temperature = gen_label()
        self.label_humidity = gen_label()
        self.label_atomization_efficiency = gen_label()
        self.label_is_auto = gen_label()
        self.label_is_child_lock = gen_label()
        self.label_is_muted = gen_label()
        self.label_is_lack_water = gen_label()
        self.add_widgets(
            self.label_power,
            self.label_temperature,
            self.label_humidity,
            self.label_atomization_efficiency,
            self.label_is_auto,
            self.label_is_child_lock,
            self.label_is_muted,
            self.label_is_lack_water,
            gen_turn_on_off_area(device, self.obj()),
            gen_button(device, lambda d: d.set_mode(), "set_mode"),
            gen_button(
                device, lambda d: d.set_atomization_efficiency(), "set_atomization_efficiency"
            ),
            gen_button(device, lambda d: d.set_auto_mode(), "set_auto_mode"),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
        self.label_temperature.setText(f"temperature: {status.temperature}")
        self.label_humidity.setText(f"humidity: {status.humidity}")
        self.label_atomization_efficiency.setText(
            f"atomization_efficiency: {status.atomization_efficiency}"
        )
        self.label_is_auto.setText(f"is_auto: {status.is_auto}")
        self.label_is_child_lock.setText(f"is_child_lock: {status.is_child_lock}")
        self.label_is_muted.setText(f"is_muted: {status.is_muted}")
        self.label_is_lack_water.setText(f"is_lack_water: {status.is_lack_water}")