def on_button_pressed_a():
    OLED.clear()
    if Master >= 18 and Master <= 20:
        basic.show_icon(IconNames.HAPPY)
    elif False:
        if Master < 18:
            basic.show_string("C")
    elif Master > 20:
        basic.show_string("H")
    radio.send_string("ping")
    basic.pause(5000)
    if Lounge > 0 and Kitchen > 0 and Hall_Upper > 0 and Hall_Lower > 0:
        OLED.write_string_new_line("Master : " + convert_to_text(Master))
        OLED.new_line()
        OLED.write_string_new_line("Hall U : " + convert_to_text(Hall_Upper))
        OLED.new_line()
        OLED.write_string_new_line("Hall L : " + convert_to_text(Hall_Lower))
        OLED.new_line()
        OLED.write_string_new_line("Kitchen : " + convert_to_text(Kitchen))
        OLED.write_string_new_line("Lounge : " + convert_to_text(Lounge))
    else:
        OLED.write_string_new_line("Master : " + convert_to_text(Master))
        OLED.new_line()
        OLED.write_string_new_line("Hall U : " + "NA")
        OLED.new_line()
        OLED.write_string_new_line("Hall L : " + "NA")
        OLED.new_line()
        OLED.write_string_new_line("Kitchen : " + "NA")
        OLED.write_string_new_line("Lounge : " + "NA")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_value(name, value):
    global Lounge, Kitchen, Hall_Lower, Hall_Upper
    if name == "l":
        Lounge = value
    if name == "k":
        Kitchen = value
    if name == "hl":
        Hall_Lower = value
    if name == "hu":
        Hall_Upper = value
radio.on_received_value(on_received_value)

Hall_Lower = 0
Hall_Upper = 0
Kitchen = 0
Lounge = 0
Master = 0
radio.set_group(6)
Master = input.temperature()
Lounge = 0
Kitchen = 0
Hall_Upper = 0
Hall_Lower = 0
OLED.init(128, 64)