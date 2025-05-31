import subprocess
import os
from flask import Flask, request

app = Flask(__name__)
commands_dict = {
    "hello": ["echo", "Hello World!"],
    "goodbye": ["echo", "Goodbye!", "exit"],
}