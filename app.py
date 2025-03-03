from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the BENi AI Nutritional Tracker App!"

if __name__ == '__main__':
    app.run(debug=True)
