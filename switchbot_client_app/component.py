from typing import Callable, List, Tuple, Union

from PySide6 import QtCore, QtWidgets
from switchbot_client.devices import SwitchBotCommandResult, SwitchBotDevice

from switchbot_client_app.object import DeviceStatusObject


class Slider(QtWidgets.QSlider):
    def __init__(
        self,
        device: SwitchBotDevice,
        min_value: int,
        max_value: int,
        callback: Callable[[SwitchBotDevice, int], SwitchBotCommandResult],
        status: DeviceStatusObject,
    ):
        super().__init__(orientation=QtCore.Qt.Orientation.Horizontal)
        self.setRange(min_value, max_value)
        self.setSingleStep(1)

        def value_changed():
            exec_command_and_update(lambda: callback(device, self.value()), status)

        self.sliderReleased.connect(value_changed)


class ColorSlider(QtWidgets.QGroupBox):
    def __init__(
        self,
        device: SwitchBotDevice,
        callback: Callable[[SwitchBotDevice, int, int, int], SwitchBotCommandResult],
        status: DeviceStatusObject,
    ):
        super().__init__()

        self.r_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
        self.r_slider.setRange(0, 255)
        self.r_slider.setSingleStep(1)
        self.g_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
        self.g_slider.setRange(0, 255)
        self.g_slider.setSingleStep(1)
        self.b_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
        self.b_slider.setRange(0, 255)
        self.b_slider.setSingleStep(1)

        def value_changed():
            exec_command_and_update(
                lambda: callback(
                    device, self.r_slider.value(), self.g_slider.value(), self.b_slider.value()
                ),
                status,
            )

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.r_slider)
        layout.addWidget(self.g_slider)
        layout.addWidget(self.b_slider)
        self.r_slider.sliderReleased.connect(value_changed)
        self.g_slider.sliderReleased.connect(value_changed)
        self.b_slider.sliderReleased.connect(value_changed)
        self.setLayout(layout)

    def set_value(self, color_hex: str):
        rgb = tuple(int(color_hex.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
        self.r_slider.setValue(rgb[0])
        self.g_slider.setValue(rgb[1])
        self.b_slider.setValue(rgb[2])

    def value(self):
        return [
            self.r_slider.value(),
            self.g_slider.value(),
            self.b_slider.value(),
        ]


class ComboBox(QtWidgets.QGroupBox):
    def __init__(self, label: str, items: List[Tuple[str, Union[int, str]]]):
        super().__init__()
        self.label = QtWidgets.QLabel()
        self.widget = QtWidgets.QComboBox()
        self.label.setText(label)
        for i in items:
            self.widget.addItem(i[0], i[1])
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.widget)
        self.setLayout(layout)

    def current_index_changed(self):
        return self.widget.currentIndexChanged

    def value(self):
        return self.widget.currentData()


class FloatInput(QtWidgets.QGroupBox):
    def __init__(
        self,
        label: str,
        min_value: float,
        max_value: float,
        default_value: float,
        single_step: float,
    ):
        super().__init__()
        self.label = QtWidgets.QLabel()
        self.widget = QtWidgets.QDoubleSpinBox()
        self.label.setText(label)
        self.widget.setSingleStep(single_step)
        self.widget.setDecimals(1)
        self.widget.setRange(min_value, max_value)
        self.widget.setValue(default_value)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.widget)
        self.setLayout(layout)

    def value(self) -> float:
        return self.widget.value()


class CenterLabel(QtWidgets.QLabel):
    def __init__(self, text: str):
        super().__init__()
        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore


class CommandButton(QtWidgets.QPushButton):
    def __init__(
        self, text: str, callback: Callable[[], SwitchBotCommandResult], status: DeviceStatusObject
    ):
        super().__init__(text)
        self.clicked.connect(lambda: exec_command_and_update(callback, status))


class RefreshButton(QtWidgets.QPushButton):
    def __init__(self, status: DeviceStatusObject):
        text = "refresh status"
        super().__init__(text)
        self.clicked.connect(status.update_immediately)


class Button(QtWidgets.QPushButton):
    def __init__(
        self, device: SwitchBotDevice, callback: Callable[[SwitchBotDevice], None], text: str
    ):
        super().__init__(text)

        def click():
            callback(device)

        self.clicked.connect(click)


class Label(QtWidgets.QLabel):
    def __init__(self, text: str = ""):
        super().__init__()
        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore


class TurnOnOffArea(QtWidgets.QGroupBox):
    def __init__(self, device: SwitchBotDevice, status: DeviceStatusObject):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()

        def turn_on():
            return exec_command_and_update(device.turn_on, status)

        def turn_off():
            return exec_command_and_update(device.turn_off, status)

        layout.addWidget(CommandButton("on", turn_on, status))
        layout.addWidget(CommandButton("off", turn_off, status))
        self.setLayout(layout)


def exec_command_and_update(
    callback: Callable[[], SwitchBotCommandResult], status: DeviceStatusObject
):
    response = callback()
    if response.status_code == 100:
        status.update()
    return response
