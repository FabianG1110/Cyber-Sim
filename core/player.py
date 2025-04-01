import time

class Player:
    def __init__(self, username):
        self.username = username
        self.hints_used = 0
        self.challenges_completed = {}
        self.current_challenge = None
        self.time_started = None

    def start_challenge(self, challenge_id):
        self.current_challenge = challenge_id
        self.time_started = time.time()

    def complete_challenge(self, success):
        self.challenges_completed[self.current_challenge] = success
        self.current_challenge = None
        self.time_started = None

    def use_hint(self):
        self.hints_used += 1

    def get_stats(self):
        total = len(self.challenges_completed)
        passed = sum(1 for s in self.challenges_completed.values() if s)
        return {
            "attempted": total,
            "success_rate": (passed / total) * 100 if total > 0 else 0,
            "hints_used": self.hints_used
        }

