from abc import ABC, abstractmethod


class DocumentState(ABC):
    @abstractmethod
    def publish(self, context):
        pass

    @abstractmethod
    def review(self, context):
        pass


class Draft(DocumentState):
    def publish(self, context: "Document"):
        context.state = PublishedState()

    def review(self, context: "Document"):
        context.state = Review()


class Review(DocumentState):
    def publish(self, context):
        print("not able to publish")

    def review(self, context):
        print("already in context")


class PublishedState(DocumentState):
    def publish(self, context: "Document") -> None:
        print("Document is already published.")

    def review(self, context: "Document") -> None:
        print("Cannot review; the document is published.")


class Document:
    def __init__(self):
        self.state: DocumentState = Draft()

    def publish(self):
        self.state.publish(self)

    def review(self):
        self.state.review(self)


document = Document()

document.review()
document.publish()


document.review()
document.publish()


document.state = PublishedState()
document.publish()
document.review()
