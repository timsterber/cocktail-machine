from flask import Flask, render_template, jsonify, request
import sqlite3
import os
import time
#. from control import Control

app = Flask(__name__, template_folder="templates")

# Path to the database
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sqlite", "database", "cocktails.db")

#. control = Control()

def get_cocktails():
    """Fetch all cocktail names from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Cocktails")  # Fetch only the names
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]  # Extract names into a list

@app.route('/')
def index():
    # Fetch cocktail names
    cocktails = get_cocktails()
    return render_template('index.html', cocktails=cocktails)

# Logic for 
@app.route('/button/<cocktail>', methods=['POST'])
def button_action(cocktail):
    # Here you can handle any action, e.g., logging or database update
    print(f"Create cocktail: {cocktail}")  # Log to server or handle further actions
    time.sleep(5)
    #! HERE THE CODE FOR THE VALVE CONTROL
    #! 1. read cocktail values
    #! 2. start the process
    # Send a response back to the frontend
    return jsonify({"message": f"Button for {cocktail} clicked successfully!"})

@app.route('/settings/measuring', methods=['POST'])
def measuring_action():
    #. control.start_tpm()
    print("Measuring!")
    time.sleep(2)
    return jsonify({})

@app.route('/settings/calculate/<amount>', methods=['POST'])
def calc_measuring_action(amount):
    #. tpm = control.calc_tpm(amount)
    #print(f"Amount: {amount}")
    return jsonify({"amount" : amount})

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
