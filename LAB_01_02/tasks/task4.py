def generate_color(value):
    # Генерация RGB значения вида (r, g, b) 
    color = (255 - int(value * 255),) * 3
    return f'rgb{color}'

def generate_table():
    # Открываем файл для записи
    with open('gradient_table.html', 'w') as f:
        # Записываем начало HTML-файла
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<style>\n')
        f.write('table {\nborder-collapse: collapse;\nwidth: 100%;\nborder: 0; /* Убираем границу у таблицы */\n}\n')
        f.write('td, th {\nborder: 0px solid black;\npadding: 8px;\nfont-family: Arial, sans-serif;\n}\n')
        f.write('</style>\n</head>\n<body>\n')
        f.write('<table>\n')

        # Генерация таблицы 70x10
        for i in range(70):
            f.write('<tr>\n')
            for j in range(10):
                color_value = i / 70
                color = generate_color(color_value)
                f.write(f'<td style="background-color:{color};"></td>\n')
            f.write('</tr>\n')

        # Закрываем HTML-файл
        f.write('</table>\n</body>\n</html>')

# Генерация таблицы

if __name__ == '__main__':

    generate_table()
