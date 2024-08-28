import unittest
import json
from src.part_library_gen.generators.multipart_generator import multipart_generator


class TestRectangularComponentGenerator(unittest.TestCase):
    def setUp(self):
        with open('tests/data/test_multipart.json') as json_file:
            j = json.load(json_file)
            self.symbol_data = j[0]
            self.generator_data = j[0]['symbol_generator']['multipart']

    def test_symbol_generation(self):
        generated_symbol = multipart_generator(self.symbol_data, self.generator_data)
        for symbol_part in generated_symbol:
            self.assertEqual(generated_symbol[symbol_part].designator.designator, "U?")
            self.assertEqual(generated_symbol[symbol_part].part_number.text, "Test Part Name")
            self.assertEqual(len(generated_symbol[symbol_part].pins), 3)

        self.assertEqual(generated_symbol['A'].pins[0].name, 'IN1+')
        self.assertEqual(generated_symbol['A'].pins[1].name, 'IN1-')
        self.assertEqual(generated_symbol['A'].pins[2].name, 'OUT1')

        self.assertEqual(generated_symbol['B'].pins[0].name, 'IN2+')
        self.assertEqual(generated_symbol['B'].pins[1].name, 'IN2-')
        self.assertEqual(generated_symbol['B'].pins[2].name, 'OUT2')

        self.assertEqual(generated_symbol['A'].pins[0].number, 3)
        self.assertEqual(generated_symbol['A'].pins[1].number, 2)
        self.assertEqual(generated_symbol['A'].pins[2].number, 1)

        self.assertEqual(generated_symbol['B'].pins[0].number, 5)
        self.assertEqual(generated_symbol['B'].pins[1].number, 6)
        self.assertEqual(generated_symbol['B'].pins[2].number, 7)

        self.assertEqual(generated_symbol['B'].pins[0].function, 'InAnalog')
        self.assertEqual(generated_symbol['B'].pins[1].function, 'InAnalog')
        self.assertEqual(generated_symbol['B'].pins[2].function, 'OutAnalog')
