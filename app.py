from flask import Flask, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST"])
def image_coordinates():
    # get inputs
    m, n = request.json["dimensions"]
    corners = request.json["corners"]

    # get bounds
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    # build coordinates
    coords = []
    for y in np.linspace(ymax, ymin, m):
        # build row
        row = []
        for x in np.linspace(xmin, xmax, n):
            row.append([x, y])

        # append row
        coords.append(row)

    return coords
