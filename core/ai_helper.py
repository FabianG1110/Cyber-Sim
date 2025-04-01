from core.gemini_wrapper import GeminiChat

class AIHelper:
    def __init__(self, player):
        self.player = player
        self.gemini = GeminiChat()

    def provide_hint(self, challenge):
        self.player.use_hint()

        prompt = f"""
        You're a cybersecurity coach AI. The player is working on a CTF-style challenge about {challenge.challenge_type}.
        Give a short, helpful hint without revealing the answer.
        """

        return self.gemini.ask(prompt)

    def analyze_progress(self):
        stats = self.player.get_stats()
        if stats["success_rate"] >= 80:
            return "Strong performance! Keep going."
        elif stats["success_rate"] >= 50:
            return "Decent progress. Consider reviewing weak spots."
        else:
            return "You're just getting started — no shame in using a hint!"
