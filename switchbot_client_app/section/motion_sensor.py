from switchbot_client.devices import MotionSensor
from switchbot_client.devices.status import MotionSensorDeviceStatus

from switchbot_client_app.component import Label, RefreshButton
from switchbot_client_app.section import DeviceSection


class MotionSensorSection(DeviceSection[MotionSensor, MotionSensorDeviceStatus]):
    def __init__(self, device: MotionSensor):
        super().__init__(device)
        self.label_brightness = Label()
        self.label_is_move_detected = Label()
        self.add_widgets(
            self.label_brightness, self.label_is_move_detected, RefreshButton(self.obj())
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_brightness.setText(f"brightness: {status.brightness}")
        self.label_is_move_detected.setText(f"is_move_detected: {status.is_move_detected}")
