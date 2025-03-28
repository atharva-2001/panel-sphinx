import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
import numpy as np
from IPython.display import display

class PlotlyVisualization:
    def __init__(self):
        """Initialize the visualization class with empty figure widgets."""
        self.fig1 = None
        self.fig2 = None
        self.create_figures()
    
    def create_sample_data(self):
        """Generate sample data for the plots."""
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        return x, y1, y2
    
    def create_figures(self):
        """Create the FigureWidget objects."""
        x, y1, y2 = self.create_sample_data()
        
        # Create the first FigureWidget
        self.fig1 = go.FigureWidget(
            data=[go.Scatter(x=x, y=y1, mode='lines', name='sin(x)')],
            layout=go.Layout(title='Sine Wave', height=400)
        )
        
        # Create the second FigureWidget
        self.fig2 = go.FigureWidget(
            data=[go.Scatter(x=x, y=y2, mode='lines', name='cos(x)')],
            layout=go.Layout(title='Cosine Wave', height=400)
        )
    
    def display_plots(self):
        """Display both figures in a VBox layout and return the widget."""
        if self.fig1 is None or self.fig2 is None:
            self.create_figures()
            
        display(widgets.VBox([self.fig1, self.fig2]))
        # return vbox

    def display_plots_show(self):
      """Display both figures in a VBox layout and return the widget."""
      if self.fig1 is None or self.fig2 is None:
          self.create_figures()
          
      display(widgets.VBox([self.fig1.show(), self.fig2.show()]))
      # return vbox

# # Example usage:
# if __name__ == "__main__":
#     viz = PlotlyVisualization()
#     display(viz.display_plots())
