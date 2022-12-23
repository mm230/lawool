import networkx as nx



weighted_cities = [('Rufisque', 'Pikine', 19.6), ('Rufisque', 'Keur Massar', 11.9), ('Dakar', 'Guediawaye', 21.6),
                           ('Pikine', 'Guediawaye', 2.8), ('Guediawaye', 'Keur Massar', 13.1), ('Pikine', 'Dakar', 19.1),
                           ('Rufisque', 'Dakar', 33.8),
                           ('Diourbel', 'Gossas', 27.5), ('Diourbel', 'Bambey', 25.1), ('Diourbel', 'Mbacke', 40.7),
                           ('Bambey', 'Thies', 65.1), ('Thies', 'Tivaouane', 24.2), ('Thies', 'Mbour', 52.8),
                           ('Rufisque', 'Mbour', 53.6), 
                           ('Thies', 'Tivaouane', 24.2), ('Thies', 'Rufisque', 42.6), ('Louga', 'Dahra', 88.3),
                           ('Mbacke', 'Dahra', 80.7),  ('Mbacke', 'Kebemer', 101),  ('Kebemer', 'Louga', 37.7),
                           ('Kebemer', 'Tivaouane', 62.9),  ('Louga', 'Saint-Louis', 73.7),  ('Podor', 'Dagana', 78.7),
                           ('Matam', 'Dagana', 282),
                           ('Saint-Louis', 'Richard-Toll', 106),  ('Richard-Toll', 'Dagana', 22.9), ('Podor', 'Matam', 230),
                           ('Matam', 'Kanel', 24), ('Matam', 'Ranerou', 83.3), ('Kanel', 'Bakel', 124), ('Matam', 'Tambacounda' , 232),
                           ('Linguere', 'Ranerou' , 132), ('Dahra', 'Linguere', 42.2),('Kaolack', 'Nioro', 58.9), 
                           ('Kaolack', 'Guinguineo', 26.6), ('Kaolack', 'Birkelane', 41.3), 
                           ('Kaolack', 'Fatick', 45.2), ('Kaolack', 'Foundiougne', 66.4), ('Kaolack', 'Gossas', 38.4),
                           ('Kaolack', 'Banjul', 120), ('Nioro', 'Farafenni', 29.4),('Farafenni', 'Soma', 16.6),
                           ('Soma', 'Bounkiling', 54.3), ('Bounkiling', 'Kolda', 107), ('Bounkiling', 'Bignona', 69.2),
                           ('Fatick', 'Bambey', 42.2), ('Fatick', 'Foundiougne', 27.2), ('Fatick', 'Gossas', 49.4), 
                           ('Fatick', 'Mbour', 64.6),('Kaffrine', 'Birkelane', 23.6), ('Kaffrine', 'Malem Hodar', 31.5), 
                           ('Kaffrine', 'Koungheul', 85.6), 
                           ('Kaffrine', 'Mbacke', 108), ('Kaffrine', 'Gossas', 96.9), ('Koungheul', 'Koumpentoum', 27.2),
                           ('Tambacounda', 'Koumpentoum', 102), ('Tambacounda', 'Goudiry', 115), ('Goudiry', 'Bakel', 136),
                           ('Tambacounda', 'Kedougou', 234), ('Kedougou', 'Salemata', 78.8), ('Kedougou', 'Saraya', 59.8),
                           ('Tambacounda', 'Velingara', 96),('Kolda', 'Velingara', 131), ('Kolda', 'Medina Yoro Foulah', 98), 
                           ('Kolda', 'Sedhiou', 88.5),
                           ('Kolda', 'Goudomp', 149), ('Sedhiou','Bounkiling', 50.4), ('Sedhiou','Bignona', 85.6),
                           ('Ziguinchor','Bignona', 33.4), ('Ziguinchor','Oussouye', 43.8), ('Ziguinchor','Goudomp', 35),
                           ('Banjul','Bignona', 119)
                           ]

def buildGraph():
    G=nx.Graph()
    # G.add_nodes_from(cities)
    G.add_weighted_edges_from(weighted_cities)
    return G