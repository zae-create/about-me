import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges for the sports tutorial web
G.add_edges_from([
    ("Sports Tutorials", "Types of Sports"),
    ("Types of Sports", "Team Sports"),
    ("Types of Sports", "Individual Sports"),
    ("Team Sports", "Soccer"),
    ("Team Sports", "Basketball"),
    ("Individual Sports", "Tennis"),
    ("Individual Sports", "Swimming"),
    ("Sports Tutorials", "Training Techniques"),
    ("Training Techniques", "Strength Training"),
    ("Training Techniques", "Endurance Training"),
    ("Sports Tutorials", "Skill Development"),
    ("Skill Development", "Dribbling"),
    ("Skill Development", "Shooting"),
    ("Sports Tutorials", "Nutrition & Recovery"),
    ("Nutrition & Recovery", "Meal Planning"),
    ("Nutrition & Recovery", "Hydration"),
    ("Sports Tutorials", "Mental Preparation"),
    ("Mental Preparation", "Visualization"),
    ("Mental Preparation", "Focus Techniques")
])

# Create a layout for the graph
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)

# Set title
plt.title("Sports Tutorial Web")

# Show the plot
plt.axis('off')  # Hide the axes
plt.show()
