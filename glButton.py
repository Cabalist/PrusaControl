# -*- coding: utf-8 -*-
import itertools

__author__ = 'Tibor Vavra'


class GlButton(object):
    newid = itertools.count(1)

    def __init__(self, texture_off=None, texture_on=None, texture_hover=None, texture_background=None, size=None, position=None, auto_release=False, tool_tip='', tool_name='', dpi_coef=1.0):
        if size is None:
            size = [10., 10.]

        if position is None:
            position = [0.0, 0.0]

        self.id = next(self.newid) * 7013
        self.color_id = [(self.id & 0x000000FF) >> 0, (self.id & 0x0000FF00) >> 8, (self.id & 0x00FF0000) >> 16]

        self.texture_off = texture_off
        self.texture_on = texture_on
        self.texture_hover = texture_hover
        self.texture_background = texture_background

        self.size = [size[0] * dpi_coef, size[1] * dpi_coef]
        self.position = [position[0] * dpi_coef, position[1] * dpi_coef]

        self.pressed = False
        self.mouse_over = False
        self.callback_function = None
        self.press_variable = None
        self.auto_release = auto_release

        self.key = None
        self.subkey = None

        self.tool_name = tool_name
        self.tool_tip = tool_tip

    def set_callback(self, func):
        self.callback_function = func

    def mouse_is_over(self, Is):
        self.mouse_over = Is

    def press_button(self):
        if self.auto_release:
            self.pressed = False
        else:
            self.pressed = not self.pressed
        # print("Byl stisknut " + self.tool_name)
        self.callback_function()

    def unpress_button(self):
        self.pressed = False

    def set_press_variable(self, variable, key, subkey):
        self.press_variable = variable
        self.key = key
        self.subkey = subkey

    def set_viewport(self, width, height):
        self.xW = width
        self.yH = height

    def is_pressed(self):
        if self.pressed:
            return True
        else:
            return False

    def get_size(self):
        pass

    def render(self, picking=False):
        pass

    def run_callback(self):
        if self.callback_function:
            self.callback_function()

    def check_button(self, color):
        # return True if checked color is same as button color
        # else return False

        color_id = color[0] + (color[1] * 255) + (color[2] * 255 * 255)

        if color_id == self.id:
            return True
        else:
            return False
