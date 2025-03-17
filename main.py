import pygame as pg
import time
from bird import Bird
pg.init()

class Game:
    def __init__(self):
        # setting window config
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.running = True
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 100 
        self.bird = Bird(self.scale_factor)
        self.is_enter_pressed = False
        self.setUPBgAndGround()
        self.gameLoop()

    def gameLoop(self):
        last_time = time.time()
        while self.running:
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN :
                        self.is_enter_pressed = True
                    if event.key == pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)

            self.updateEverything(dt)
            self.draw()
            
            # Update the display
            pg.display.flip()
            self.clock.tick(60) 

        pg.quit()

    def updateEverything(self, dt):
        # Move ground left
        if self.is_enter_pressed:
            self.ground1_rect.x -= self.move_speed * dt
            self.ground2_rect.x -= self.move_speed * dt

            # Wrap ground when off-screen
            if self.ground1_rect.right <= 0:
                self.ground1_rect.x = self.ground2_rect.right
            if self.ground2_rect.right <= 0:
                self.ground2_rect.x = self.ground1_rect.right
            
            self.bird.update(dt)    
        
    def setUPBgAndGround(self):
        # Loading images for bg and ground
        self.bg_img = pg.transform.scale_by(pg.image.load("assets/bg.png").convert(), self.scale_factor)
        self.ground1_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(), self.scale_factor)
        self.ground2_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(), self.scale_factor)

        # Create rects
        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground1_img.get_rect()

        # Set initial positions
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = self.ground2_rect.y = 568

    def draw(self):
        self.win.blit(self.bg_img, (0, -300))
        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)

# Run only in main.py  
if __name__ == "__main__":
    game = Game()