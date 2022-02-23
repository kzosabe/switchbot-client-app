from switchbot_client.devices import AirConditioner
from switchbot_client.devices.status import PseudoRemoteDeviceStatus

from switchbot_client_app.component import (
    exec_command_and_update,
    gen_combo_box,
    gen_command_button,
    gen_label,
    gen_number_input,
    gen_turn_on_off_area,
)
from switchbot_client_app.section import DeviceSection


class AirConditionerSection(DeviceSection[AirConditioner, PseudoRemoteDeviceStatus]):
    def __init__(self, device: AirConditioner):
        super().__init__(device)
        self.label_power = gen_label()

        self.temperature_input = gen_number_input(device, 10, 50, 25, None, self.obj())

        self.mode_input = gen_combo_box(device, None, self.obj())
        self.mode_input.addItem("AUTO", AirConditioner.Parameters.MODE_AUTO)
        self.mode_input.addItem("FAN", AirConditioner.Parameters.MODE_FAN)
        self.mode_input.addItem("DRY", AirConditioner.Parameters.MODE_DRY)
        self.mode_input.addItem("COOL", AirConditioner.Parameters.MODE_COOL)
        self.mode_input.addItem("HEAT", AirConditioner.Parameters.MODE_HEAT)

        self.fan_speed_input = gen_combo_box(device, None, self.obj())
        self.fan_speed_input.addItem("AUTO", AirConditioner.Parameters.FAN_SPEED_AUTO)
        self.fan_speed_input.addItem("LOW", AirConditioner.Parameters.FAN_SPEED_LOW)
        self.fan_speed_input.addItem("MEDIUM", AirConditioner.Parameters.FAN_SPEED_MEDIUM)
        self.fan_speed_input.addItem("HIGH", AirConditioner.Parameters.FAN_SPEED_HIGH)

        def turn_on_with_values():
            return device.set_all(
                temperature=float(self.temperature_input.value()),
                mode=self.mode_input.currentData(),
                fan_speed=self.fan_speed_input.currentData(),
                power=AirConditioner.Parameters.POWER_ON,
            )

        self.turn_on = gen_command_button(turn_on_with_values, "turn on with values", self.obj())
        self.turn_off = gen_command_button(lambda: device.turn_off(), "turn off", self.obj())
        self.add_widgets(
            self.label_power,
            self.temperature_input,
            self.mode_input,
            self.fan_speed_input,
            self.turn_on,
            self.turn_off,
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_power.setText(f"power: {status.power}")
