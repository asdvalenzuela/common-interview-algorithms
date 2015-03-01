def flood_fill(world, x, y, old_color, new_color):
	if world[x][y] != old_color:
		return 
	world[x][y] = new_color
	if x > 0:
		flood_fill(world, x-1, y, old_color, new_color)
	if x < world.width-1:
		flood_fill(world, x+1, y, old_color, new_color)
	if y > 0:
		flood_fill(world, x, y-1, old_color, new_color)
	if y < world.height-1:
		flood_fill(world, x, y+1, old_color, new_color)

