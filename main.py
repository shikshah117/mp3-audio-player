led.enable(False)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P3, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P4, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P5, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P6, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P7, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_UP)
makerbit.connect_serial_mp3(DigitalPin.P13, DigitalPin.P14)
makerbit.set_mp3_volume(30)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P2) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P3) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P4) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P5) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P6) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P7) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
    if pins.digital_read_pin(DigitalPin.P8) == 0:
        makerbit.play_mp3_track_from_folder(1, 1, Mp3Repeat.NO)
basic.forever(on_forever)
