# import dash
# import plotly.express as px

# print(dash.__version__)

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


# from dash import Dash, html

# # Create app
# app = Dash(__name__)

# # Layout with just text
# app.layout = html.Div([
#     html.H1("My First Dashboard"),
#     html.P("This is a simple Dash application with just text.")
# ])

# # Run server
# if __name__ == "__main__":
#     app.run(debug=True)  # <-- changed from run_server to run


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


# 2: Dashboard with static graph
# from dash import Dash, html, dcc
# import plotly.express as px
# import seaborn as sns

# # Load dataset
# df = sns.load_dataset("tips")

# # Create static figure
# fig = px.scatter(
#     df,
#     x="total_bill",
#     y="tip",
#     color="sex",
#     title="Total Bill vs Tip"
# )

# # Create app
# app = Dash(__name__)

# # Layout
# app.layout = html.Div([
#     html.H1("Tips Dashboard"),
#     html.P("This dashboard shows a static Plotly scatter plot."),
#     dcc.Graph(figure=fig)
# ])

# # Run server
# if __name__ == "__main__":
#     app.run(debug=True)



# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


# 3: Interactive Dashboard with Dropdown
# from dash import Dash, html, dcc, Input, Output
# import plotly.express as px
# import seaborn as sns

# # Load dataset
# df = sns.load_dataset("tips")

# # Create app
# app = Dash(__name__)

# # Layout
# app.layout = html.Div([
#     html.H1("Interactive Tips Dashboard"),
#     html.P("Select a day to filter the scatter plot."),
    
#     html.Label("Select Day:"),
#     dcc.Dropdown(
#         id="day-dropdown",
#         options=[{"label": day, "value": day} for day in df["day"].unique()],
#         value="Sun",
#         clearable=False
#     ),
    
#     dcc.Graph(id="scatter-graph")
# ])

# # Callback for interactivity
# @app.callback(
#     Output("scatter-graph", "figure"),
#     Input("day-dropdown", "value")
# )
# def update_graph(selected_day):
#     filtered_df = df[df["day"] == selected_day]
#     fig = px.scatter(
#         filtered_df,
#         x="total_bill",
#         y="tip",
#         color="sex",
#         title=f"Total Bill vs Tip on {selected_day}"
#     )
#     return fig

# # Run server
# if __name__ == "__main__":
#     app.run(debug=True)

