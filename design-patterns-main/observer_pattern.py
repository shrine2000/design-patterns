from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
    
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class NewsPublisher(Subject):
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def attach(self, observer: Observer):
        self._observers.append(observer)
        print(f"{observer.__class__.__name__}")

    def detach(self, observer: Observer):
        self._observers.remove(observer)
        print(f"{observer.__class__.__name__}")

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news):
        self._latest_news = news
        self.notify()

class NewsReader(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} got news update: {message}")


class EmailSubscriber(Observer):
    def __init__(self, email):
        self._email = email

    def update(self, message):
        print(f"Email to {self._email}: {message}")


class MobileAppSubscriber(Observer):
    def  __init__(self, username):
        self._username = username

    def update(self, message):
        print(f"Push notification for {self._username}: {message}")


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    reader1 = NewsReader("Alice")
    reader2 = NewsReader("Bob")
    email_subscriber = EmailSubscriber("bob@example.com")
    mobile_app_subscriber = MobileAppSubscriber("bob123")

    news_publisher.attach(reader1)
    news_publisher.attach(reader2)
    news_publisher.attach(email_subscriber)
    news_publisher.attach(mobile_app_subscriber)

    news_publisher.add_news("Python 3.10 is released!")
    print()
    news_publisher.add_news("Observer Pattern in Python is easy to implement.")

    news_publisher.detach(reader2)

    print()
    news_publisher.add_news("Django 4.0 is released!")