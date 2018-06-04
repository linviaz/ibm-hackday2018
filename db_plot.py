#!/usr/bin/env python
""" Create a plot diagram HTML file using bokeh """

from flask import Flask, render_template
from db_read import get_temp
from bokeh.plotting import figure, output_file, save

app = Flask(__name__)

def create_plot(x, y):
    """ Create a static HTML file with plot data """
    # output to static HTML file
    output_file("templates/temperature.html", title="temperature chart")

    # create a new plot with a title and axis labels
    p = figure(title="temperature chart", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    # save the results
    save(p)

@app.route('/')
def graph():
    # Plot temperature values. x = list of 0 to nr of readings. y = readings
    temp_list = get_temp()['data']
    x = list(range(len(temp_list)))
    y = temp_list
    print(x,y)

    create_plot(x, y)
    return render_template('temperature.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run('0.0.0.0', port=8080)
