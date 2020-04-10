#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Testing pythonsimpleGUI."""

import PySimpleGUI as sg


class TelaPython():
    """Docstring for TelaPython."""

    def __init__(self):
        """Docstring of the constructot methods."""
        # Setting the theme for application
        sg.change_look_and_feel('Black')
        # Layout
        layout = [
            [sg.Text("Type a binary with 8 digits.")],
            [sg.Input(size=(8,0), key='binary')],
            [sg.Button("Convert")],
            [sg.Output(size=(30, 20))],
            [sg.Cancel()]
        ]
        # Window
        self.window = sg.Window("Bin2Dec").layout(layout)
        # Get data from Window
        #self.button, self.values = self.window.Read()

    def iniciar(self):
        """For start and print values."""
        while True:
            self.button, self.values = self.window.Read()
            binary = self.values['binary']
            print(
                f"""Binary: {binary}  Decimal: XXX """
             )
            self.window.close()


screen = TelaPython()
screen.iniciar()

