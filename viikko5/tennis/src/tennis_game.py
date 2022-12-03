class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def _number_to_tennis_term(self, number):
        terms = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty"
        }
        if number in terms:
            return terms[number]
        else:
            return None

    def _tie_game(self, number):
        score = self._number_to_tennis_term(number)
        if score not in (None, "Forty"):
            return score + "-All"
        else:
            return "Deuce"

    def _biased_game(self):
        difference = self.m_score1 - self.m_score2
        score = None
        if abs(difference) == 1: 
            score = "Advantage "
        elif abs(difference) > 1: 
            score = "Win for "
        if difference > 0:
            score += "player1"
        elif difference < 0:
            score += "player2"
        return score

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self._tie_game(self.m_score1)    
        elif self._number_to_tennis_term(max(self.m_score1, self.m_score2)) is None:
            score = self._biased_game()
        else:
            score = self._number_to_tennis_term(self.m_score1) + "-" + self._number_to_tennis_term(self.m_score2)

        return score
