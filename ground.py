import cairo


# Create the surface and context
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)  #white
context.rectangle(0, 0, width, height)  
context.fill()

# Lawn color (RGB)
lawn_color = (0.3, 0.8, 0.3)  # Green

#ground structure
context.set_source_rgb(*lawn_color)  # Set lawn color
context.move_to(70,158)
context.line_to(40, 170)
context.line_to(140, 200)
context.line_to(240, 150)
context.line_to(190,135)
context.close_path()  # Close the shape
context.fill()  # Fill the shape with the lawn color

context.move_to(40,170)
context.line_to(40,180)
context.line_to(140,210)
context.line_to(240,160)
context.line_to(240,150)

context.move_to(140,200)
context.line_to(140,210)

context.set_source_rgb(0,0,0)
context.set_line_width(0.8)
context.stroke()

surface.write_to_png("ground.png")