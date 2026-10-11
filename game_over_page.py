import random
from pgzero.actor import Actor
from sqlalchemy import true

ROAD_SIGNS = {
    "1":  "This sign warns that road construction is taking place.\nSlow down, follow detours or instructions, and watch for workers.",
    "2":  "This sign means you must come to a complete stop.\nStop fully, check traffic in all directions, then proceed when safe.",
    "3":  "This warns that the road surface may be slippery, especially when wet.\nReduce speed and avoid sudden braking or sharp turns.",
    "4":  "This sign means rocks may fall onto the road from a nearby slope.\nDrive carefully and do not stop in this area.",
    "5":  "This warns that pedestrians may cross the road ahead.\nSlow down and be ready to stop for pedestrians.",
    "6":  "This sign means parking is not allowed in this area.\nDo not stop or park your vehicle here.",
    "7":  "This sign means vehicles are not allowed to enter. Do not drive in this direction.",
    "8":  "This warns of sharp or continuous curves ahead. Slow down and keep full control of your vehicle.",
    "9":  "This sign warns of a speed hump on the road. Reduce speed to pass safely and comfortably.",
    "10": "This means passing other vehicles is prohibited. Stay in your lane and do not overtake.",
    "11": "This sign means turning left is not allowed. Continue straight or follow the permitted direction.",
    "12": "This warns of a steep uphill or downhill road. Slow down and use the correct gear to control your vehicle.",
    "13": "This indicates workers are present on or near the road. Reduce speed and follow warning signs or signals.",
    "14": "This warns that a roundabout is coming up. Slow down and give way to traffic already in the roundabout.",
    "15": "This sign means the road surface is uneven or bumpy. Reduce speed to avoid losing control or damaging your vehicle.",
    "16": "This means vehicles coming from the opposite direction have priority. Give way and proceed only when the road is clear.",
    "17": "This warns that children may cross the road, often near schools. Slow down and be prepared to stop suddenly.",
    "18": "This means bicycles may be crossing or using the road. Watch for cyclists and give them enough space.",
    "19": "This sign tells you to reduce your speed. Drive carefully and be alert for hazards ahead.",
    "20": "This warns that traffic lights are ahead. Prepare to stop and obey the signal lights.",
}

sign_actor = Actor("signs/1", (400, 150))
current_sign = None

def pick_random_sign():
    global current_sign
    current_sign = random.choice(list(ROAD_SIGNS.items()))

def reset():
    global current_sign
    current_sign = None
    music = true

def draw(screen, score, coins):
    if current_sign:
        sign_actor.image = f"signs/{current_sign[0]}"
        sign_actor.draw()
        screen.draw.text(current_sign[1], midtop=(400, 305), width=700, fontsize=33, color="white", align="center", shadow=(1, 1), scolor="black")

    screen.draw.text(f"Your score: {score}   Coins: {coins}", center=(400, 400), fontsize=36, color="yellow")
    screen.draw.text("GAME OVER", center=(400, 475), fontsize=110, color="red")
    screen.draw.text("Press R to Restart", center=(400, 550), fontsize=48, color="white")
