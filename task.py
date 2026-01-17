import datetime as dt

class Task:
    def __init__(self, description, category, due_date, priority, status):
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    # Move this out of __init__
    def complete_task(self):
        self.status = 'Done'

    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            # .isoformat() is great, it turns the date object into "2026-01-17"
            "due_date": self.due_date.isoformat(),
            "status": self.status,
            "priority" : self.priority
        }

    @classmethod
    def from_dict(cls, data):
        due_date = dt.date.fromisoformat(data["due_date"])
        return cls(
            description=data["description"],
            category=data["category"],
            due_date=due_date,
            priority=data.get("priority", "Medium"), # Priority comes 4th
            status=data["status"]                    # Status comes 5th
        )