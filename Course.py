from abc import abstractmethod


class DisplayBehavior:
    @abstractmethod
    def display(self):
        pass

class OfflineCourseDisplay(DisplayBehavior):
    @abstractmethod
    def display(self):
        return f"{super().__str__()} - {self.location}"

class OnlineCourseDisplay(DisplayBehavior):
    @abstractmethod
    def display(self):
        return f"{super().__str__()} - {self.url}"


class Course:
    """Course"""

    def __init__(self, id, title, description, price):
        """Initialize Course"""
        self.id = id
        self.title = title
        self.description = description
        self.price = price

    def display_course(self):
        self.displayBehavior.display()


class OnlineCourse(Course):
    """Online Course"""

    def __init__(self, id, title, description, price, url):
        """Initialize Online Course"""
        super().__init__(id, title, description, price)
        self.url = url
        self.display_course = OnlineCourseDisplay()


class OfflineCourse(Course):
    """Offline Course"""

    def __init__(self, id, title, description, price, location):
        """Initialize Offline Course"""
        super().__init__(id, title, description, price)
        self.location = location
        self.display_course = OfflineCourseDisplay()
