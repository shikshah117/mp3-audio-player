input.onPinPressed(TouchPin.P0, function () {
    makerbit.playMp3TrackFromFolder(3, 3, Mp3Repeat.No)
    basic.showLeds(`
        # . . . #
        . # # # .
        . . . . .
        . # . # .
        . . # . .
        `)
})
input.onButtonPressed(Button.A, function () {
    makerbit.playMp3TrackFromFolder(9, 1, Mp3Repeat.No)
    basic.showIcon(IconNames.Happy)
})
input.onPinPressed(TouchPin.P2, function () {
    makerbit.playMp3TrackFromFolder(6, 6, Mp3Repeat.No)
    basic.showLeds(`
        # . # # .
        . # # . .
        . # # # #
        . # # # .
        . . # . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    makerbit.playMp3TrackFromFolder(4, 4, Mp3Repeat.No)
    basic.showIcon(IconNames.StickFigure)
})
input.onButtonPressed(Button.B, function () {
    makerbit.playMp3TrackFromFolder(5, 5, Mp3Repeat.No)
    basic.showIcon(IconNames.Sad)
})
input.onPinPressed(TouchPin.P1, function () {
    makerbit.playMp3TrackFromFolder(1, 1, Mp3Repeat.No)
    basic.showLeds(`
        . . . . .
        . # # . .
        # # # # .
        . # # # #
        . # # # .
        `)
})
basic.showIcon(IconNames.Heart)
makerbit.connectSerialMp3(DigitalPin.P13, DigitalPin.P14)
makerbit.setMp3Volume(30)
basic.showIcon(IconNames.Heart)
makerbit.playMp3TrackFromFolder(7, 7, Mp3Repeat.No)
