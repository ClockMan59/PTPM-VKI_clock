import unittest
from unittest.mock import Mock, patch

from src.triangle_calculator import TriangleCalculator
from src.database import Database
from src.user_interaction import ConsoleUserInteraction
from src.external_service import ExternalServer
from src.controller import Controller


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.calculator = TriangleCalculator()
        self.database = Database()
        self.user_interaction = ConsoleUserInteraction()
        self.external_service = Mock()

        self.controller = Controller(
            self.calculator,
            self.database,
            self.user_interaction,
            self.external_service
        )

    def tearDown(self):
        self.database.close()

    # 1. Полный интеграционный сценарий
    @patch("builtins.input", side_effect=["3", "4", "5"])
    def test_full_triangle_calculation(self, mock_input):
        result = self.controller.run()

        self.assertEqual(
            result,
            "Тип треугольника: разносторонний"
        )

        self.external_service.send.assert_called_once()

    # 2. Повторный запрос использует БД
    @patch("builtins.input", side_effect=["3", "4", "5"])
    def test_second_request_uses_database(self, mock_input):
        first_result = self.controller.run()
        second_result = self.controller.run()

        self.assertEqual(first_result, second_result)

        self.assertEqual(
            self.database.get(3, 4, 5),
            ("разносторонний", "")
        )

    # 3. Интеграция с ошибочными данными
    @patch("builtins.input", side_effect=["abc", "4", "5"])
    def test_invalid_input(self, mock_input):
        result = self.controller.run()

        self.assertIn(
            "Входные данные не являются числами",
            result
        )

        self.external_service.send.assert_called_once()

    # 4. Проверяем добавление в БД
    def test_database_add_and_get(self):
        self.database.add(
            3,
            4,
            5,
            "разносторонний",
            ""
        )

        result = self.database.get(3, 4, 5)

        self.assertEqual(
            result,
            ("разносторонний", "")
        )

    # 5. Проверяем удаление из БД
    def test_database_delete(self):
        self.database.add(
            3,
            4,
            5,
            "разносторонний",
            ""
        )

        self.database.delete(3, 4, 5)

        result = self.database.get(3, 4, 5)

        self.assertIsNone(result)

    # 6. Проверяем Mock внешнего сервиса
    def test_external_service_mock(self):
        service = Mock()

        service.send("Тестовое сообщение")

        service.send.assert_called_once_with(
            "Тестовое сообщение"
        )

    # 7. Проверяем реальный внешний сервис
    def test_external_server(self):
        service = ExternalServer()

        result = service.send("Тест")

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()