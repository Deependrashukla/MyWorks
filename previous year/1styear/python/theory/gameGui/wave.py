"""
Subcontroller module for Planetoids

This module contains the subcontroller to manage a single level (or wave) in the 
Planetoids game.  Instances of Wave represent a single level, and should correspond
to a JSON file in the Data directory. Whenever you move to a new level, you are 
expected to make a new instance of the class.

The subcontroller Wave manages the ship, the asteroids, and any bullets on screen. These 
are model objects. Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Ed Discussions and we will answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random
import datetime

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Level is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)

class Wave(object):
    """
    This class controls a single level or wave of Planetoids.
    
    This subcontroller has a reference to the ship, asteroids, and any bullets on screen.
    It animates all of these by adding the velocity to the position at each step. It
    checks for collisions between bullets and asteroids or asteroids and the ship 
    (asteroids can safely pass through each other). A bullet collision either breaks
    up or removes a asteroid. A ship collision kills the player. 
    
    The player wins once all asteroids are destroyed.  The player loses if they run out
    of lives. When the wave is complete, you should create a NEW instance of Wave 
    (in Planetoids) if you want to make a new wave of asteroids.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 25 for an example.  This class will be similar to
    than one in many ways.  
    
    All attributes of this class are to be hidden. No attribute should be accessed 
    without going through a getter/setter first. However, just because you have an
    attribute does not mean that you have to have a getter for it. For example, the
    Planetoids app probably never needs to access the attribute for the bullets, so 
    there is no need for a getter there. But at a minimum, you need getters indicating
    whether you one or lost the game.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # THE ATTRIBUTES LISTED ARE SUGGESTIONS ONLY AND CAN BE CHANGED AS YOU SEE FIT
    # Attribute _data: The data from the wave JSON, for reloading 
    # Invariant: _data is a dict loaded from a JSON file
    #
    # Attribute _ship: The player ship to control 
    # Invariant: _ship is a Ship object
    #
    # Attribute _asteroids: the asteroids on screen 
    # Invariant: _asteroids is a list of Asteroid, possibly empty
    #
    # Attribute _bullets: the bullets currently on screen 
    # Invariant: _bullets is a list of Bullet, possibly empty
    #
    # Attribute _lives: the number of lives left 
    # Invariant: _lives is an int >= 0
    #
    # Attribute _firerate: the number of frames until the player can fire again 
    # Invariant: _firerate is an int >= 0
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (standard form) TO CREATE SHIP AND ASTEROIDS
    def __init__(self,json):
        self._data = json
        self._ship = Ship(x=json['ship']['position'][0], y=json['ship']['position'][1], width=2*SHIP_RADIUS, height=2*SHIP_RADIUS, source=SHIP_IMAGE, angle=json['ship']['angle'])
        self._asteroids=[]
        self._bullets=[]
        self._firerate=0
        self._lives=0
        for element in self._data["asteroids"]:
            if element['size']=="large":
                size="large"
                source=LARGE_IMAGE
                width=LARGE_RADIUS*2
                height=LARGE_RADIUS*2
                speed=LARGE_SPEED 
            elif element['size']=="small":
                size="small"
                source=SMALL_IMAGE
                width=SMALL_RADIUS*2
                height=SMALL_RADIUS*2
                speed=SMALL_SPEED
            elif element['size']=="medium":
                size="medium"
                source=MEDIUM_IMAGE
                width=MEDIUM_RADIUS*2
                height=MEDIUM_RADIUS*2
                speed=MEDIUM_SPEED
            x=element['position'][0]
            y=element['position'][1]
            direction_x = element['direction'][0]
            direction_y = element['direction'][1]

            direc = Vector2(direction_x,direction_y)
            if direction_x==0 and direction_y==0:
                velocity = direc
            else:
                velocity = direc.normalize()*speed
            self._asteroids.append(Asteroid(x,y,width,height,source,size,velocity))
            




                

    
    # UPDATE METHOD TO MOVE THE SHIP, ASTEROIDS, AND BULLETS
    def update(self,input):
        if self._ship != None:
            self._ship.turn(input)
            self._ship.impulse(input)
            self._ship.wrapping()
            self.bullet_asteroids_collision()
            # self.ship_asteroids_collision()
            self.bullet_creation(input)
        for i in self._asteroids:
            i.wrapping()
        
        for i in self._bullets:
            i.bullet_move()
       
        
        
        
    
    def bullet_creation(self,input):
        self._firerate+=1
        if  input.is_key_down('spacebar') and self._firerate >= BULLET_RATE:
            tip=(self._ship._facing * SHIP_RADIUS) +Vector2(self._ship.x,self._ship.y)
            bullet_velocity = self._ship._facing * BULLET_SPEED
            self._bullets.append(Bullet(x=tip.x,y=tip.y,velocity=bullet_velocity))
            self._firerate=0

    def delete_bullet(self,bullet):
        if bullet.x<0 or  bullet.x>GAME_WIDTH or  bullet.y > GAME_HEIGHT or  bullet.y<0:
            self._bullets.remove(bullet)


        

    
  



        

        
    
    # DRAW METHOD TO DRAW THE SHIP, ASTEROIDS, AND BULLETS
    def draw(self,view):
        if self._ship != None:
            self._ship.draw(view)
        for i in self._asteroids:
            i.draw(view)

        for i in self._bullets:
            i.draw(view)
            self.delete_bullet(i)
        
        
    
    # RESET METHOD FOR CREATING A NEW LIFE
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def bullet_asteroids_collision(self):
        i=0
        while i<len(self._bullets):
            j=0
            while j<len(self._asteroids):
                Radius=(self._bullets[i].width/2 + self._asteroids[j].width/2) 
                Distance = ((self._bullets[i].x - self._asteroids[j].x)**2 +(self._bullets[i].y - self._asteroids[j].y)**2)**0.5
                if Distance < Radius:
                    self.break_asteroid(self._bullets[i],self._asteroids[i])
                    self._asteroids.remove(self._asteroids[j])
                    self._bullets.remove(self._bullets[i])
                    
                    break
                j+=1
            i+=1
    def ship_asteroids_collision(self):
        i=0
        while i< len(self._asteroids):
            Radius= self._asteroids[i].width/2 + self._ship.width/2
            Distance= ((self._asteroids[i].x - self._ship.x)**2 + (self._asteroids[i].y - self._ship.y)**2)**0.5 
            if Distance < Radius:
                self.break_asteroid(self._ship,self._asteroids[i])
                self._asteroids.remove(self._asteroids[i])
                self._ship=None
                self._lives+=1
                break
            i+=1

    def break_asteroid(self,other,asteroid):
        if other._velocity.x == 0 and other._velocity.y == 0:
            vector1=Vector2(other._facing.x, other._facing.y)
            vector2=Vector2(other._facing.x*math.cos(degToRad(120))-other._facing.y*math.sin(degToRad(120)),other._facing.x*math.sin(degToRad(120))+other._facing.y*math.cos(degToRad(120)))
            vector3=Vector2(other._facing.x*math.cos(degToRad(240))-other._facing.y*math.sin(degToRad(240)),other._facing.x*math.sin(degToRad(240))+other._facing.y*math.cos(degToRad(240)))
        else:
            vector1 = Vector2(other._velocity.x, other._velocity.y).normalize()
            vector2 = Vector2(other._velocity.x*math.cos(degToRad(120))-other._velocity.y*math.sin(degToRad(120)),other._velocity.x*math.sin(degToRad(120))+other._velocity.y*math.cos(degToRad(120))).normalize()
            vector3 = Vector2(other._velocity.x*math.cos(degToRad(240))-other._velocity.y*math.sin(degToRad(240)),other._velocity.x*math.sin(degToRad(240))+other._velocity.y*math.cos(degToRad(240))).normalize()

        if asteroid._size=="large":
            self._asteroids.append(Asteroid(x=(vector1*MEDIUM_RADIUS).x+asteroid.x,y=(vector1*MEDIUM_RADIUS).y+asteroid.y,width=MEDIUM_RADIUS*2,height=MEDIUM_RADIUS*2,source=MEDIUM_IMAGE,size="medium",velocity=vector1*MEDIUM_SPEED))
            self._asteroids.append(Asteroid(x=(vector2*MEDIUM_RADIUS).x+asteroid.x,y=(vector2*MEDIUM_RADIUS).y+asteroid.y,width=MEDIUM_RADIUS*2,height=MEDIUM_RADIUS*2,source=MEDIUM_IMAGE,size="medium",velocity=vector2*MEDIUM_SPEED))
            self._asteroids.append(Asteroid(x=(vector3*MEDIUM_RADIUS).x+asteroid.x,y=(vector3*MEDIUM_RADIUS).y+asteroid.y,width=MEDIUM_RADIUS*2,height=MEDIUM_RADIUS*2,source=MEDIUM_IMAGE,size="medium",velocity=vector3*MEDIUM_SPEED))

        elif asteroid._size=="medium":
            self._asteroids.append(Asteroid(x=(vector1*SMALL_RADIUS).x+asteroid.x,y=(vector1*SMALL_RADIUS).y+asteroid.y,width=SMALL_RADIUS*2,height=SMALL_RADIUS*2,source=SMALL_IMAGE,size="small",velocity=vector1*SMALL_SPEED))
            self._asteroids.append(Asteroid(x=(vector2*SMALL_RADIUS).x+asteroid.x,y=(vector2*SMALL_RADIUS).y+asteroid.y,width=SMALL_RADIUS*2,height=SMALL_RADIUS*2,source=SMALL_IMAGE,size="small",velocity=vector2*SMALL_SPEED))
            self._asteroids.append(Asteroid(x=(vector3*SMALL_RADIUS).x+asteroid.x,y=(vector3*SMALL_RADIUS).y+asteroid.y,width=SMALL_RADIUS*2,height=SMALL_RADIUS*2,source=SMALL_IMAGE,size="small",velocity=vector3*SMALL_SPEED))

        


