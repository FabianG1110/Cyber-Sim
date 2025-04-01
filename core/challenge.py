from abc import ABC, abstractmethod

class Challenge(ABC):
    def __init__(self, challenge_id, challenge_type):
        self.challenge_id = challenge_id
        self.challenge_type = challenge_type

    @abstractmethod
    def evaluate_answer(self, answer):
        pass

    @abstractmethod
    def get_hint(self):
        pass
