import logging
import math
import sys

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

def calculate_triangle(a_str, b_str, c_str):

    logging.info(
        f"Получен запрос: a={a_str}, b={b_str}, c={c_str}"
    )

    try:
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)
    except (ValueError, TypeError):
        logging.error("Входные данные не являются числами")
        return "", [(-2, -2), (-2, -2), (-2, -2)]

    logging.debug(f"Преобразованные значения: a={a}, b={b}, c={c}")

    if a <= 0 or b <= 0 or c <= 0:
        logging.error("Длины сторон должны быть положительными")
        return "", [(-1, -1), (-1, -1), (-1, -1)]

    if a + b <= c or a + c <= b or b + c <= a:
        logging.warning("Треугольник с такими сторонами не существует")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if math.isclose(a, b) and math.isclose(b, c):
        triangle_type = "равносторонний"
    elif (
        math.isclose(a, b)
        or math.isclose(a, c)
        or math.isclose(b, c)
    ):
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    logging.info(f"Тип треугольника: {triangle_type}")

    x = (b ** 2 + c ** 2 - a ** 2) / (2 * c)
    y_squared = b ** 2 - x ** 2


    if y_squared < 0 and math.isclose(y_squared, 0):
        y_squared = 0

    if y_squared < 0:
        logging.error("Не удалось вычислить координаты")
        return triangle_type, [(-1, -1), (-1, -1), (-1, -1)]

    y = math.sqrt(y_squared)


    max_coordinate = max(c, x, y, 0)

    if max_coordinate > 100:
        scale = 100 / max_coordinate
    else:
        scale = 1

    coordinates = [
        (0, 0),
        (round(c * scale), 0),
        (round(x * scale), round(y * scale))
    ]

    logging.info(f"Координаты вершин: {coordinates}")

    return triangle_type, coordinates


def main():
    logging.info("Программа запущена")

    try:
        a = input("Введите сторону A: ")
        b = input("Введите сторону B: ")
        c = input("Введите сторону C: ")

        triangle_type, coordinates = calculate_triangle(a, b, c)

        print("\nРезультат:")
        print(f"Тип треугольника: {triangle_type}")
        print(f"Координаты вершин: {coordinates}")

        logging.info(
            f"Запрос успешно обработан: "
            f"тип={triangle_type}, координаты={coordinates}"
        )

    except Exception:
        logging.exception(
            "Непредвиденная ошибка"
        )


if __name__ == "__main__":
    main()

    