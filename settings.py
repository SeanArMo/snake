class Settings:
    def __init__(self):
        self.SCREEN_WIDTH = 1600
        self.SCREEN_HEIGHT = 1600
        self.WINDOW_TITLE = "Snake"

        self.BLOCK_SIZE = 0.02
        self.VELOCITY = self.SCREEN_HEIGHT * self.BLOCK_SIZE

        self.FPS = 10

        self.GROWTH_VALUE = 10

        self.running = True
