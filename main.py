def on_button_pressed_a():
    global Conter
    Conter += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Conter
    Conter = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Conter = 0
radio.set_group(10)
strip = neopixel.create(DigitalPin.P16, 5, NeoPixelMode.RGB)

def on_forever():
    global Conter
    if Conter == 3:
        radio.send_string("I need help")
        basic.show_string("Message sent to your school counselor")
        Conter = 0
basic.forever(on_forever)

def on_forever2():
    strip.show()
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    basic.pause(100)
basic.forever(on_forever2)
