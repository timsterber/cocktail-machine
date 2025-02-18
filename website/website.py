from quart import Quart, render_template, jsonify, request
import asyncio
import os

# Own functions
from control_rpi_test import Control_RPI
from control_db import *


app = Quart(__name__, template_folder="templates")

# Path to the database


control = Control_RPI()
db = Control_DB()

@app.route('/')
async def index():
    # Fetch cocktail names
    cocktails = db.get_cocktails_names()
    return await render_template('index.html', cocktails=cocktails)

@app.route('/cocktail/<cocktail>', methods=['POST'])
async def button_action(cocktail):
    # Here you can handle any action, e.g., logging or database update
    print(f"Create cocktail: {cocktail}")  # Log to server or handle further actions
    
    data = db.cocktail_values_by_name(cocktail)
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
    await control._start(control.pins[int(input) - 1]) if state else await control._stop(control.pins[int(input) - 1])
    return jsonify({"input": input, "state": state})


@app.route('/settings', methods=['GET', 'POST'])
async def settings():
    return await render_template('settings.html')

@app.route("/database")
async def database():
    cocktails = db.get_cocktails()
    return await render_template("database.html", cocktails=cocktails)

@app.route("/database/save", methods=["POST"])
async def save_database():
    data = await request.get_json()
    
    # Check if there are empty values and fill them with 0
    for index, cocktail in enumerate(data):
        if data[index][0] == '':
            return {"message": "Missing Attribut 'name'."}, 400
        data[index] = [0 if i == '' else i for i in cocktail]

    # Clear the table and add the new data
    db.clear_table()
    for cocktail in data:
        db.add_cocktail(cocktail)
    return {"message": "Saved successfully!"}, 200

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=80, debug=True)
    except KeyboardInterrupt:
        control.reset_pins()
        db.close()