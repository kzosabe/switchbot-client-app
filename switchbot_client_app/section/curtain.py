from switchbot_client.devices import Curtain
from switchbot_client.devices.status import CurtainDeviceStatus

from switchbot_client_app.component import Label, RefreshButton, Slider, TurnOnOffArea
from switchbot_client_app.section import DeviceSection


class CurtainSection(DeviceSection[Curtain, CurtainDeviceStatus]):
    def __init__(self, device: Curtain):
        super().__init__(device)
        self.label_slide_position = Label()
        self.label_is_calibrated = Label()
        self.label_is_grouped = Label()
        self.label_is_moving = Label()
        self.add_widgets(
            TurnOnOffArea(device, self.obj()),
            self.label_slide_position,
            Slider(device, 1, 100, lambda d, value: d.set_position(value), self),
            self.label_is_calibrated,
            self.label_is_grouped,
            self.label_is_moving,
            RefreshButton(self.obj()),
        )
        self.init_status()

    def update_status(self):
        super().update_status()
        status = self.obj().status()
        self.label_slide_position.setText(f"slide_position: {status.slide_position}")
        self.label_is_calibratedn.setText(f"is_calibrated: {status.is_calibrated}")
        self.label_is_grouped.setText(f"is_grouped: {status.is_grouped}")
        self.label_is_moving.setText(f"is_moving: {status.is_moving}")
