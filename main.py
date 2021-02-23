# Course: CS 30
# Period: 1
# Date Created: 20/10/08
# Date Modified:
# Name: Volodymyr Akulov
# Description: Peasant turn based house defender

# Nested dictionary of characters in peasent defender.

Characters = {
    'Peasant': {
      'W': 'The poor uneducated dirt poor peasant aka your measly character ',
      'Hp': 10, },
    'Enemy Peasant': {
      'W': 'Some random pesant whos just very slightly better than you',
      'Hp': 11, },
    'Pillgrim': {
      'W': 'A religious man who spreads his religion to other lands',
      'Hp': 15, },
    'Knight': {
      'W': 'A dapper gentlemen sure to rescue you in a time of need (or not)',
      'Hp': 30, },
    'Priest': {
      'W': '"Have you heard of our lord and saviour?"',
      'Hp': 25, },
    'Archer': {
      'W': 'Some british lad with a bent stick and a few pointy sticks',
      'Hp': 15, },
    'Hero': {
      'W': '"The Hero"',
      'Hp': 50, },
    'Hero+': {
      'W': '"you lose"',
      'Hp': 300, },
    'Drunkard': {
      'W': '"A drunk man who just lost his house in a rigged dice game"',
      'Hp': 10, }, }

# Looping Peasant defender Characters's traits.
print("Character Descriptions\n")
for Characters, CharacterInfo in Characters.items():
    x = "-"
    print(f"{Characters.title()}:\n{30 * x}\n{(CharacterInfo['W'])}")
    print(f"The {Characters.title()}'s Hp is {CharacterInfo['Hp']}.")
    print(30 * "-" + "\n")

print('\n')

# Nested dictionary of character inventories in peasent defender.
EnemyInventories = {
    'Enemy Peasant': {
      'Weapon': ['Stick'],
      'Armour': ['Leather Cap'],
      'Healing': ['Potato']
    },
    'Pilgrim': {
      'Weapon': ['Staff'],
      'Armour': ['Leather Cap'],
      'Healing': ['Bread']
    },
    'Knight': {
      'Weapon': ['Sword'],
      'Armour': ['Steel Breastplate', 'Shield'],
      'Healing': ['Health Potion']
    },
    'Priest': {
      'Weapon': ['Staff', 'God'],
      'Armour': ['Faith', 'Drapes'],
      'Healing': ['Holy water']
    },
    'Archer': {
      'Weapon': ['Bow'],
      'Armour': ['Hardened leather'],
      'Healing': ['potato']
    },
    'Hero': {
      'Weapon': ['The hammer of god'],
      'Armour': ['Full plate armour'],
      'Healing': ['Health potion']
    },
    'Hero+': {
      'Weapon': ['Friendship'],
      'Armour': ['Plot armour'],
      'Healing': ['Determination']
    },
    'Drunkard': {
      'Weapon': ['Broken beer bottle', 'projectile vomit'],
      'Armour': ['none'],
      'Healing': ['Beer']
    },
}

# Displaying the enemy items and armour
print("\n\nCharacter Inventories\n")
for EnemyInventories, Inventories in EnemyInventories.items():
    x = "-"
    print(f"{EnemyInventories.title()}:\n{30 * x}")
    print(f"Weapons: {Inventories['Weapon']}")
    print(f"Armour: {Inventories['Armour']}")
    print(f"Healing: {Inventories['Healing']}")
    print(30 * "-" + "\n")

# Nested dictionary of tiles in peasent defender.
LocationTiles = {
    'Mud': {
      'Accuracy': -5,
      'Damadge':  0
    },
    'Dirt': {
      'Accuracy': 0,
      'Damadge':  0
    },
    'Grass': {
      'Accuracy': -5,
      'Damadge':  +5
    },
    'stone': {
      'Accuracy': +5,
      'Damadge':  0
    },
}

# Displaying types of Tiles 

print("Types of tiles and their modifiers\n")
for LocationTiles, Tiles in LocationTiles.items():
    x = "-"
    print(f"{LocationTiles.title()}:\n{30 * x}")
    print(f"Dmg modifier: {Tiles['Damadge']}")
    print(f"Accuracy modifier: {Tiles['Accuracy']}")
    print(30 * "-" + "\n")
