"""
WSGI config for PythonAnywhere deployment
"""
import sys
import os

# PythonAnywhere path'lerini ekle
path = '/home/KULLANICI_ADINIZ/kamu_web'
if path not in sys.path:
    sys.path.append(path)

# Environment variables
os.environ['MAIL_USERNAME'] = 'your-email@gmail.com'  # Gmail adresinizi buraya
os.environ['MAIL_PASSWORD'] = 'your-app-password'      # Gmail app password

from app import app as application
