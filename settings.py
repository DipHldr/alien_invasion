class Settings():
    """A class to store all settings for alien invasion."""
    def __init__(self):
        """initialize the game settings"""
        #screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5
        self.ship_limit=3
        #bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #alien settings
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #fleet drection of 1 represents right ; -1 represents left
        self.fleet_direction=1
        
        
