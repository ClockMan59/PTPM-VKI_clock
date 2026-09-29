from triangle_calculator import TriangleCalculator
from database import Database
from user_interaction import ConsoleUserInteraction
from external_service import ExternalServer
from controller import Controller


def main():
    calculator = TriangleCalculator()
    database = Database()
    user_interaction = ConsoleUserInteraction()
    external_service = ExternalServer()

    controller = Controller(
        calculator,
        database,
        user_interaction,
        external_service
    )

    controller.run()

    database.close()


if __name__ == "__main__":
    main()