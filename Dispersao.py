from bokeh.io import show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'
p.circle(flowers["petal_length"], flowers["petal_width"], color=colors, fill_alpha=0.2, size=10)

show(p)