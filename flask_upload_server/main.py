from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Укажите директорию для сохранения загруженных файлов
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('./upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Нет файла для загрузки', 400
    file = request.files['file']
    if file.filename == '':
        return 'Нет выбранного файла', 400
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return f'Файл {filename} успешно загружен', 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)