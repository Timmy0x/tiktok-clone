from flask import Flask, render_template, request, Response

import json
import csv
import requests

from videos import VideoController

app = Flask(__name__)
video_con = VideoController()

@app.route("/")
def index():
    return render_template("media.html", videos=video_con.get_feed())
@app.route("/styles/core.css")
def core_css():
    return Response(open("styles/core.css").read(), mimetype="text/css")
@app.route("/styles/media.css")
def media_css():
    return Response(open("styles/media.css").read(), mimetype="text/css")

app.run(host="0.0.0.0", port=80)