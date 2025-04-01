from core.player import Player
from core.challenge import Challenge
from core.ai_helper import AIHelper

class FakeChallenge(Challenge):
    def __init__(self):
        super().__init__(challenge_id=1, challenge_type="ctf_web_inspection")

    def evaluate_answer(self, answer):
        return answer == "FLAG{test}"

    def get_hint(self):
        return "Try checking the HTML comments."

# Setup
player = Player("HackerHero")
ai = AIHelper(player)
challenge = FakeChallenge()

player.start_challenge(challenge.challenge_id)

print("Generated AI Hint:")
print(ai.provide_hint(challenge))
print("\nProgress Analysis:")
print(ai.analyze_progress())
