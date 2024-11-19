import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 1000, 1000

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

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

surface.write_to_png("walls.png")
print("House drawing saved to '2D_house.png'.")