import math


class TriangleCalculator:

    def calculate(self, a_str, b_str, c_str):
        try:
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
        except (ValueError, TypeError):
            return "", "Входные данные не являются числами"

        if a <= 0 or b <= 0 or c <= 0:
            return "", "Длины сторон должны быть положительными"

        if a + b <= c or a + c <= b or b + c <= a:
            return "не треугольник", "Треугольник с такими сторонами не существует"

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

        return triangle_type, ""