def on_forever():
    while input.button_is_pressed(Button.A):
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.NORTH_WEST)
basic.forever(on_forever)
