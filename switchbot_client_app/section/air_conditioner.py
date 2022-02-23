from switchbot_client.devices import AirConditioner
from switchbot_client.devices.status import PseudoRemoteDeviceStatus

from switchbot_client_app.component import (
    CenterLabel,
    ComboBox,
    CommandButton,
    FloatInput,
)
from switchbot_client_app.section import DeviceSection


class AirConditionerSection(DeviceSection[AirConditioner, PseudoRemoteDeviceStatus]):
    def __init__(self, device: AirConditioner):
        super().__init__(device)
        self.label_power = CenterLabel("power:")

        self.temperature_input = FloatInput(
            label="temperature", min_value=10, max_value=50, default_value=25, singlestep=0.5
        )

        self.mode_input = ComboBox(
            label="mode",
            items=[
                ("AUTO", AirConditioner.Parameters.MODE_AUTO),
                ("FAN", AirConditioner.Parameters.MODE_FAN),
                ("DRY", AirConditioner.Parameters.MODE_DRY),
                ("COOL", AirConditioner.Parameters.MODE_COOL),
                ("HEAT", AirConditioner.Parameters.MODE_HEAT),
            ],
        )

        self.fan_speed_input = ComboBox(
            label="fan speed",
            items=[
                ("AUTO", AirConditioner.Parameters.FAN_SPEED_AUTO),
                ("LOW", AirConditioner.Parameters.FAN_SPEED_LOW),
                ("MEDIUM", AirConditioner.Parameters.FAN_SPEED_MEDIUM),
                ("HIGH", AirConditioner.Parameters.FAN_SPEED_HIGH),
            ],
        )

        def turn_on_with_values():
            return device.set_all(
                temperature=self.temperature_input.value(),
                mode=self.mode_input.value(),
                fan_speed=self.fan_speed_input.value(),
                power=AirConditioner.Parameters.POWER_ON,
            )

        self.turn_on = CommandButton("turn on with values", turn_on_with_values, self.obj())
        self.turn_off = CommandButton("turn off", device.turn_off, self.obj())
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
