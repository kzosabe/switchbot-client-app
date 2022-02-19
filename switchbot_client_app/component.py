from typing import Callable

from PySide6 import QtCore, QtWidgets
from switchbot_client.devices import SwitchBotCommandResult, SwitchBotDevice

from switchbot_client_app.object import DeviceStatusObject


def gen_command_button(
    callback: Callable[[], SwitchBotCommandResult], command_name: str, status: DeviceStatusObject
):
    button = QtWidgets.QPushButton(f"{command_name}")

    def click():
        exec_command_and_update(callback, status)

    button.clicked.connect(click)
    return button


def gen_turn_on_off_area(device: SwitchBotDevice, status: DeviceStatusObject):
    layout = QtWidgets.QHBoxLayout()

    def turn_on():
        response: SwitchBotCommandResult = device.turn_on()
        return response

    def turn_off():
        response: SwitchBotCommandResult = device.turn_off()
        return response

    layout.addWidget(gen_command_button(turn_on, "on", status))
    layout.addWidget(gen_command_button(turn_off, "off", status))
    box = QtWidgets.QGroupBox()
    box.setLayout(layout)
    return box


def gen_label(label_str: str = ""):
    label = QtWidgets.QLabel()
    label.setText(label_str)
    label.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
    return label


def gen_button(
    device: SwitchBotDevice, callback: Callable[[SwitchBotDevice], None], command_name: str
):
    button = QtWidgets.QPushButton(f"{command_name}")

    def click():
        callback(device)

    button.clicked.connect(click)
    return button


def gen_slider(
    device: SwitchBotDevice,
    min_value: int,
    max_value: int,
    callback: Callable[[SwitchBotDevice, int], SwitchBotCommandResult],
    status: DeviceStatusObject,
):
    slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
    slider.setRange(min_value, max_value)
    slider.setSingleStep(1)

    def value_changed():
        exec_command_and_update(lambda: callback(device, slider.value()), status)

    slider.sliderReleased.connect(value_changed)
    return slider


def gen_color_slider(
    device: SwitchBotDevice,
    callback: Callable[[SwitchBotDevice, int, int, int], SwitchBotCommandResult],
    status: DeviceStatusObject,
):
    r_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
    r_slider.setRange(0, 255)
    r_slider.setSingleStep(1)
    g_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
    g_slider.setRange(0, 255)
    g_slider.setSingleStep(1)
    b_slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
    b_slider.setRange(0, 255)
    b_slider.setSingleStep(1)

    def value_changed():
        exec_command_and_update(
            lambda: callback(device, r_slider.value(), g_slider.value(), b_slider.value()), status
        )

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(r_slider)
    layout.addWidget(g_slider)
    layout.addWidget(b_slider)
    r_slider.sliderReleased.connect(value_changed)
    g_slider.sliderReleased.connect(value_changed)
    b_slider.sliderReleased.connect(value_changed)
    box = QtWidgets.QGroupBox()
    box.setLayout(layout)
    return box


def exec_command_and_update(
    callback: Callable[[], SwitchBotCommandResult], status: DeviceStatusObject
):
    response = callback()
    if response.status_code == 100:
        status.update()