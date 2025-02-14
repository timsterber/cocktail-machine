from quart import Quart, render_template, jsonify, request
import sqlite3
import os
from control import Control
import asyncio

app = Quart(__name__, template_folder="templates")

# Path to the database
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "cocktails.db")

control = Control()

def get_cocktails():
    """Fetch all cocktail names from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Cocktails")  # Fetch only the names
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]  # Extract names into a list

def cocktail_values_by_name(name):
    """Fetch a cocktail by its name."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Cocktails WHERE name='{name}'")
    row = cursor.fetchone()
    conn.close()
    return row[2:]      # Return only the values

@app.route('/')
async def index():
    # Fetch cocktail names
    cocktails = get_cocktails()
    return await render_template('index.html', cocktails=cocktails)

# Logic for 
@app.route('/button/<cocktail>', methods=['POST'])
async def button_action(cocktail):
    # Here you can handle any action, e.g., logging or database update
    print(f"Create cocktail: {cocktail}")  # Log to server or handle further actions
    
    data = cocktail_values_by_name(cocktail)
    control.check_values(data)
    
    tasks = []
    
    for i in range(len(data)):
        if(data[i] != 0):
            print(f"Pouring {data[i]} ml from Input {i+1}")
            tasks.append(start_stop_task(data[i], i+1))
            
    await asyncio.gather(*tasks)
    
    # Send a response back to the frontend
    return jsonify({"message": f"Button for {cocktail} clicked successfully!"})

async def start_stop_task(ml, input):
    if ml != 0:
        await control._start(control.pins[input - 1])  # Start the pouring process
        await asyncio.sleep(ml * control.tpm)  # Wait for the specified time
        await control._stop(control.pins[input - 1])  # Stop the pouring process

@app.route('/settings/measuring', methods=['POST'])
async def measuring_action():
    await control.process_time(10, 1)     # 10seconds pouring from Input 1
    return jsonify({})

@app.route('/settings/stop_website', methods=['POST'])
async def stop_website():
    os.system("sudo poweroff")  # This will stop the script
    return jsonify({"message": "Server stopping."})

@app.route('/settings/calculate/<amount>', methods=['POST'])
async def calc_measuring_action(amount):
    tpm = control.calc_tpm(int(amount))
    print(f"New time per milliliter: {tpm}")
    return jsonify({"tpm" : tpm})

@app.route('/settings/flow', methods=['POST'])
async def flow_action():
    data = await request.get_json()
    input = data.get('input')
    state = data.get('value')
    assert(input != None and state != None)
    await control._start(input) if state else await control._stop(input)
    return jsonify({"input": input, "state": state})


@app.route('/settings', methods=['GET', 'POST'])
async def settings():
    return await render_template('settings.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, use_reloader=False)
