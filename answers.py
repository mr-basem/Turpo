"""
Traffic Signs Answers Database - Scenario Stories
Maps each question ID to its single correct scenario story description.
"""

CORRECT_ANSWERS = {
    "1": "Workers are repairing the asphalt ahead, so cars must slow down.",
    "2": "A driver comes to a full stop, checks all lanes, then proceeds safely.",
    "3": "Tires lose grip on a wet, slick surface, so braking hard could spin the car.",
    "4": "Loose boulders tumble down the slope and block your lane.",
    "5": "A family is stepping onto the crosswalk to reach the other side.",
    "6": "Leaving your car unattended here is illegal and will get it towed.",
    "7": "Driving into a restricted street against the flow of oncoming traffic.",
    "8": "Steering through sharp, twisting bends that require lower speed.",
    "9": "An elevated asphalt bump ahead will jolt the chassis if crossed too fast.",
    "10": "Passing is strictly forbidden here because oncoming visibility is dangerous.",
    "11": "Swinging left into oncoming lanes where left turns are barred.",
    "12": "The road drops down a steep incline, so engine braking prevents brake fade.",
    "13": "A road crew in high-visibility vests is fixing underground pipes.",
    "14": "Slows down, yields to cars already in the ring, then merges in a circle.",
    "15": "The pavement is cracked, pitted, and uneven, requiring careful driving.",
    "16": "You must yield and let oncoming cars pass through the bottleneck first.",
    "17": "School just ended, and excited kids might dash across without looking.",
    "18": "Cyclists riding along the lane edge who need ample passing room.",
    "19": "Tapped the brakes and slowed down because hazards lie ahead.",
    "20": "Automated signal lights cycling between red, yellow, and green.",
}


def get_correct_answer(question_id):
    return CORRECT_ANSWERS.get(str(question_id))


def check_answer(question_id, selected_choice):
    correct = CORRECT_ANSWERS.get(str(question_id))
    if not correct or not selected_choice:
        return False
    return str(selected_choice).strip() == correct.strip()
