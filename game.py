import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys


#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

class Character(GameElement):
    IMAGE = "Girl"
   
    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []


class Ball(GameElement):
    IMAGE = "bomb.png"
    frame = 0
    exploded = False

    # def __init__(self, xy = (0,0), xm = 0, ym = 0):
    #     GameElement.__init__(self)
    #     self.rect.centerx, self.rect.centery = xy

    #     self.xmove = xm
    #     self.ymove = ym

def interact(self, player):
    if not player.invincible:

        # hit the player, take away health
        # player.hit(1)


        bomb = Ball()
        GAME_BOARD.register(bomb)
        GAME_BOARD.set_el(2, 4, bomb)
        exploded_bomb = Ball()
        exploded_bomb.exploded = True
        exploded_bomb.IMAGE = "explodedbomb.png"
        GAME_BOARD.register(exploded_bomb)
        GAME_BOARD.del_el(bomb.x, bomb.y)
        GAME_BOARD.set_el(bomb.x, bomb.y, exploded_bomb)

    
def update(self):
    self.frame += 1

    if self.frame > 20:
        if self.exploded:
            GAME_BOARD.del_el(self.x, self.y)
        else:
            self.move()
 
        self.frame = 0







#     def move(self):
#         self.rect.x += self.xmove
#         self.rect.y += self.ymove

#     def picture(self, filename):
#         self.Picture = Picture.load(filename)
#         self.rect = self.image.get_rect()

    # def ballBarrier(self):
    #     """
    #     Checks to make sure ball is within bounds, adjusts movement speed if it's not
    #     """
    #     if self.rect.right > GAME_WIDTH:
    #         self.xmove = random.randint(-2, 0)
    #     if self.rect.left < 0:
    #         self.xmove = random.randint(0, 2)
    #     if self.rect.bottom > GAME_HEIGHT:
    #         self.ymove = random.randint(-2, 0)
    #     if self.rect.top < 0:
    #         self.ymove = random.randint(0, 2)

class ball_manager(GameElement):
    def __init__(self, numballs = 5, balls = []):      
            self.blist = balls

    # def numballs():

    #     if numballs > 0:
    #         self.multipleBalls(numballs) # moved this here so balls get init'd only once

    def add_ball(self, xy = (0,0), xm = 0, ym = 0):
        self.blist.append(Ball(xy, xm, ym)) # appends a random ball

    # def multipleBalls(self, numballs):
    #     for i in range(numballs):
    #         self.add_ball((random.randint(0, GAME_WIDTH),
    #         random.randint(0, GAME_HEIGHT)),
    #         random.randint(-2,2),
    #         random.randint(-2,2))


class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True 


class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False   

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("SUPER POWER! You have %d STAR!"%(len(player.inventory)))


def initialize():
    """Put game initialization code here"""
    rock_positions = [
            (2, 1),
            (1, 5),
            (3, 8),
            (2, 1) 
        ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False


    for rock in rocks:
        print rock

        global PLAYER
        PLAYER = Character()
        GAME_BOARD.register(PLAYER)
        GAME_BOARD.set_el(2, 2, PLAYER)
        print PLAYER

        GAME_BOARD.draw_msg("This game is wicked awesome.")
        gem = Gem()
        GAME_BOARD.register(gem)
        GAME_BOARD.set_el(3, 1, gem)   


def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]
        existing_el = GAME_BOARD.get_el(next_x, next_y)
        if existing_el:
            existing_el.interact(PLAYER)
        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)
        

 
      

# def keyboard_handler():
#     if KEYBOARD[key.UP]:
#         GAME_BOARD.draw_msg("You pressed up")
#         next_y = PLAYER.y - 1
#         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#         GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
#     elif KEYBOARD[key.SPACE]:
#         GAME_BOARD.erase_msg()
#         next_y = PLAYER.y - 1
#         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#         GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
#     elif KEYBOARD[key.DOWN]:
#         GAME_BOARD.draw_msg("You pressed down")
#         next_y = PLAYER.y + 1
#         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#         GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
#     elif KEYBOARD[key.LEFT]:
#         GAME_BOARD.draw_msg("You pressed left")
#         next_x = PLAYER.x - 1
#         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#         GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
#     elif KEYBOARD[key.RIGHT]:
#         GAME_BOARD.draw_msg("You pressed right")
#         next_x = PLAYER.x + 1
#         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#         GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)







