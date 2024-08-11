import plotly.graph_objects as go
from plotly.offline import plot

colours = ["#80659c", "#0da96f", "#af3752", "#0c618d", "#e66310", "#c6ca51"]


def make_sections_chart(badges):

    fig = go.Figure(
        data=[
            go.Pie(
                labels=[badge.name for badge in badges],
                values=[1 for badge in badges],
                pull=[0.2 for badge in badges],
                textinfo="none",
            )
        ]
    )

    fig.update_traces(hole=0.5, marker_colors=[badge.colour for badge in badges])
    fig.update_layout(
        showlegend=False,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    return fig.to_html()
