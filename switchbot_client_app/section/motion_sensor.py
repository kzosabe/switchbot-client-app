from switchbot_client.devices import MotionSensor
from switchbot_client.devices.status import MotionSensorDeviceStatus

from switchbot_client_app.component import gen_label, gen_refresh_button
from switchbot_client_app.section import DeviceSection


class MotionSensorSection(DeviceSection[MotionSensor, MotionSensorDeviceStatus]):
    def __init__(self, device: MotionSensor):
        super().__init__(device)
        self.label_brightness = gen_label()
        self.label_is_move_detected = gen_label()
        self.add_widgets(
            self.label_brightness, self.label_is_move_detected, gen_refresh_button(self.obj())
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_brightness.setText(f"brightness: {status.brightness}")
        self.label_is_move_detected.setText(f"is_move_detected: {status.is_move_detected}")
