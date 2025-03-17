import pygame as pg
pg.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height = 768
        self.running = True
        self.win = pg.display.set_mode((self.width,self.height))
        self.gameLoop()
    
    def gameLoop(self):
        while self.running:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.running = False

            # Fill screen with black
            self.win.fill((0,0,0))
            # Update the display
            pg.display.flip()

        pg.quit()

# run only in main.py  
if __name__ == "__main__":
    game = Game()
    # game.gameLoop()