from generators.rectangular_symbol_generator import rectangular_symbol_generator
from generators.default_generator import default_generator
from exporters.svg.svg_exporter import export as svg_exporter


def generate_file_name(component_data, generator_name):
    manufacturer_name = component_data['manufacturer'].replace(' ', '_')
    part = component_data['part'].replace('#', '')
    return f"symbols/{manufacturer_name}_{part}_{generator_name}"


def generate(data):
    generator_map = {'default': default_generator,
                     'rectangle': rectangular_symbol_generator}

    if 'symbol_generator' not in data:
        symbol = default_generator(data, {})
        export_symbol(symbol, generate_file_name(data, 'generic'))
    else:
        for generator in data['symbol_generator']:
            generator_data = data['symbol_generator'][generator]
            filename = generate_file_name(data, generator)
            symbol = generator_map[generator](data, generator_data)
            export_symbol(symbol, filename)


def export_symbol(symbol, filename):
    exporters = [svg_exporter]
    for exporter in exporters:
        exporter(symbol, filename)
