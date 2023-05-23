from ursina.prefabs.platformer_controller_2d import PlatformerController2d

class Player(PlatformerController2d):
    def __init__(self, **kwargs):
        super().__init__(
            collider='box',
            scale=(1, 1),
            max_jumps=2,
            jump_height=1.8,  
            texture = 'assets/idle'
        ) 