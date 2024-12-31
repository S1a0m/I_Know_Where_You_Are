from flask import Blueprint, render_template, request, redirect, jsonify
from .models import VisitorIP
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/save-ip', methods=['POST'])
def save_ip():
    try:
        ip = request.json.get('ip')
        if ip:
            new_ip = VisitorIP(ip=ip)
            db.session.add(new_ip)
            db.session.commit()
            return jsonify({'message': 'IP saved successfully'}), 200
        return jsonify({'error': 'IP not provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/redirect')
def redirect_page():
    return redirect("https://https://www.google.com/search?client=firefox-b-e&q=you+have+been+hacked", code=302)  
