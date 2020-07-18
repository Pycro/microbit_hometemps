input.onButtonPressed(Button.A, function () {
    Master = input.temperature()
    Lounge = 0
    Kitchen = 0
    Hall_Upper = 0
    Hall_Lower = 0
    OLED.clear()
    if (Master >= 18 && Master <= 20) {
        basic.showIcon(IconNames.Happy)
    } else if (false) {
        if (Master < 18) {
            basic.showString("C")
        }
    } else if (Master > 20) {
        basic.showString("H")
    }
    radio.sendValue("ping", 0)
    basic.pause(5000)
    OLED.writeStringNewLine("Master : " + convertToText(Master))
    OLED.newLine()
    OLED.writeStringNewLine("Hall U : " + convertToText(Hall_Upper))
    OLED.newLine()
    OLED.writeStringNewLine("Hall L : " + convertToText(Hall_Lower))
    OLED.newLine()
    OLED.writeStringNewLine("Kitchen : " + convertToText(Kitchen))
    OLED.writeStringNewLine("Lounge : " + convertToText(Lounge))
})
radio.onReceivedValue(function (name, value) {
    if (name == "l") {
        Lounge = value
    }
    if (name == "k") {
        Kitchen = value
    }
    if (name == "hl") {
        Hall_Lower = value
    }
    if (name == "hu") {
        Hall_Upper = value
    }
})
let Hall_Lower = 0
let Hall_Upper = 0
let Kitchen = 0
let Lounge = 0
let Master = 0
radio.setGroup(6)
OLED.init(128, 64)
