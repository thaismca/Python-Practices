class Question:
    """Models a Question that can be used in a quiz"""
    def __init__(self, text, category, answer):
        self.text = text
        self.category = category
        self.answer = answer