import unittest

from src.Delivery import calculate_delivery_cost


class TestDelivery(unittest.TestCase):

    # 1. Обычная посылка
    def test_ordinary_package(self):
        result = calculate_delivery_cost(2, 100, "обычный")

        self.assertEqual(result, (700, "2026-09-04"))

    # 2. Хрупкая посылка
    def test_fragile_package(self):
        result = calculate_delivery_cost(2, 100, "хрупкий")

        self.assertEqual(result, (1000, "2026-09-04"))

    # 3. Опасная посылка
    def test_dangerous_package(self):
        result = calculate_delivery_cost(2, 100, "опасный")

        self.assertEqual(result, (1700, "2026-09-04"))

    # 4. Минимальный допустимый вес
    def test_min_weight_is_valid(self):
        result = calculate_delivery_cost(0.1, 100, "обычный")

        self.assertEqual(result, (700, "2026-09-04"))

    # 5. Максимальный допустимый вес
    def test_max_weight_is_valid(self):
        result = calculate_delivery_cost(50, 100, "обычный")

        self.assertEqual(result, (1050, "2026-09-04"))

    # 6. Вес меньше минимального
    def test_weight_below_minimum_is_invalid(self):
        result = calculate_delivery_cost(0.09, 100, "обычный")

        self.assertEqual(result, (-1, "0000-00-00"))

    # 7. Вес больше максимального
    def test_weight_above_maximum_is_invalid(self):
        result = calculate_delivery_cost(50.1, 100, "обычный")

        self.assertEqual(result, (-1, "0000-00-00"))

    # 8. Минимальная допустимая дистанция
    def test_min_distance_is_valid(self):
        result = calculate_delivery_cost(1, 1, "обычный")

        self.assertEqual(result, (205, "2026-09-04"))

    # 9. Дистанция больше максимальной
    def test_distance_above_maximum_is_invalid(self):
        result = calculate_delivery_cost(1, 5001, "обычный")

        self.assertEqual(result, (-1, "0000-00-00"))

    # 10. Нулевая дистанция
    def test_zero_distance_is_invalid(self):
        result = calculate_delivery_cost(1, 0, "обычный")

        self.assertEqual(result, (-1, "0000-00-00"))

    # 11. Неверный тип посылки
    def test_invalid_package_type_is_rejected(self):
        result = calculate_delivery_cost(1, 100, "почта")

        self.assertEqual(result, (-1, "0000-00-00"))

    # 12. Вес от 5 до 20 кг
    def test_weight_between_5_and_20_uses_1_2_coefficient(self):
        result = calculate_delivery_cost(6, 100, "обычный")

        self.assertEqual(result, (840, "2026-09-04"))

    # 13. Ровно 5 кг
    def test_weight_exactly_5_has_no_weight_coefficient(self):
        result = calculate_delivery_cost(5, 100, "обычный")

        self.assertEqual(result, (700, "2026-09-04"))

    # 14. Ровно 20 кг
    def test_weight_exactly_20_uses_1_5_coefficient(self):
        result = calculate_delivery_cost(20, 100, "обычный")

        self.assertEqual(result, (1050, "2026-09-04"))

    # 15. Экспресс-доставка уменьшает стоимость в два раза
    def test_express_delivery_halves_cost(self):
        result = calculate_delivery_cost(2, 100, "обычный", True)

        self.assertEqual(result, (350, "2026-09-03"))

    # 16. Дистанция 500 км
    def test_distance_500_takes_one_day(self):
        result = calculate_delivery_cost(1, 500, "обычный")

        self.assertEqual(result, (2700, "2026-09-04"))

    # 17. Дистанция 1000 км
    def test_distance_1000_takes_two_days(self):
        result = calculate_delivery_cost(1, 1000, "обычный")

        self.assertEqual(result, (5200, "2026-09-05"))

    # 18. Экспресс на дистанции 1000 км
    def test_express_1000_takes_one_day(self):
        result = calculate_delivery_cost(1, 1000, "обычный", True)

        self.assertEqual(result, (2600, "2026-09-04"))

    # 19. Экспресс на дистанции 500 км
    def test_express_500_takes_at_least_one_day(self):
        result = calculate_delivery_cost(1, 500, "обычный", True)

        self.assertEqual(result, (1350, "2026-09-04"))

    # 20. Нечисловой вес
    def test_non_numeric_weight_returns_error(self):
        result = calculate_delivery_cost("abc", 100, "обычный")

        self.assertEqual(result, (-1, "0000-00-00"))


if __name__ == "__main__":
    unittest.main()
