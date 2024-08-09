from .rectangular_symbol_generator import rectangular_symbol_generator


def default_generator(data, generator_data):
    pin_count = len(data['pins'])

    left_side = data['pins'].keys()
    generator_data['left_side'] = list(left_side)
    generator_data['right_side'] = []
    return rectangular_symbol_generator(data, generator_data)
