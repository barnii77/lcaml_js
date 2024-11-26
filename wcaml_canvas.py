# TODO this is incomplete, should at some point be completed
@pyffi.interface(name="wcaml_canvas_get_context")
def wcaml_canvas_get_context(canvas, ctx_type):
    return canvas.getContext(ctx_type)


@pyffi.interface(name="wcaml_canvas_fill_rect")
def wcaml_canvas_fill_rect(ctx, *args):
    ctx.fillRect(*args)


@pyffi.interface(name="wcaml_canvas_stroke_rect")
def wcaml_canvas_stroke_rect(ctx, *args):
    ctx.strokeRect(*args)


@pyffi.interface(name="wcaml_canvas_clear_rect")
def wcaml_canvas_clear_rect(ctx, *args):
    ctx.clearRect(*args)


@pyffi.interface(name="wcaml_canvas_is_point_in_path")
def wcaml_canvas_is_point_in_path(ctx, *args):
    return ctx.isPointInPath(*args)


@pyffi.interface(name="wcaml_canvas_move_to")
def wcaml_canvas_move_to(ctx, *args):
    ctx.moveTo(*args)


@pyffi.interface(name="wcaml_canvas_line_to")
def wcaml_canvas_line_to(ctx, *args):
    ctx.lineTo(*args)


@pyffi.interface(name="wcaml_canvas_fill")
def wcaml_canvas_fill(ctx, *args):
    ctx.fill(*args)


@pyffi.interface(name="wcaml_canvas_rect")
def wcaml_canvas_rect(ctx, *args):
    ctx.rect(*args)


@pyffi.interface(name="wcaml_canvas_stroke")
def wcaml_canvas_stroke(ctx, *args):
    ctx.stroke(*args)


@pyffi.interface(name="wcaml_canvas_bezier_curve_to")
def wcaml_canvas_bezier_curve_to(ctx, *args):
    ctx.bezierCurveTo(*args)


@pyffi.interface(name="wcaml_canvas_arc")
def wcaml_canvas_arc(ctx, *args):
    ctx.arc(*args)


# TODO the canvas api is broken and incomplete - some things aren't functions but actually attr -> convert to getters and setters


@pyffi.interface(name="wcaml_canvas_arc_to")
def wcaml_canvas_arc_to(ctx, *args):
    ctx.arcTo(*args)


@pyffi.interface(name="wcaml_canvas_quadratic_curve_to")
def wcaml_canvas_quadratic_curve_to(ctx, *args):
    ctx.quadraticCurveTo(*args)


@pyffi.interface(name="wcaml_canvas_get_direction")
def wcaml_canvas_get_direction(ctx, *args):
    return ctx.direction


@pyffi.interface(name="wcaml_canvas_set_direction")
def wcaml_canvas_set_direction(ctx, value):
    ctx.direction = value


@pyffi.interface(name="wcaml_canvas_fill_text")
def wcaml_canvas_fill_text(ctx, *args):
    ctx.fillText(*args)


@pyffi.interface(name="wcaml_canvas_font")
def wcaml_canvas_font(ctx, *args):
    ctx.font(*args)


@pyffi.interface(name="wcaml_canvas_measure_text")
def wcaml_canvas_measure_text(ctx, *args):
    return ctx.measureText(*args)


@pyffi.interface(name="wcaml_canvas_stroke_text")
def wcaml_canvas_stroke_text(ctx, *args):
    return ctx.strokeText(*args)


@pyffi.interface(name="wcaml_canvas_text_align")
def wcaml_canvas_text_align(ctx, *args):
    return ctx.textAlign(*args)


@pyffi.interface(name="wcaml_canvas_text_baseline")
def wcaml_canvas_text_baseline(ctx, *args):
    return ctx.textBaseline(*args)


@pyffi.interface(name="wcaml_canvas_text_baseline")
def wcaml_canvas_text_baseline(ctx, *args):
    return ctx.textBaseline(*args)


# TODO some of the above stuff are attrs and need getters/setters, not functions
# TODO color, styles, shadows canvas bindings and everything after (image, transformations, ...)
# TODO https://www.w3schools.com/Jsref/api_canvas.asp


@pyffi.interface(name="add_color_stop")
def add_color_stop(ctx, *args):
    ctx.addColorStop(*args)


@pyffi.interface(name="create_linear_gradient")
def create_linear_gradient(ctx, *args):
    ctx.createLinearGradient(*args)


@pyffi.interface(name="create_pattern")
def create_pattern(ctx, *args):
    return ctx.createPattern(*args)


@pyffi.interface(name="create_radial_gradient")
def create_radial_gradient(ctx, *args):
    return ctx.createRadialGradient(*args)


@pyffi.interface(name="get_fill_style")
def get_fill_style(ctx, *args):
    return ctx.fillStyle


@pyffi.interface(name="set_fill_style")
def set_fill_style(ctx, value):
    ctx.fillStyle = value


@pyffi.interface(name="get_line_cap")
def get_line_cap(ctx, *args):
    return ctx.lineCap


@pyffi.interface(name="set_line_cap")
def set_line_cap(ctx, value):
    ctx.lineCap = value


@pyffi.interface(name="get_line_join")
def get_line_join(ctx, *args):
    return ctx.lineJoin


@pyffi.interface(name="set_line_join")
def set_line_join(ctx, value):
    ctx.lineJoin = value


@pyffi.interface(name="get_line_width")
def get_line_width(ctx):
    return ctx.lineWidth


@pyffi.interface(name="set_line_width")
def set_line_width(ctx, value):
    ctx.lineWidth = value


@pyffi.interface(name="get_miter_limit")
def get_miter_limit(ctx, *args):
    return ctx.miterLimit


@pyffi.interface(name="set_miter_limit")
def set_miter_limit(ctx, value):
    ctx.miterLimit = value


@pyffi.interface(name="get_shadow_blur")
def get_shadow_blur(ctx, *args):
    return ctx.shadowBlurshadowBlur


@pyffi.interface(name="set_shadow_blur")
def set_shadow_blur(ctx, value):
    ctx.shadowBlur = value


@pyffi.interface(name="get_shadow_color")
def get_shadow_color(ctx, *args):
    return ctx.shadowColor


@pyffi.interface(name="set_shadow_color")
def set_shadow_color(ctx, value):
    ctx.shadowColor = value


@pyffi.interface(name="get_shadow_offset_x")
def get_shadow_offset_x(ctx, *args):
    return ctx.shadowOffsetX


@pyffi.interface(name="set_shadow_offset_x")
def set_shadow_offset(ctx, value):
    ctx.shadowOffsetX = value


@pyffi.interface(name="get_shadow_offset_y")
def get_shadow_offset_y(ctx, *args):
    return ctx.shadowOffsetY


@pyffi.interface(name="set_shadow_offset_y")
def set_shadow_offset(ctx, value):
    ctx.shadowOffsetY = value


@pyffi.interface(name="get_stroke_style")
def get_stroke_style(ctx, *args):
    return ctx.strokeStyle


@pyffi.interface(name="set_stroke_style")
def set_stroke_style(ctx, value):
    ctx.strokeStyle = value


@pyffi.interface(name="scale")
def scale(ctx, *args):
    ctx.scale(*args)


@pyffi.interface(name="rotate")
def rotate(ctx, *args):
    ctx.rotate(*args)


@pyffi.interface(name="translate")
def translate(ctx, *args):
    ctx.translate(*args)


@pyffi.interface(name="transform")
def transform(ctx, *args):
    ctx.transform(*args)


@pyffi.interface(name="set_transform")
def set_transform(ctx, *args):
    ctx.setTransform(*args)


@pyffi.interface(name="draw_image")
def draw_image(ctx, *args):
    ctx.drawImage(*args)


@pyffi.interface(name="create_image_data")
def create_image_data(ctx, *args):
    return ctx.create_image_data(*args)


@pyffi.interface(name="get_image_data")
def get_image_data(ctx, *args):
    return ctx.get_image_data(*args)


# ImageData.data
# ImageData.height
# ImageData.width
@pyffi.interface(name="put_image_data")
def put_image_data(ctx, *args):
    return ctx.put_image_data(*args)


# globalAlpha	Sets or returns the current alpha or transparency value of the drawing
# globalCompositeOperation	Sets or returns how a new image are drawn onto an existing image


@pyffi.interface(name="clip")
def clip(ctx, *args):
    ctx.clip(*args)


@pyffi.interface(name="save")
def save(ctx, *args):
    ctx.save(*args)


@pyffi.interface(name="restore")
def restore(ctx, *args):
    ctx.restore(*args)


@pyffi.interface(name="create_event")
def create_event(ctx, *args):
    ctx.createEvent(*args)


@pyffi.interface(name="get_context")
def get_context(ctx, *args):
    return ctx.getContext(*args)


@pyffi.interface(name="to_data_url")
def to_data_url(ctx, *args):
    return ctx.toDataURL(*args)


# "canvas": {
#     "wcaml_canvas_get_context": wcaml_canvas_get_context,
#     "wcaml_canvas_text_baseline": wcaml_canvas_text_baseline,
#     "wcaml_canvas_text_align": wcaml_canvas_text_align,
#     "wcaml_canvas_stroke_text": wcaml_canvas_stroke_text,
#     "wcaml_canvas_measure_text": wcaml_canvas_measure_text,
#     "wcaml_canvas_font": wcaml_canvas_font,
#     "wcaml_canvas_fill_text": wcaml_canvas_fill_text,
#     "wcaml_canvas_direction": wcaml_canvas_direction,
#     "wcaml_canvas_quadratic_curve_to": wcaml_canvas_quadratic_curve_to,
#     "wcaml_canvas_arc_to": wcaml_canvas_arc_to,
#     "wcaml_canvas_arc": wcaml_canvas_arc,
#     "wcaml_canvas_bezier_curve_to": wcaml_canvas_bezier_curve_to,
#     "wcaml_canvas_stroke": wcaml_canvas_stroke,
#     "wcaml_canvas_rect": wcaml_canvas_rect,
#     "wcaml_canvas_fill": wcaml_canvas_fill,
#     "wcaml_canvas_line_to": wcaml_canvas_line_to,
#     "wcaml_canvas_move_to": wcaml_canvas_move_to,
#     "wcaml_canvas_is_point_in_path": wcaml_canvas_is_point_in_path,
#     "wcaml_canvas_clear_rect": wcaml_canvas_clear_rect,
#     "wcaml_canvas_stroke_rect": wcaml_canvas_stroke_rect,
#     "wcaml_canvas_fill_rect, ": wcaml_canvas_fill_rect,
# },
