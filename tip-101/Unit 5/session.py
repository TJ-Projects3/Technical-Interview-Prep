class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		print(f"{opponent.name} health: {opponent.hp}")
		opponent.hp = opponent.hp - self.damage
		print(f"{self.name} dealt {self.damage} to {opponent.name}")
		print(f"{opponent.name} health: {opponent.hp}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

		