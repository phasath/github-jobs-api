from flask import Flask

from app.server import application

def test_app_creation():
    assert isinstance(application, Flask)
    