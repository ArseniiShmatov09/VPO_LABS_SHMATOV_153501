import unittest
import sys
import os

sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task4 import generate_color, generate_table
class TestGenerateColor(unittest.TestCase):

    def test_generate_color_value_0(self):
        result = generate_color(0.0)
        self.assertEqual(result, 'rgb(255, 255, 255)')

    def test_generate_color_value_0_5(self):
        result = generate_color(0.5)
        self.assertEqual(result, 'rgb(128, 128, 128)')

    def test_generate_color_value_1(self):
        result = generate_color(1.0)
        self.assertEqual(result, 'rgb(0, 0, 0)')

    def test_generate_color_value_0_25(self):
        result = generate_color(0.25)
        self.assertEqual(result, 'rgb(192, 192, 192)')

    def test_generate_color_value_0_75(self):
        result = generate_color(0.75)
        self.assertEqual(result, 'rgb(64, 64, 64)')

    def test_generate_table_colors(self):
        # Генерируем таблицу
        generate_table()

        # Проверяем цвета в каждой ячейке таблицы
        with open('gradient_table.html', 'r') as f:
            html_content = f.read()

        rows = html_content.split('<tr>')
        rows = [row for row in rows if '<td' in row]

        for i, row in enumerate(rows):
            cells = row.split('<td')
            cells = [cell for cell in cells if 'style="background-color:' in cell]

            for j, cell in enumerate(cells):
                color_start = cell.find('style="background-color:') + len('style="background-color:')
                color_end = cell.find(';"', color_start)
                cell_color = cell[color_start:color_end]

                # Вычисляем ожидаемый цвет на основе текущей строки
                color_value = i / len(rows)
                expected_color = generate_color(color_value)

                # Проверяем, что цвет в текущей ячейке соответствует ожидаемому
                self.assertEqual(cell_color, expected_color)


if __name__ == '__main__':
    unittest.main()
