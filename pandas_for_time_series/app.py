#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:47:23 2024

@author: ondul
"""

from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from yolo import YOLO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

yolo = YOLO()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    # Perform authentication here
    user = {"id": "1", "username": username}
    return jsonify(user)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Perform object detection using YOLO
        objects = yolo.detect_objects(filepath)
        return jsonify({"url": filepath, "objects": objects})

@app.route('/search', methods=['POST'])
def search_images():
    query = request.get_json()['query']
    # Search images based on query using YOLO metadata
    results = search_in_database(query)
    return jsonify(results)

def search_in_database(query):
    # Implement search logic here
    return []

if __name__ == '__main__':
    app.run(debug=True)
