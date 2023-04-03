from datetime import date


class Task:
    def __init__(self, title, description, created=date.today()):
        self.title = title
        self.description = description
        self.created = created
