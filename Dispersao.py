from bokeh.io import show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Número de manutenções por dia")
p.xaxis.axis_label = 'Dias da semana'
p.yaxis.axis_label = 'Número de manutenções'
p.circle(flowers["petal_length"], flowers["petal_width"], color=colors, fill_alpha=0.2, size=10)

show(p)