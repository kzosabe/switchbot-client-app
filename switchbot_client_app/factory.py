from switchbot_client.devices import (
    AirConditioner,
    Bot,
    ColorBulb,
    ContactSensor,
    Curtain,
    Humidifier,
    Light,
    Meter,
    MeterPlusJp,
    MeterPlusUs,
    MotionSensor,
    Plug,
    PlugMiniJp,
    PlugMiniUs,
    SmartFan,
    SwitchBotDevice,
)


def gen_section(device: SwitchBotDevice):
    if isinstance(device, Bot):
        from switchbot_client_app.section.bot import BotSection

        return BotSection(device)
    if isinstance(device, (Plug, PlugMiniUs, PlugMiniJp)):
        from switchbot_client_app.section.plug import PlugSection

        return PlugSection(device)
    if isinstance(device, Curtain):
        from switchbot_client_app.section.curtain import CurtainSection

        return CurtainSection(device)
    if isinstance(device, (Meter, MeterPlusUs, MeterPlusJp)):
        from switchbot_client_app.section.meter import MeterSection

        return MeterSection(device)
    if isinstance(device, MotionSensor):
        from switchbot_client_app.section.motion_sensor import MotionSensorSection

        return MotionSensorSection(device)
    if isinstance(device, ContactSensor):
        from switchbot_client_app.section.contact_sensor import ContactSensorSection

        return ContactSensorSection(device)
    if isinstance(device, ColorBulb):
        from switchbot_client_app.section.color_bulb import ColorBulbSection

        return ColorBulbSection(device)
    if isinstance(device, Humidifier):
        from switchbot_client_app.section.humidifier import HumidifierSection

        return HumidifierSection(device)
    if isinstance(device, SmartFan):
        from switchbot_client_app.section.smart_fan import SmartFanSection

        return SmartFanSection(device)
    if isinstance(device, Light):
        from switchbot_client_app.section.light import LightSection

        return LightSection(device)
    if isinstance(device, AirConditioner):
        from switchbot_client_app.section.air_conditioner import AirConditionerSection

        return AirConditionerSection(device)
    return None
