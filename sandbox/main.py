import pprint, re, random

from flask import Flask, request
import requests
from flask_cors import CORS
import fantasynames as names

'''
names = []
with open("names.txt") as file:
    contents = file.readlines()
for content in contents:
    names.append(content)
'''

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World"

def namegen(no):
    n = []
    for i in range(no):
        x = names.human()
        n.append(x)
    return n

@app.post('/namegen')
def namegen_post():
    message = request.json
    print(f"\nIncoming message to {request.path}:")
    pprint.pprint(message, indent=2)
    end = namegen(int(message["form_data"]['nameno']))
    ans = "Click on a button to save that name. <div class='msg-container'><ul>"
    for i in range(len(end)):
        ans += f'<button id="{end[i]}" onclick="nameSaver(\'{end[i]}\')"><li>{end[i]}</li></button>'
    ans += "</ul></div>"
    return {
        'author': 'DnDBot',
        'text': ans,
        'css': "/static/stylesheet.css",
        'js': "/static/name-saver.js",
    }

@app.post('/dnd')
def dnd_bot():
    message = request.json
    print(f"\nIncoming message to {request.path}:")
    pprint.pprint(message, indent=2)

    # default roll (rolls 1 d20)
    rolls = 1
    die = 20
    no = 10

    msg_txt = message['text']
    return {
        'author': 'DnDBot',
        #'text': f"<marquee>Hello! Your message was: {message_text}<marquee>",
        #'css': something here idk how to format it
        'text': f'''<div class="msg-container">
                <img id="dnd_logo" src='https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png'>
                <br>
                <b> Welcome to the DnD bot. </b>
                <br> <br>
                <b> Dice roller </b>
                <div class="input-container" id="die-type-container">
                <label for="die-type">Number of Sides: </label>
                <input id="die-type" type="number" class="form-input" min="1" max="100" value="20" placeholder="Sides..."></input>
                </div>

                <div class="input-container" id="roll-num-container">
                <label for="roll-num">Number of rolls: </label>
                <input id="roll-num" name="roll-num" class="form-input" type="number" min="1" value="1" max="100" placeholder="Rolls..."></input>
                </div>

                <button onclick="roll()"> Roll dice! </button>
                <div id="outputdice"></div>
                <div id="totaldice"></div>
                <br>                

                <b> Name generator </b>
                <br>
                <form action="/namegen">
                <div class="input-container" id="name-gen-container">
                <label for="nameno">Number of names: </label>
                <input id="nameno" name="nameno" class="form-input" type="number" min="1" max="100" value="10" placeholder="Number..."></input>
                </div>

                <button> Generate names! </button>
                <br>
                <div id="outputname"></div>
                <div id="name-gen-output"></div>
                </form>
                </div>
                ''',
        "css": "/static/stylesheet.css",
        "js": "/static/dnd-roller.js"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

'''
def namegen(no):
    gennames = []
    for i in range(no):
        x = names[random.randint(0, len(names))]
        gennames.append(x)
        return gennames
'''