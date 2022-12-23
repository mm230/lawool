from flask import Flask, render_template, request

import networkx as nx

import cities_graph as G


app = Flask(__name__)

Graph = G.buildGraph()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def distance():
    source_a = request.form['source']
    target_b = request.form['target']

    road_to = nx.dijkstra_path(Graph, source_a, target_b)

    
    path_length = round(nx.dijkstra_path_length(Graph, source_a, target_b), 2)
  

    return render_template("after.html", data =[source_a, target_b, road_to, path_length])



if __name__ == "__main__":
    app.run(debug=True)
