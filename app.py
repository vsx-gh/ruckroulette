'''
Program:     app.py
Author:      Jeff VanSickle
Created:     20190530

Program selects a random three ruck PT exercises from a collection based on
user input for the body area they would like to work
'''

from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.debug = True

# PT moves and body area worked (subject to change/interpretation)
pt_moves = [{'name': 'Ruck Squat', 'area': 'leg'}, {'name': 'Lunges', 'area': 'leg'}, {'name': 'Ruck Overhead Squat', 'area': 'both'},
        {'name': 'Push-up', 'area': 'arm'}, {'name': 'Ruck High Pull', 'area': 'arm'}, {'name': 'Overhead Shoulder Press', 'area': 'arm'},
        {'name': 'Bear Crawl', 'area': 'both'}, {'name': 'Suitcase Carry', 'area': 'arm'}, {'name': 'Russian Twist', 'area': 'abs'},
        {'name': 'Plank Pulls', 'area': 'abs'}, {'name': 'Ruck Swings', 'area': 'arm'}, {'name': 'Thruster', 'area': 'both'}, 
        {'name': 'Deadlift', 'area': 'both'}, {'name': 'Flutter Kicks', 'area': 'abs'}]

# Body area selection in drop-down menu
body_area = ['Leg', 'Arm', 'Both', 'Abs', 'Any']

@app.route('/', methods=['GET', 'POST'])
def dropdown():
    return render_template('index.html', body_areas=body_area)

@app.route('/results.html', methods=['GET', 'POST'])
def get_moves():
    if request.method == 'POST':
        workout_type = request.form['body_area']

    # Select any area, else get moves only from the area chosen by user
    if workout_type == 'Any':
        workout_list = pt_moves
    else:
        workout_list = [item for item in pt_moves if item['area'] == workout_type.lower()]

    do_these_moves = []     # Hold moves that match body area selected
    curr_move = 0           # Move counter

    # Cap number of moves at 3; follows GORUCK training plans (mostly)
    while curr_move < 3:
        if curr_move > len(workout_list) - 1:     # Don't get more moves than available
            break

        list_pos = random.randint(0, len(pt_moves) - 1)
        add_move = workout_list[random.randint(0, len(workout_list) - 1)]

        # Avoid adding move to workout list multiple times
        if add_move not in do_these_moves:
            do_these_moves.append(add_move)
            curr_move += 1
        else:
            continue

    return render_template('results.html', body_areas=body_area, workout=do_these_moves)

if __name__ == "__main__":
    app.run()
