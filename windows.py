import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 1000, 1000

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

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
# Save the image
surface.write_to_png("windows.png")
