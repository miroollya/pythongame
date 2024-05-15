from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    player_name = request.form.get('player_name')
    if not player_name:
        player_name = 'Adventurer'
    
    story = [
        f"Hello, {player_name}! Welcome to Pylandia.",
        "Your first task is to help a villager organize their items using variables.",
        "Create a variable named 'item' and store the value 'Magic Wand' in it."
    ]
    
    return render_template('game.html', player_name=player_name, story=story, task='task1')

@app.route('/task1', methods=['POST'])
def task1():
    player_name = request.form.get('player_name')
    item_code = request.form.get('item')
    if item_code.strip() == "item = 'Magic Wand'":
        story = [
            "Great job! You've created a variable named 'item' and stored the value 'Magic Wand' in it.",
            "In Python, there are different types of data you can work with, such as strings, numbers, and lists.",
            "Create a list of three items you might need on your adventure."
        ]
        return render_template('game.html', player_name=player_name, story=story, task='task2')
    else:
        message = "Hmm, that doesn't seem right. Try again. Remember to type exactly: item = 'Magic Wand'"
        return render_template('result.html', message=message, player_name=player_name)

@app.route('/task2', methods=['POST'])
def task2():
    player_name = request.form.get('player_name')
    list_code = request.form.get('list_data')
    if list_code.strip().startswith("list_data = [") and list_code.strip().endswith("]"):
        story = [
            "Well done! You've created a list with your adventure items.",
            "Now, let's solve a riddle using string manipulation.",
            "Try to create a greeting message for yourself. Combine 'Hello, ' with your character's name."
        ]
        return render_template('game.html', player_name=player_name, story=story, task='task3')
    else:
        message = "Hmm, that doesn't seem right. Try again. Remember to type exactly: list_data = ['item1', 'item2', 'item3']"
        return render_template('result.html', message=message, player_name=player_name)

@app.route('/task3', methods=['POST'])
def task3():
    player_name = request.form.get('player_name')
    greeting_code = request.form.get('greeting')
    expected_code = f"greeting = 'Hello, ' + '{player_name}'"
    if greeting_code.strip() == expected_code:
        message = f"Awesome! Your greeting message is: Hello, {player_name}. Congratulations! You've completed the first chapter of Python Quest. Here is your flag: UCC{{Pyth0n_iz_e4sy_2_learn}}"
    else:
        message = f"Hmm, that doesn't seem right. Try again. Remember to type exactly: greeting = 'Hello, ' + '{player_name}'"
    return render_template('result.html', message=message, player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)
