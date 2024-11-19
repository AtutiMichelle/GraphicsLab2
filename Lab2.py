import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 1000, 1000

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()
#Grass
context.move_to(50,600)
context.line_to(800,600)
context.line_to(900, 900)
context.line_to(100, 900)
context.close_path()
context.move_to(50,600)
context.line_to(45,550)
context.line_to(100, 800)
context.line_to(100, 850)
context.close_path()
context.set_source_rgb(0.686,0.894,0.403)
context.fill()
#left wall
context.move_to(200,200)
context.line_to(100,250)
context.line_to(100, 600)
context.line_to(300, 800)
context.line_to(300, 250)
context.close_path()
context.set_source_rgb(0.780,0.749,0.717)
context.fill()
#front wall
context.move_to(300,250)
context.line_to(800, 250)
context.line_to(800, 800)
context.line_to(300, 800)
#context.close_path()
context.set_source_rgb(0.8,0.770,0.740)
context.fill()
#window left wall
context.rectangle(130, 300, 50, 150)
context.rectangle(190, 300, 50, 150)
context.rectangle(130, 500, 50, 100)
context.rectangle(190, 500, 50, 100)
#widows and doors front wall
context.rectangle(450, 300, 100, 150)
context.rectangle(570, 300, 100, 150)
context.set_source_rgb(0.760,0.874,0.968)
context.fill()
context.rectangle(600, 570, 120, 180)
context.set_source_rgb(0.192,0.235,0.294)
context.fill()
context.rectangle(610, 572, 30, 165)
context.set_source_rgb(0.760,0.874,0.968)
context.fill()
#roof
context.move_to(200,180)
context.line_to(800,180)
context.line_to(880, 300)
context.line_to(300, 300)
context.close_path()
context.set_source_rgb(0.192,0.235,0.294)
context.fill()
surface.write_to_png("2D_house.png")
print("House drawing saved to '2D_house.png'.")
#