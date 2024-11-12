import os.path
import typst
import tempfile

from flask import Flask, request, render_template, send_file
from printing import print_label, print_image
from PIL import Image

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form

        if 'text' not in data:
            if 'image' not in request.files:
                return "Missing 'text' field", 400

            image = request.files['image']
            if image.filename == '':
                return "Missing 'text' field", 400

            try:
                print_image(Image.open(image))
                return render_template('/index.html', message="Label printed!!")
            except Exception as e:
                return render_template('/index.html', error=f"Error printing label: {e}")

            return "Missing 'text' field", 400

        try:
            print_label(data['text'], data.get('preformatted', False))
        except Exception as e:
            return render_template('/index.html', error=f"Error printing label: {e}")

        return render_template('/index.html', message="Label printed!!")

    # check if printer is there
    if not os.path.isfile('/dev/usb/lp0'):
        return render_template('/index.html', error="Printer not connected/turned on")

    # return template
    return render_template('/index.html')


@app.route('/preview', methods=['GET'])
def preview():
    text = request.args.get('text')

    tmp_png = tempfile.NamedTemporaryFile(mode="w+")

    # Create temporary copy of label.typ and add variable
    with open("label.typ", "r") as f:
        template = f.read()

        # construct temporary file with populated variable
        tmp = tempfile.NamedTemporaryFile(mode="w+")

        tmp.write(f"#let LABEL_TEXT = [{text}]\n" + template)
        tmp.seek(0)

        typst.compile(tmp.name, output=tmp_png.name, format="png", ppi=600)

    return send_file(tmp_png.name, mimetype='image/png')


if __name__ == '__main__':
    app.run()
