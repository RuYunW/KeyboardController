import rabird.winio
import time
import atexit

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

__winio = None


def __get_winio():
    global __winio

    if __winio is None:
        __winio = rabird.winio.WinIO()

        def __clear_winio():
            global __winio
            __winio = None

        atexit.register(__clear_winio)

    return __winio


def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
        dwRegVal = winio.get_port_byte(KBC_KEY_CMD)


def key_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)


def SPkey_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, 0xe0)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)


def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)


def SPkey_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, 0xe0)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)


def mouse_down():
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd3)
    wait_for_buffer_empty()
    winio.set_port_dword(KBC_KEY_DATA, 0x09)


def mouse_up():
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd3)
    wait_for_buffer_empty()
    winio.set_port_dword(KBC_KEY_DATA, 0x08)


def key_press(scancode, press_time=0.05):
    key_down(scancode)
    time.sleep(press_time)
    key_up(scancode)
    time.sleep(press_time)


def SPkey_press(scancode, press_time=0.05):
    SPkey_down(scancode)
    time.sleep(press_time)
    SPkey_up(scancode)
    time.sleep(press_time)


def mouse_clicked(clicked_time=0.05):
    mouse_down()
    time.sleep(clicked_time)
    mouse_up()
    time.sleep(clicked_time)

# key_press(0x1E, 0.5)
