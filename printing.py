from brother_label import BrotherLabel
import typst
import tempfile

def print_label(text, preformatted=False):
    printer_model = 'QL-800'
    printer_backend = 'linux_kernel'
    printer_address = '/dev/usb/lp0'

    label_size = '62'

    brother_label = BrotherLabel(device=printer_model, target=printer_address, backend=printer_backend)

    tmp_png = tempfile.NamedTemporaryFile(mode="w+")

    # Create temporary copy of label.typ and add variable
    with open("label.typ", "r") as f:
        template = f.read()

        # construct temporary file with populated variable
        tmp = tempfile.NamedTemporaryFile(mode="w+")

        tmp.write(f"#let LABEL_TEXT = [{text}]\n" + template)
        tmp.seek(0)

        typst.compile(tmp.name, output=tmp_png.name, format="png", ppi=600)

    brother_label.print(label_size, [tmp_png.name], cut=True, red=True, dither=True)

    print("Label sent to the printer.")


def print_image(image):
    printer_model = 'QL-800'
    printer_backend = 'linux_kernel'
    printer_address = '/dev/usb/lp0'

    label_size = '62'

    brother_label = BrotherLabel(device=printer_model, target=printer_address, backend=printer_backend)

    brother_label.print(label_size, [image])

    print("Label sent to the printer.")
