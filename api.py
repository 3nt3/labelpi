from flask import Flask, request, render_template
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

    # return template
    return render_template('/index.html')


if __name__ == '__main__':
    app.run()
