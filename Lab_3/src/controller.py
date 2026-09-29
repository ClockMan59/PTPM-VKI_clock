class Controller:

    def __init__(self, calculator, database, user_interaction, external_service):
        self.calculator = calculator
        self.database = database
        self.user_interaction = user_interaction
        self.external_service = external_service

    def run(self):
        a_str, b_str, c_str = self.user_interaction.get_data()

        try:
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
        except (ValueError, TypeError):
            triangle_type, error_message = self.calculator.calculate(
                a_str, b_str, c_str
            )

            result = f"Тип: {triangle_type}. Ошибка: {error_message}"
            self.external_service.send(result)

            return result

        saved_result = self.database.get(a, b, c)

        if saved_result is not None:
            triangle_type, error_message = saved_result
        else:
            triangle_type, error_message = self.calculator.calculate(
                a_str, b_str, c_str
            )

            self.database.add(
                a,
                b,
                c,
                triangle_type,
                error_message
            )

        if error_message:
            result = f"Тип: {triangle_type}. Ошибка: {error_message}"
        else:
            result = f"Тип треугольника: {triangle_type}"

        self.external_service.send(result)

        return result