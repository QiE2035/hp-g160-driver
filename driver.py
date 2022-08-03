from enum import Enum as __Enum


class Key(__Enum):
    LEFT = 0x1
    RIGHT = 0x3
    MIDDLE = 0x2
    SIDE_UP = 0x5
    SIDE_DOWN = 0x4
    MID_UP = 0x8
    MID_DOWN = 0x6


class Breath(__Enum):
    SLOW = 0x10
    QUICK = 0x13
    FIXED = 0x16
    CLOSE = 0x17

    @staticmethod
    def from_index(index):
        for i, item in enumerate(Breath):
            if(i == index):
                return item


class Driver:
    def __init__(self):
        import usb
        from usb.core import Device

        dev: Device = usb.core.find(
            idVendor=0x18F8, idProduct=0x1286)
        if(dev.is_kernel_driver_active(1)):
            dev.detach_kernel_driver(1)
        self.__dev = dev

    def __send_command(self, command):
        # print([hex(i) for i in command])
        self.__dev.ctrl_transfer(
            0x21, 0x9, 0x307, 0x1,
            [0x7] + command + [0x0] * 3)

    def set_key(self, key: Key, key_code):
        self.__send_command(
            [0x10, key.value, key_code, 0x0])

    def set_dpi(self, current, index, value):
        self.__send_command(
            [0x9, 0x40 + current - 1,
             [0x8, 0x9, 0xA, 0xB][index - 1]
             + 0x10 * value, 0xF])

    def set_scroll(self, is_scroll):
        self.__send_command(
            [0x11, 0 if is_scroll else 1]
            + [0x0] * 2)

    def set_breath(self, breath: Breath):
        self.__send_command(
            [0x13, 0x7F, breath.value, 0xF])

    def set_click_speed(self, click_speed):
        self.__send_command(
            [0x12, 0x0, click_speed, 0x0])
