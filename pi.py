import datetime
import api

from gpiozero import Button
from signal import pause
from printing import print_label


def get_datetime_string() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")

def get_date_string() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")

button_pins = [27, 22, 24, 23]
button_texts = ["Leo", "Nia", "Tim", get_date_string]
button_hold_texts = ["LeHOE", "Hure", "Timi", get_datetime_string]
buttons_were_held = [False] * len(button_pins)


def return_text_or_evaluated_function(text_or_function):
    if callable(text_or_function):
        return text_or_function()
    else:
        return text_or_function


def held(button_i, text):
    buttons_were_held[button_i] = True
    try:
        print_label(text)
    except Exception as e:
        print(f"Error while printing label: {e}")


def released(button_i, text):
    if not buttons_were_held[button_i]:
        try:
            print_label(text)
        except Exception as e:
            print(f"Error while printing label: {e}")
    buttons_were_held[button_i] = False


def main():
    buttons = [Button(pin, pull_up=False, hold_time=1) for pin in button_pins]

    for i, _ in enumerate(buttons):
        print(f"linking button {i} to text {button_texts[i]}")
        buttons_were_held[i] = False
        buttons[i].when_released = lambda i0 = i: released(i0, return_text_or_evaluated_function(button_texts[i0]))
        buttons[i].when_held = lambda i0 = i: held(i0, return_text_or_evaluated_function(button_hold_texts[i0]))

    api.app.run(host='0.0.0.0', port=80)
    pause()


main()
