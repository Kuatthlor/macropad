import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

col = digitalio.DigitalInOut(board.GP15)
row = digitalio.DigitalInOut(board.GP16)

col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()

