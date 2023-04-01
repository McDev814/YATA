from datetime import date


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created = date.today()
