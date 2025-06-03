import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

def execute_bash():
    try:
        # ... your current code here ... 
    except subprocess.CalledProcessError as e:  # or other exception types, depending on what might go wrong
        print(f"Error executing command: {e}")
        return "Command not recognized"