import pybullet as p
import pybullet_data
import time


p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

# Cargar suelo
p.loadURDF("plane.urdf")

startPos = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])

# Cargar URDF del robot
robotId = p.loadURDF("opcional.urdf", startPos, startOrientation, useFixedBase=True)

# Total de joints
numJoints = p.getNumJoints(robotId)

# Guardar nombre e indice
jointInfo = {}
for i in range(numJoints):
    # nombre joint
    name = p.getJointInfo(robotId, i)[1].decode("utf-8")

    # indice asociado
    jointInfo[name] = i


# Slider para articulacion vertical
base_to_vertical_slider = p.addUserDebugParameter("Vertical", -0.8, 0.8, 0)

# Slider para articulacion horizontal
vertical_to_horizontal_slider = p.addUserDebugParameter("Horizontal", -3.14, 3.14, 0)


while True:
    # Leer valores actuales de los sliders
    base_to_vertcial_val = p.readUserDebugParameter(base_to_vertical_slider)
    vertical_to_horizontal_val = p.readUserDebugParameter(vertical_to_horizontal_slider)
    
    # Controlar posicion de las articulaciones
    p.setJointMotorControl2(robotId, jointInfo["base_to_vertical"], p.POSITION_CONTROL, targetPosition=base_to_vertcial_val)
    p.setJointMotorControl2(robotId, jointInfo["vertical_to_horizontal"], p.POSITION_CONTROL, targetPosition=vertical_to_horizontal_val)

    
    p.stepSimulation()
    time.sleep(1./240.)
