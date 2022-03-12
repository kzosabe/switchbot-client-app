from switchbot_client.devices import ContactSensor
from switchbot_client.devices.status import ContactSensorDeviceStatus

from switchbot_client_app.component import RefreshButton, gen_label
from switchbot_client_app.section import DeviceSection


class ContactSensorSection(DeviceSection[ContactSensor, ContactSensorDeviceStatus]):
    def __init__(self, device: ContactSensor):
        super().__init__(device)
        self.label_brightness = gen_label()
        self.label_open_state = gen_label()
        self.label_is_move_detected = gen_label()
        self.add_widgets(
            self.label_brightness,
            self.label_open_state,
            self.label_is_move_detected,
            RefreshButton(self.obj()),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_brightness.setText(f"brightness: {status.brightness}")
        self.label_open_state.setText(f"open_state: {status.open_state}")
        self.label_is_move_detected.setText(f"is_move_detected: {status.is_move_detected}")
