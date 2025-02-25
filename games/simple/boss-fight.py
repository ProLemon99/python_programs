import random
import time
import replit
sleep = time.sleep

critchance = random.randint(0,10)
crit = 2

defended = random.randint(0,6)
maxhealth= 35
bhealthmax = 50

def menu():
	print("Your Health: {}".format(hp))
	sleep(1)
	print("Enemy Health: {}".format(bosshp))
	sleep(1)
	print("\n[Attack] - Damages the enemy.\n[Defend] - Chance to block enemies attack.\n[Heal] - Regain some of your health.\n\n")

def attack():
	replit.clear()
	sleep(0.2)
	print("You attack the enemy. \n")
	
	critdmg = 1
	sleep(1)
	
	if critchance == 10:
		critdmg = damagedealt * crit
		
	print("You dealt {} damage.\n".format(damagedealt * critdmg))

	return damagedealt * critdmg

def defend():
	replit.clear()
	sleep(0.2)
	print("You prepare your defences. \n")

def heal():
	replit.clear()
	sleep(0.2)
	print("You wrap yourself in bandages. \n")
	sleep(1)
	print("You gained {} health. \n".format(plushp))

def battack():
	replit.clear()
	sleep(0.2)
	print("The Boss attacks you. \n")
	sleep(1)

	if prompt == "DEFEND":
			print("You deflected the attack. \n")
	else:
		print("You take {} damage. \n".format(damagetaken))

def bdefend():
	replit.clear()
	sleep(0.2)
	
	if prompt == "ATTACK":
			print("The Boss deflected your attack. \n")
	else:
		print("The Boss tried to deflect you attack...\n")
		sleep(1)
		replit.clear()
		print("... but it failed")

def bheal():
	replit.clear()
	sleep(0.2)
	print("The Boss regained {} health. \n".format(plusbhp))

play = True
hp = 20
bosshp = 50

while play == True:
	bturn = random.randint(1,6)
	damagedealt = random.randint(2,10)
	plushp = random.randint(5,12)
	plusbhp = random.randint(3,7)
	damagetaken = random.randint(1,8)
	
	if hp > 0 or bosshp > 0:
		if hp > 0:
			menu()
			prompt = input().upper()
			if prompt == "ATTACK":
				if bturn != 5:
					bosshp = bosshp - attack()
				sleep(1)
			elif prompt == "DEFEND":
				defend()
				sleep(1)
			elif prompt == "HEAL":
				replit.clear()
				heal()
				hp = hp + plushp
				if hp > maxhealth:
					hp = maxhealth
				sleep(1)
		else:
			break
		
		if bosshp > 0:
			if bturn < 5:
				battack()
				if prompt != "DEFEND":
					hp = hp - damagetaken
				sleep(1)
				replit.clear()
			elif bturn == 5:
				bdefend()
				sleep(1)
			elif bturn == 6:
				bheal()
				bosshp = bosshp + plusbhp
				if bosshp > bhealthmax:
					bosshp = bhealthmax
				sleep(1)
		else:
			break
		
	else:
		play = False
		break

print("Your Health: {}".format(hp))
print("Enemy Health: {}".format(bosshp))

if bosshp <= 0:
	print("You Win!")
elif hp <= 0:
	print("You Lose!")