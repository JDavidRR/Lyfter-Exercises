"""4- Cree las siguientes clases:
- Head
- Torso
- Arm
- Hand
- Leg
- Feet
- Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
Por ejemplo (este código esta incompleto, pero describe la idea):

class Torso:
	def __init__(self, head, right_arm, ...):
		self.head = head
		self.right_arm = right_arm
		...
		
class Hand:
	def __init__(self):
		pass

class Arm:
	def __init__(self, hand):
		self.hand = hand

right_hand = Hand()
right_arm = Arm(right_hand)
torso = Torso(head, right_arm, ...)"""

class Head:
    def __init__(self):
        pass

class Hand:
	def __init__(self):
		pass

class Arm:
	def __init__(self, hand):
		self.hand = hand

class Feet:
	def __init__(self):
		pass

class Leg:
	def __init__(self, feet):
		self.feet = feet

class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		self.right_leg = right_leg
		self.left_leg = left_leg

class Human:
	def __init__(self,cuerpo, name):
		self.cuerpo = cuerpo
		self.name = name

def main ():
	head = Head()
	right_hand = Hand()
	left_hand = Hand()
	right_arm = Arm(right_hand)
	left_arm = Arm(left_hand)
	right_feet = Feet()
	left_feet = Feet()
	right_leg = Leg(right_feet)
	left_leg = Leg(left_feet)
	torso = Torso(head,right_arm,left_arm,right_leg,left_leg)
	Juan = Human(torso,"Juan")

    