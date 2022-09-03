class Stats:
    """статистика"""

    def __init__(self):
        """инициализация стаистики"""
        self.score = 0
        self.guns_left = 5
        self.reset_stats()
        self.run_game = True
        with open("highrecords.txt", "r") as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """динамика статистики(изменение)"""
