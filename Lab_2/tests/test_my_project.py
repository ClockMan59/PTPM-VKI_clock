import unittest

from src.my_project import calculate_triangle


class TestCalculateTriangle(unittest.TestCase):

    # 1. Проверяем равносторонний треугольник
    def test_returns_equilateral_triangle(self):
        triangle_type, coordinates = calculate_triangle("5", "5", "5")

        self.assertEqual(triangle_type, "равносторонний")
        self.assertEqual(len(coordinates), 3)

    # 2. Проверяем равнобедренный треугольник
    def test_returns_isosceles_triangle(self):
        triangle_type, coordinates = calculate_triangle("5", "5", "6")

        self.assertEqual(triangle_type, "равнобедренный")
        self.assertEqual(len(coordinates), 3)

    # 3. Проверяем разносторонний треугольник
    def test_returns_scalene_triangle(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "5")

        self.assertEqual(triangle_type, "разносторонний")
        self.assertEqual(len(coordinates), 3)

    # 4. Проверяем треугольник, который не существует
    
    def test_returns_not_triangle_when_triangle_inequality_is_violated(self):
        triangle_type, coordinates = calculate_triangle("1", "2", "5")

        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(
            coordinates,
            [(-1, -1), (-1, -1), (-1, -1)]
        )

    # 5. Проверяем нулевую сторону
    def test_returns_error_for_zero_side(self):
        triangle_type, coordinates = calculate_triangle("0", "4", "5")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-1, -1), (-1, -1), (-1, -1)]
        )

    # 6. Проверяем отрицательную сторону
    def test_returns_error_for_negative_side(self):
        triangle_type, coordinates = calculate_triangle("-3", "4", "5")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-1, -1), (-1, -1), (-1, -1)]
        )

    # 7. Проверяем нечисловое значение первой стороны
    def test_returns_invalid_input_for_non_numeric_first_side(self):
        triangle_type, coordinates = calculate_triangle("abc", "4", "5")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-2, -2), (-2, -2), (-2, -2)]
        )

    # 8. Проверяем нечисловое значение второй стороны
    def test_returns_invalid_input_for_non_numeric_second_side(self):
        triangle_type, coordinates = calculate_triangle("3", "abc", "5")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-2, -2), (-2, -2), (-2, -2)]
        )

    # 9. Проверяем нечисловое значение третьей стороны
    def test_returns_invalid_input_for_non_numeric_third_side(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "abc")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-2, -2), (-2, -2), (-2, -2)]
        )

    # 10. Проверяем пустую строку
    def test_returns_invalid_input_for_empty_side(self):
        triangle_type, coordinates = calculate_triangle("", "4", "5")

        self.assertEqual(triangle_type, "")
        self.assertEqual(
            coordinates,
            [(-2, -2), (-2, -2), (-2, -2)]
        )

    # 11. Проверяем дробные значения
    def test_accepts_decimal_side_values(self):
        triangle_type, coordinates = calculate_triangle("3.5", "4.5", "5.5")

        self.assertEqual(triangle_type, "разносторонний")
        self.assertEqual(len(coordinates), 3)

    # 12. Проверяем координаты для треугольника 3-4-5
    def test_calculates_coordinates_for_three_four_five_triangle(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "5")

        self.assertEqual(triangle_type, "разносторонний")
        self.assertEqual(coordinates, [(0, 0), (5, 0), (3, 2)])

    # 13. Проверяем, что координат всегда три
    def test_returns_three_vertices(self):
        triangle_type, coordinates = calculate_triangle("6", "7", "8")

        self.assertEqual(len(coordinates), 3)

    # 14. Проверяем формат координат
    def test_returns_integer_coordinates(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "5")

        for point in coordinates:
            self.assertEqual(len(point), 2)
            self.assertIsInstance(point[0], int)
            self.assertIsInstance(point[1], int)

    # 15. Проверяем первую вершину
    def test_first_vertex_is_zero_zero(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "5")

        self.assertEqual(coordinates[0], (0, 0))

    # 16. Проверяем, что вторая вершина лежит на горизонтальной оси
    def test_second_vertex_has_zero_y_coordinate(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "5")

        self.assertEqual(coordinates[1][1], 0)

    # 17. Проверяем большие значения сторон
    def test_scales_large_triangle_to_100_by_100_field(self):
        triangle_type, coordinates = calculate_triangle(
            "300",
            "400",
            "500"
        )

        for x, y in coordinates:
            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(x, 100)
            self.assertLessEqual(y, 100)

    # 18. Проверяем перестановку равных сторон
    def test_detects_isosceles_triangle_when_equal_sides_are_different(self):
        triangle_type, coordinates = calculate_triangle("6", "5", "6")

        self.assertEqual(triangle_type, "равнобедренный")

    # 19. Проверяем треугольник с очень маленькими сторонами
    def test_accepts_small_positive_sides(self):
        triangle_type, coordinates = calculate_triangle(
            "0.1",
            "0.1",
            "0.1"
        )

        self.assertEqual(triangle_type, "равносторонний")
        self.assertEqual(len(coordinates), 3)

    # 20. Проверяем границу существования треугольника
    def test_returns_not_triangle_when_two_sides_equal_third_side(self):
        triangle_type, coordinates = calculate_triangle("3", "4", "7")

        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(
            coordinates,
            [(-1, -1), (-1, -1), (-1, -1)]
        )


if __name__ == "__main__":
    unittest.main()
