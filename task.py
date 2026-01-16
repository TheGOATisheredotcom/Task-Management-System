class Task:
    def __init__(self, description, category, due_date, priority, status):
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

        def complete_task(self):
            self.status = 'Done'

    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date.isoformat(),
            "status": self.status,
        }
    
    @classmethod
    def from_dict(cls, data):
        import datetime as dt
        due_date = dt.date.fromisoformat(data["due_date"])
        return cls(
            description=data["description"],
            category=data["category"],
            due_date=due_date,
            status=data["status"]
        )
            
        
