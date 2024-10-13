from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
import typst
import tempfile

def print_label(text, preformatted=False):
    printer_model = 'QL-800'
    printer_backend = 'linux_kernel'
    printer_address = '/dev/usb/lp0'

    label_size = '62'

    qlr = BrotherQLRaster(printer_model)

    tmp_png = tempfile.NamedTemporaryFile(mode="w+")

    # Create temporary copy of label.typ and add variable
    with open("label.typ", "r") as f:
        template = f.read()

        # construct temporary file with populated variable
        tmp = tempfile.NamedTemporaryFile(mode="w+")

        # preformatted text by enclosing in brackets (typst content syntax)
        if preformatted:
            tmp.write(f"#let LABEL_TEXT = [{text}]\n" + template)
        else:
            tmp.write(f"#let LABEL_TEXT = [*{text}*]\n" + template)
        tmp.seek(0)

        typst.compile(tmp.name, output=tmp_png.name, format="png", ppi=600)

    # Convert the image to the correct format and print
    convert(qlr, [tmp_png.name], label_size, cut=True, red=True, dither=True)

    # Send the label to the printer
    send(instructions=qlr.data, printer_identifier=printer_address, backend_identifier=printer_backend)

    print("Label sent to the printer.")


def print_image(image):
    printer_model = 'QL-800'
    printer_backend = 'linux_kernel'
    printer_address = '/dev/usb/lp0'

    label_size = '62'

    qlr = BrotherQLRaster(printer_model)

    # Convert the image to the correct format and print
    convert(qlr, [image], label_size, cut=True, red=True, dither=True)

    # Send the label to the printer
    send(instructions=qlr.data, printer_identifier=printer_address, backend_identifier=printer_backend)

    print("Label sent to the printer.")
