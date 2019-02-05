### Movement
from bge import logic, events
keyboard = logic.keyboard
SPEED_STEP = 0.01
TILT_STEP = 0.02
ROTATION_STEP = 0.03
MAX_SPEED = 1.10
SPEED_UP_KEY = events.WKEY
SPEED_DOWN_KEY = events.SKEY
GO_FORWARD_KEY = events.UPARROWKEY
GO_BACKWARD_KEY = events.DOWNARROWKEY
TURN_RIGHT_KEY = events.RIGHTARROWKEY
TURN_LEFT_KEY = events.LEFTARROWKEY
FALLING_SPEED = -7

def is_key_pressed(key):
    return keyboard.events[key] == logic.KX_INPUT_ACTIVE

def update_speed(own):
    if is_key_pressed(SPEED_DOWN_KEY):
        if own['speed'] > SPEED_STEP:
            own['speed'] -= SPEED_STEP
    if is_key_pressed(SPEED_UP_KEY):
        if own['speed'] < MAX_SPEED:
            own['speed'] += SPEED_STEP
    if own['speed'] > 0:
        own['speed'] -= SPEED_STEP*0.05
        if own['speed'] < 0:
            own['speed'] = 0

def update_tilt(own):
    if is_key_pressed(GO_FORWARD_KEY):
        own.applyRotation([ 0, -TILT_STEP, 0], True)
    if is_key_pressed(GO_BACKWARD_KEY):
        own.applyRotation([ 0, TILT_STEP, 0], True)
    rotation = own.worldOrientation.to_euler()
    if (rotation.y != 0):
        own.applyRotation([0, -rotation.y/25, 0], True)
    if (rotation.x != 0):
        own.applyRotation([-rotation.x/25, 0, 0], True)
        
def update_rotation(own):
    if is_key_pressed(TURN_RIGHT_KEY):
        own.applyRotation([0, 0, -ROTATION_STEP])
    if is_key_pressed(TURN_LEFT_KEY):
        own.applyRotation([0, 0, ROTATION_STEP])

def update_force(own):
    own.applyForce([0, 0, own['speed']*100], True)

def apply_air_resistance(own):
    velocity = own.getLinearVelocity()
    print(velocity)
    own.applyForce([-velocity.x*5, -velocity.y*5, 0])

def main(controller):
    own = controller.owner
    update_speed(own)
    update_tilt(own)
    update_rotation(own)
    update_force(own)
    apply_air_resistance(own)
    
main(logic.getCurrentController())



### Camera
from bge import logic, events
from mathutils import Vector

keyboard = logic.keyboard
TURN_RIGHT_KEY = events.RIGHTARROWKEY
TURN_LEFT_KEY = events.LEFTARROWKEY
TURN_RIGHT_KEY2 = events.KKEY
TURN_LEFT_KEY2 = events.LKEY
ROTATION_STEP = 0.01

def is_key_pressed(key):
    return keyboard.events[key] == logic.KX_INPUT_ACTIVE

def update_rotation(own):
    if is_key_pressed(TURN_RIGHT_KEY) or is_key_pressed(TURN_RIGHT_KEY2):
        own.applyRotation([0, 0, -ROTATION_STEP])
    if is_key_pressed(TURN_LEFT_KEY) or is_key_pressed(TURN_LEFT_KEY2):
        own.applyRotation([0, 0, ROTATION_STEP])

def main(controller):
    own = controller.owner
    update_rotation(own)

    scene = logic.getCurrentScene()
    helicopter = scene.objects['Helicopter']
    own.worldPosition = helicopter.worldPosition
    
main(logic.getCurrentController())



### Colide
from bge import logic

scene = logic.getCurrentScene()
scene.replace('SelectLevel')




### Finish
from bge import logic

scene = logic.getCurrentScene()
speed = scene.objects['Helicopter']['speed']
if speed < 0.4:
    scene.replace('SelectLevel')




### RemoveCoin
from bge import logic

controller = logic.getCurrentController()
own = controller.owner
own.endObject()



### SpinCoin
from bge import logic

controller = logic.getCurrentController()
own = controller.owner

own.applyRotation([0, 0, 0.04], True)




### SpinScrew
from bge import logic

controller = logic.getCurrentController()
own = controller.owner

scene = logic.getCurrentScene()
speed = scene.objects['Helicopter']['speed']

own.applyRotation([0, 0, speed], True)