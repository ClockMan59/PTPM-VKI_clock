from abc import ABC, abstractmethod


class ExternalService(ABC):

    @abstractmethod
    def send(self, message):
        pass


class ExternalServer(ExternalService):

    def send(self, message):
        print(f"Отправка на внешний сервер: {message}")
        return True