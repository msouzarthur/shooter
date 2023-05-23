from ursina import *
from player import *

app = Ursina()

player = Player()
quad = load_model('quad', use_deepcopy=True)
level_parent = Entity(model=Mesh(vertices=[], uvs=[]), texture='white_cube')

def make_level(texture):
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)

            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x+.5,y+.5,0) for e in quad.generated_vertices] 
                level_parent.model.uvs += quad.uvs
    
                if not collider:
                    collider = Entity(parent=level_parent, position=(x,y), model='quad', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    collider.scale_x += 1
            else:
                collider = None

            if col == color.green:
                player.start_position = (x, y)
                player.position = player.start_position

    level_parent.model.generate()

make_level(load_texture('./assets/level'))

player.traverse_target = level_parent
camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

app.run()
