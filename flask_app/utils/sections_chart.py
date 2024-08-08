import plotly.graph_objects as go
from plotly.offline import plot

colours = ['#80659c', "#0da96f", "#af3752", "#0c618d", "#e66310", "#c6ca51"]

def make_sections_chart():
    labels = ["Creative", "Wellness", "Self Aware", "Global", "Wild", "Grown Up"]
    values = [1, 1, 1, 1, 1, 1]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1], insidetextorientation='tangential', rotation=30)])

    fig.update_traces(hole=0.5, textinfo='label', marker=dict(colors=colours))
    fig.update_layout(showlegend=False, plot_bgcolor= 'rgba(0, 0, 0, 0)', paper_bgcolor= 'rgba(0, 0, 0, 0)', font_family="Bradley Hand, cursive", font_size=18)
    
    return fig.to_html()