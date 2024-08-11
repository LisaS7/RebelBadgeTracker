import plotly.graph_objects as go
from .filters import adjust_colour


def sections_chart(badges):

    colours = []
    for badge in badges:
        if badge.complete:
            colours.append(badge.colour)
        else:
            darker = adjust_colour(badge.colour, 0.5)
            colours.append(darker)

    fig = go.Figure(
        data=[
            go.Pie(
                labels=[badge.name for badge in badges],
                values=[1 for badge in badges],
                pull=[0.2 for badge in badges],
                title="Completed badges",
                textinfo="none",
            )
        ]
    )

    fig.update_traces(hole=0.5, marker_colors=colours)
    fig.update_layout(
        font_color="white",
        showlegend=False,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(l=20, r=20, t=20, b=50),
    )

    return fig.to_html()
