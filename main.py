from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        self.expression = ""

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = TextInput(
            text="",
            font_size=40,
            readonly=True,
            halign="right",
            multiline=False
        )

        root.add_widget(self.display)

        buttons = GridLayout(
            cols=4,
            spacing=8
        )

        keys = [
            "AC", "⌫", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=", ""
        ]

        for key in keys:
            button = Button(
                text=key,
                font_size=26
            )

            if key:
                button.bind(
                    on_press=lambda btn, k=key:
                    self.button_pressed(k)
                )

            buttons.add_widget(button)

        root.add_widget(buttons)

        return root

    def button_pressed(self, key):

        if key == "AC":
            self.expression = ""

        elif key == "⌫":
            self.expression = self.expression[:-1]

        elif key == "=":
            try:
                expression = self.expression.replace("×", "*")
                expression = expression.replace("÷", "/")
                self.expression = str(eval(expression))
            except:
                self.expression = "Error"

        elif key == "%":
            try:
                self.expression = str(
                    float(self.expression) / 100
                )
            except:
                self.expression = "Error"

        else:
            if self.expression == "Error":
                self.expression = ""

            self.expression += key

        self.display.text = self.expression


if __name__ == "__main__":
    CalculatorApp().run()
