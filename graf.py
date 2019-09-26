import bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, output_file, show

# Outuput
output_file("Bokeh-Grafico-Circulos.html")

p = figure(plot_width = 400, plot_height = 400)

# Adicionando círculos ao gráfico
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size = 20, color = "navy", alpha = 0.5)

# Mostrando o resultado
show(p)
