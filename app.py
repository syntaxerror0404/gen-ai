from flask import Flask, render_template
import json
import random

app = Flask(__name__)

# Load cat facts from a JSON file (or embed directly)
try:
    with open('cat_facts.json', 'r') as f:
        cat_facts = json.load(f)
except FileNotFoundError:
    cat_facts = [
        {"fact": "Cats are cool!", "source": "Me"},
        {"fact": "Another cat fact!", "source": "Also me"}
    ]  # Default facts if file not found

def get_random_fact():
    return random.choice(cat_facts)

@app.route('/')
def index():
    fact = get_random_fact()
    return render_template('index.html', fact=fact)

if __name__ == '__main__':
    app.run(debug=True)
