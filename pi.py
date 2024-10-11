import datetime
import api

from gpiozero import Button
from signal import pause
from printing import print_label


def get_date_string() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")


button_pins = [27, 22, 24, 23]
button_texts = ["Leo", "Nia", "Tim", get_date_string]


def return_text_or_evaluated_function(text_or_function):
    if callable(text_or_function):
        return text_or_function()
    else:
        return text_or_function


def main():
    buttons = [Button(pin, pull_up=False) for pin in button_pins]

    for i, _ in enumerate(buttons):
        print(f"linking button {i} to text {button_texts[i]}")
        buttons[i].when_pressed = lambda i0 = i: print_label(return_text_or_evaluated_function(button_texts[i0]))

    api.app.run(host='0.0.0.0', port=80)
    pause()


main()
