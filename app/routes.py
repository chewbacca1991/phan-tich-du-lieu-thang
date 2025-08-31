from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Xử lý tải lên dữ liệu CSV
    return redirect(url_for('index'))