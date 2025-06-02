import numpy as np
import math
import ipywidgets as wd
import macti.vis as mvis

def saxpy(α, x, y, w):
#    αxpy = α * x + y
    print('\n α * x = {} \t α * x + y = {}\n'.format(α * x, α * x + y))

    v = mvis.Plotter(1, 1, [dict(aspect='equal')], fig_par = dict(figsize=(5,5)))
    v.set_coordsys()
    v.plot_vectors_sum(1, [α * x, y], ['α*x', 'y'], w = [w, w, w])
    v.grid()
    v.show()

w_x1 = wd.FloatSlider(
    min=-2.0, max=2.0, step=0.5, value=0.5,
    description='x1',
    layout=wd.Layout(width='250px')
)

w_x2 = wd.FloatSlider(
    min=-2.0, max=2.0, step=0.5, value=1.0,
    description='x2',
    layout=wd.Layout(width='250px')
)

w_y1 = wd.FloatSlider(
    min=-2.0, max=2.0, step=0.5, value=1.5,
    description='y1',
    layout=wd.Layout(width='250px')
)

w_y2 = wd.FloatSlider(
    min=-2.0, max=2.0, step=0.5, value=0.5,
    description='y2',
    layout=wd.Layout(width='250px')
)

w_a = wd.FloatSlider(
    min=-2.0, max=2.0, step=0.5, value=1.0,
    description='α',
    layout=wd.Layout(width='250px')
)

w_w = wd.FloatSlider(
    min=0.01, max=0.05, step=0.01, value=0.01,
    description='w',
    layout=wd.Layout(width='250px')
)

button = wd.Button(
    description="", icon='play',
    layout=wd.Layout(width='50px')    
)

ui = wd.VBox([wd.HBox([w_a, w_w],
                      layout=wd.Layout(padding='0px', 
                                       border='1px solid gray',
                                       width='510px')),
              wd.HBox([wd.VBox([w_x1, w_x2],
                              layout=wd.Layout(padding='0px', 
                                               border='1px solid gray',
                                               width='255px')),
                       wd.VBox([w_y1, w_y2],
                              layout=wd.Layout(padding='0px', 
                                               border='1px solid gray',
                                               width='255px')),                      
                      ]),
              wd.HBox([button])])

ui.layout = wd.Layout(border='solid 0px black')
            
output = wd.Output()

display(ui, output)

def on_button_clicked(b):
    output.clear_output(wait=True)
    with output:
        saxpy(w_a.value, np.array([w_x1.value, w_x2.value]), 
                         np.array([w_y1.value, w_y2.value]),
              w_w.value)

button.on_click(on_button_clicked)