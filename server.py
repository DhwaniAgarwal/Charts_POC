import os
from flask import Flask
from flask import Response
import numpy as np
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import utilities
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
@app.route('/')
def hello():
    return "Hello World!"

# Returns a sample plot as image
@app.route('/print-plot')
def plot_png():
   fig = Figure()
   axis = fig.add_subplot(1, 1, 1)
   xs = np.random.rand(100)
   ys = np.random.rand(100)
   axis.plot(xs, ys)
   output = io.BytesIO()
   FigureCanvas(fig).print_png(output)
   return Response(output.getvalue(), mimetype='image/png')

# Returns a countplot as image in the response body on the sample dataset generated with the help of utility functions 
@app.route('/print-count-plot')
def printCountPlot():
   df = utilities.generate_dataset()
   print("df created successfully")
   fig = plt.figure()
   sns.countplot(x = 'Liquid', data = df, order = ['Skim Milk', 'Nitric Acid', 'Water', 'Motor Oil'])
   plt.xticks(rotation=45)
   plt.yticks(rotation=45)
   plt.tight_layout()
   output = io.BytesIO()
   FigureCanvas(fig).print_png(output)
   return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)