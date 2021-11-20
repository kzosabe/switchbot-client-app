from typing import Callable

from PySide6 import QtCore, QtWidgets
from switchbot_client.devices import (
    AirConditioner,
    Bot,
    ColorBulb,
    ContactSensor,
    Curtain,
    Humidifier,
    Light,
    Meter,
    MotionSensor,
    Plug,
    SmartFan,
    SwitchBotDevice,
)


def gen_section(parent: QtWidgets.QWidget, layout: QtWidgets.QVBoxLayout, device: SwitchBotDevice):
    if isinstance(device, Bot):
        status = device.status()
        layout.addWidget(gen_label(parent, f"power: {status.power}"))
        layout.addWidget(gen_turn_on_off_area(device))
        layout.addWidget(gen_button(device, lambda d: d.press(), "press"))
    elif isinstance(device, Plug):
        status = device.status()
        layout.addWidget(gen_label(parent, f"power: {status.power}"))
        layout.addWidget(gen_turn_on_off_area(device))
    elif isinstance(device, Curtain):
        status = device.status()
        layout.addWidget(gen_turn_on_off_area(device))
        layout.addWidget(gen_label(parent, f"slide_position: {status.slide_position}"))
        layout.addWidget(gen_slider(device, 1, 100, lambda d, value: d.set_position(value)))
        layout.addWidget(gen_label(parent, f"is_calibrated: {status.is_calibrated}"))
        layout.addWidget(gen_label(parent, f"is_grouped: {status.is_grouped}"))
        layout.addWidget(gen_label(parent, f"is_moving: {status.is_moving}"))
    elif isinstance(device, Meter):
        status = device.status()
        layout.addWidget(gen_label(parent, f"temperature: {status.temperature}"))
        layout.addWidget(gen_label(parent, f"humidity: {status.humidity}"))
    elif isinstance(device, MotionSensor):
        status = device.status()
        layout.addWidget(gen_label(parent, f"brightness: {status.brightness}"))
        layout.addWidget(gen_label(parent, f"is_move_detected: {status.is_move_detected}"))
    elif isinstance(device, ContactSensor):
        status = device.status()
        layout.addWidget(gen_label(parent, f"brightness: {status.brightness}"))
        layout.addWidget(gen_label(parent, f"open_state: {status.open_state}"))
        layout.addWidget(gen_label(parent, f"is_move_detected: {status.is_move_detected}"))
    elif isinstance(device, ColorBulb):
        status = device.status()
        layout.addWidget(gen_label(parent, f"power: {status.power}"))
        layout.addWidget(gen_turn_on_off_area(device))
        layout.addWidget(gen_label(parent, f"brightness: {status.brightness}"))
        layout.addWidget(gen_slider(device, 1, 100, lambda d, value: d.set_brightness(value)))
        layout.addWidget(gen_label(parent, f"color_hex: {status.color_hex}"))
        layout.addWidget(
            gen_color_slider(device, lambda d, r, g, b: d.set_color_by_number(r, g, b))
        )
        layout.addWidget(gen_label(parent, f"color_temperature: {status.color_temperature}"))
        layout.addWidget(
            gen_slider(device, 2700, 6500, lambda d, value: d.set_color_temperature(value))
        )
    elif isinstance(device, Humidifier):
        status = device.status()
        layout.addWidget(gen_label(parent, f"power: {status.power}"))
        layout.addWidget(gen_label(parent, f"temperature: {status.temperature}"))
        layout.addWidget(gen_label(parent, f"humidity: {status.humidity}"))
        layout.addWidget(
            gen_label(parent, f"atomization_efficiency: {status.atomization_efficiency}")
        )
        layout.addWidget(gen_label(parent, f"is_auto: {status.is_auto}"))
        layout.addWidget(gen_label(parent, f"is_child_lock: {status.is_child_lock}"))
        layout.addWidget(gen_label(parent, f"is_muted: {status.is_muted}"))
        layout.addWidget(gen_label(parent, f"is_lack_water: {status.is_lack_water}"))
        layout.addWidget(gen_turn_on_off_area(device))
        layout.addWidget(gen_button(device, lambda d: d.set_mode(), "set_mode"))
        layout.addWidget(
            gen_button(
                device, lambda d: d.set_atomization_efficiency(), "set_atomization_efficiency"
            )
        )
        layout.addWidget(gen_button(device, lambda d: d.set_auto_mode(), "set_auto_mode"))
    elif isinstance(device, SmartFan):
        status = device.status()
        layout.addWidget(gen_turn_on_off_area(device))
        layout.addWidget(gen_label(parent, f"mode: {status.mode}"))
        layout.addWidget(gen_button(device, lambda d: d.set_fan_mode(), "set_fan_mode"))
        layout.addWidget(gen_label(parent, f"speed: {status.speed}"))
        layout.addWidget(gen_button(device, lambda d: d.set_fan_speed(), "set_fan_speed"))
        layout.addWidget(gen_label(parent, f"shake_range: {status.shake_range}"))
        layout.addWidget(gen_slider(device, 0, 120, lambda d, value: d.set_shake_range(value)))
        layout.addWidget(gen_label(parent, f"shake_center: {status. shake_center}"))
        layout.addWidget(gen_label(parent, f"is_shaking: {status.is_shaking}"))

    elif isinstance(device, Light):
        layout.addWidget(gen_turn_on_off_area(device))
    elif isinstance(device, AirConditioner):
        layout.addWidget(gen_turn_on_off_area(device))
    else:
        return None

    box = QtWidgets.QGroupBox(title=device.device_name)
    box.setLayout(layout)
    return box


def gen_label(parent: QtWidgets.QWidget, label_str: str):
    label = QtWidgets.QLabel(parent)
    label.setText(label_str)
    label.setAlignment(QtCore.Qt.AlignCenter)
    return label


def gen_button(
    device: SwitchBotDevice, callback: Callable[[SwitchBotDevice], None], command_name: str
):
    button = QtWidgets.QPushButton(f"{device.device_name} - {command_name}")

    def click():
        callback(device)

    button.clicked.connect(click)
    return button


def gen_slider(
    device: SwitchBotDevice,
    min_value: int,
    max_value: int,
    callback: Callable[[SwitchBotDevice, int], None],
):
    slider = QtWidgets.QSlider(orientation=QtCore.Qt.Orientation.Horizontal)
    slider.setRange(min_value, max_value)
    slider.setSingleStep(1)

    def value_changed():
        callback(device, slider.value())

    slider.sliderReleased.connect(value_changed)
    return slider


def gen_color_slider(
    device: SwitchBotDevice, callback: Callable[[SwitchBotDevice, int, int, int], None]
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
        callback(device, r_slider.value(), g_slider.value(), b_slider.value())

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


def gen_turn_on_off_area(device: SwitchBotDevice):
    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(gen_button(device, lambda d: d.turn_on(), "on"))
    layout.addWidget(gen_button(device, lambda d: d.turn_off(), "off"))
    box = QtWidgets.QGroupBox()
    box.setLayout(layout)
    return box
