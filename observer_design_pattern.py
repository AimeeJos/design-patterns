from abc import ABC, abstractmethod
from typing import List, Any

# Observer interface

class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject", data: Any = None) -> None:
        pass

# Subject interface

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, data: Any = None) -> None:
        for observer in self._observers:
            observer.update(self, data)

# Concrete Subject

class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._news: str = ""

    @property
    def news(self) -> str:
        return self._news

    @news.setter
    def news(self, value: str) -> None:
        self._news = value
        self.notify(value)

# Concrete Observers

class EmailSubscriber(Observer):
    def update(self, subject: Subject, data: Any = None) -> None:
        print(f"EmailSubscriber received news: {data}")


class SMSSubscriber(Observer):
    def update(self, subject: Subject, data: Any = None) -> None:
        print(f"SMSSubscriber received news: {data}")

# Example usage

if __name__ == "__main__":
    agency = NewsAgency()
    email_sub = EmailSubscriber()
    sms_sub = SMSSubscriber()

    agency.attach(email_sub)
    agency.attach(sms_sub)

    agency.news = "Breaking: Observer Pattern Implemented!"
    agency.news = "Update: Observer Pattern in Action."
