import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(LockStatus())
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(Layers())

keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.row_pins =(board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.TRNS
XXXXXXX = KC.NO

OS_CPY = KC.LCTL(KC.C)
OS_PST = KC.LCTL(KC.V)
OS_UND = KC.LCTL(KC.Z)
LAY1 = KC.MO(1)

keyboard.keymap = [
    [
     KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS, KC.MUTE, KC.VOLD, KC.VOLU,
     KC.P7,   KC.P8,   KC.P9,   KC.F13,  KC.F15,  KC.F16,  KC.F17,
     KC.P4,   KC.P5,   KC.P6,   KC.F14,  KC.F18,  KC.F19,  KC.F20,
     KC.P1,   KC.P2,   KC.P3,   KC.PPLS, KC.F21,  KC.F22,  KC.F23,
     LAY1,    KC.P0,   KC.PDOT, KC.PENT, OS_CPY,  OS_PST,  OS_UND,
    ],
    [
     KC.N1,   KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7,
     KC.A,    KC.B,  KC.C,  KC.D,  KC.E,  KC.F,  KC.G,
     KC.H,    KC.I,  KC.J,  KC.K,  KC.L,  KC.M,  KC.N,
     KC.O,    KC.P,  KC.Q,  KC.R,  KC.S,  KC.T,  KC.U,
     XXXXXXX, KC.W,  KC.X,  KC.Y,  KC.Z,  KC.N8, KC.N9,
    ]
]

if __name__ == '__main__':
    keyboard.go()
    
