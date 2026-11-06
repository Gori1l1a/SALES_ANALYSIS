import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

sky = patches.Rectangle((0, 0), 10, 10, facecolor='lightblue')
ax.add_patch(sky)

ground = patches.Rectangle((0, 0), 10, 3, facecolor='green')
ax.add_patch(ground)

sun = patches.Circle((8, 8), radius=1, facecolor='yellow')
ax.add_patch(sun)

cloud1 = patches.Ellipse((2, 8.5), width=1.5, height=0.8, facecolor='white')
cloud2 = patches.Ellipse((3, 8.5), width=1.5, height=0.8, facecolor='white')
ax.add_patch(cloud1)
ax.add_patch(cloud2)

house = patches.Rectangle((3, 3), 4, 3, facecolor='tan')
ax.add_patch(house)

roof = patches.Polygon([[2.5, 6], [7.5, 6], [5, 8.5]], closed=True, facecolor='brown')
ax.add_patch(roof)

door = patches.Rectangle((4.5, 3), 1, 1.8, facecolor='saddlebrown')
ax.add_patch(door)

window = patches.Rectangle((5.8, 4.2), 0.8, 0.8, facecolor='white')
ax.add_patch(window)

tree_trunk = patches.Rectangle((1.2, 3), 0.5, 1.5, facecolor='brown')
tree_crown = patches.Circle((1.45, 5), radius=0.8, facecolor='darkgreen')
ax.add_patch(tree_trunk)
ax.add_patch(tree_crown)

plt.tight_layout()
plt.savefig('part1_matplotlib/img/task3.png', bbox_inches='tight')
plt.show()