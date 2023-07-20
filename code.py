import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.lock_status import LockStatus
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
locks = LockStatus()
keyboard.extensions.append(locks)

keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.row_pins =(board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
     KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS, KC.E,  KC.F,  KC.G,
     KC.P7,   KC.P8,   KC.P9,   KC.K,    KC.L,  KC.M,  KC.N,
     KC.P4,   KC.P5,   KC.P6,   KC.R,    KC.S,  KC.T,  KC.U,
     KC.P1,   KC.P2,   KC.P3,   KC.Y,    KC.Z,  KC.N1, KC.N2,
     KC.N3,   KC.P0,   KC.PDOT, KC.N6,   KC.N7, KC.N8, KC.N9,

    ]
]

if __name__ == '__main__':
    keyboard.go()

