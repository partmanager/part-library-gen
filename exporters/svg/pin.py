import drawsvg as svg

pin_spacing = 50
pin_font_size = 40
pin_desc_spacing = 15


def generate_pin(pin_dict):
    group = svg.Group()
    if 'r' not in pin_dict or pin_dict['r'] == 0:
        pin_end = pin_dict['x'] + pin_dict['l']
        group.append(svg.Line(pin_dict['x'],
                              pin_dict['y'],
                              pin_end,
                              pin_dict['y'],
                              stroke_width=5,
                              stroke='black'))
        if 'desig' in pin_dict:
            group.append(svg.Text(pin_dict['desig'],
                                  pin_font_size,
                                  pin_end + pin_desc_spacing,
                                  pin_dict['y'] + pin_font_size / 4))
        if 'no' in pin_dict:
            if isinstance(pin_dict['no'], list) and len(pin_dict['no']) == 1:
                pin_no_str = str(pin_dict['no'][0])
            else:
                pin_no_str = str(pin_dict['no'])
            group.append(svg.Text(pin_no_str,
                                  pin_font_size,
                                  pin_end - 40,
                                  pin_dict['y'] - 5,
                                  text_anchor='end'))
    elif pin_dict['r'] == 180:
        pin_end = pin_dict['x'] - pin_dict['l']
        group.append(svg.Line(pin_dict['x'] - pin_dict['l'],
                              pin_dict['y'],
                              pin_dict['x'],
                              pin_dict['y'],
                              stroke_width=5,
                              stroke='black'))
        if 'desig' in pin_dict:
            group.append(svg.Text(pin_dict['desig'],
                                  pin_font_size,
                                  pin_end - pin_desc_spacing,
                                  pin_dict['y'] + pin_font_size / 4,
                                  text_anchor='end'))
        if 'no' in pin_dict:
            group.append(svg.Text(str(pin_dict['no']),
                                  pin_font_size,
                                  pin_end + 40,
                                  pin_dict['y'] - 5))
    return group


def generate_symbol_pin(pin):
    group = svg.Group()
    if pin.rotation == 0:
        pin_end = pin.x + pin.length
        group.append(svg.Line(pin.x,
                              pin.y,
                              pin_end,
                              pin.y,
                              stroke_width=5,
                              stroke='black'))
        if pin.name:
            group.append(svg.Text(pin.name,
                                  pin_font_size,
                                  pin_end + pin_desc_spacing,
                                  pin.y + pin_font_size / 4))
        if pin.number:
            if isinstance(pin.number, list) and len(pin.number) == 1:
                pin_no_str = str(pin.number[0])
            else:
                pin_no_str = str(pin.number)
            group.append(svg.Text(pin_no_str,
                                  pin_font_size,
                                  pin_end - 40,
                                  pin.y - 5,
                                  text_anchor='end'))
    elif pin.rotation == 180:
        pin_end = pin.x - pin.length
        group.append(svg.Line(pin.x - pin.length,
                              pin.y,
                              pin.x,
                              pin.y,
                              stroke_width=5,
                              stroke='black'))
        if pin.name:
            group.append(svg.Text(pin.name,
                                  pin_font_size,
                                  pin_end - pin_desc_spacing,
                                  pin.y + pin_font_size / 4,
                                  text_anchor='end'))
        if pin.number:
            if isinstance(pin.number, list) and len(pin.number) == 1:
                pin_no_str = str(pin.number[0])
            else:
                pin_no_str = str(pin.number)
            group.append(svg.Text(pin_no_str,
                                  pin_font_size,
                                  pin_end + 40,
                                  pin.y - 5))
    return group
