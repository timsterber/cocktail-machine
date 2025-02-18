# The Cocktail Machine

## Inspiration & Plan  
The inspiration for this project came from a spontaneous and amusing idea my friend and I had:  
We want to build a cocktail machine that features multiple bottle inputs and a single output. The goal is to make it as affordable as possible. Instead of using expensive pumps to dispense liquids into the glass, we plan to use valves instead.

*Here’s our initial design concept:*  
![Design Idea](images/design_concept_initial.png)

After some changes, we completely redesigned our concept, so instead of using valves, we now use peristaltic pumps. The reason for this change is the pressure on the tubes when the bottles are full compared to when they are empty. Due to the physics involved, the liquid flows more slowly as the bottle empties.

*Our final design concept:*  
![Final Idea](images/design_concept_final.png)

## 1. Website

All cocktails will be displayed on the main page, where you can directly choose which cocktail you want to create.  
![index](images/website_list.png)

To change the input values (in ml), you can use the URL `/database`. It's very simple to use. Just type in the name of your drink and how many milliliters you want per input.

![database](images/website_database1.png)

When you create a new line, you'll see what you should write in the input field.  
![database](images/website_database2.png)

In the `/settings` tab, you can set up the TPM (time per milliliter). This is crucial so that your machine knows how long the motors should be enabled for the specific amount of liquid.  
1. Start the process (Button)  
2. Measure the amount of liquid that came out of the output and type it in  
3. Calculate the TPM  
![settings](images/website_settings.png)

## 2. Components  
The next step is deciding which computer to use for controlling the peristaltic motors, ensuring precise amounts of liquid are dispensed into the glass.  
For this, you can use a standard microcontroller like an ESP32 or Arduino.  

However, we chose a Raspberry Pi 4 to enable a user-friendly interface. By using your Raspberry Pi as both a web server and access point, you can directly connect your phone to the Wi-Fi and go on the website to control the machine.

In addition to the Raspberry Pi, the machine will require:  
- 12 peristaltic pumps (maximum)  
- 12 relays to control the valves  
- 10 meters of transparent PVC hose (for changing after usage)  
- Tube connectors  

Not necessary, but for design ideas:  
- LED light panel  
- LED lights  

Here is the electronic plan:

![Electronic](images/electronic.png)  
# Picture by: https://github.com/alex9849/CocktailPi

The pin assignment uses the following pins:

![Electronic](images/raspberrypi_pins.jpg)

| Inputs   | 1 | 2 | 3 |  4 |  5 |  6 |  7 | 8 |  9 | 10 | 11 | 12 |
|----------|---|---|---|----|----|----|----|---|----|----|----|----|
| GPIO Pin | 2 | 3 | 4 | 17 | 27 | 22 | 10 | 9 | 11 |  5 |  6 | 13 |

## 3. Saving All Information  
There are multiple solutions for saving data with a database. In this project, we are using SQLite as our database, but you are free to use another one that suits your needs better. You would just need to adapt the code to your requirements.

    -> Install SQLite  
    -> Create Databases  
    -> Create Script for requests  

SQLite database plan:

**Recipes Table:**  
* Recipe Name  
* Amount of each input in ml  
<br>=> Name | In1 | In2 | In3 | In4 | ...  

1. Program GUI in Python with Flask / Quart  
2. Buy the materials  
3. Build the machine  

## 4. Inputs  
We have 12 possible inputs, so you can add your own cocktails to the database, and it will automatically use them for the website. You can also use fewer inputs, but if you want to use more, you’ll need to create a new database with more entries and edit the `control_db.py` script so that it works.  
You'll also need to adapt all other files, like `database.html`.

## 5. Database Commands

```sql
DROP TABLE table_name;      -- Delete Table  
DELETE FROM table_name;     -- Delete all entries  
SELECT * FROM table_name;   -- Show whole Table  

.read database/schema.sql   -- Create Table for Cocktails  
.schema                     -- Verify Schema  
.tables                     -- List Tables  
```

## 6. Programming the Valves  
After building the website, we need to create functions to control the liquids (Inputs).  
We need to create a function to adjust the timing for the correct amount of liquid for the glass.

For this purpose, I created a class called [control_rpi.py](website/control_rpi.py), which gives you the ability to easily control the Raspberry Pi pins of your connected motors.

There is also a test script if you are using your PC to program and don’t have the RPi module loaded. In this case, just replace the dependency in `website.py` from `from control_rpi ...` to `from control_rpi_test ...`.

For database connection, there is an extra script, [control_db](website/control_db.py), which can be used to clear the database and fill it with new entries.

## 7. Changing Program Code or Style  
Just a quick note if you change the [styles.css](website/static/styles.css): If you do so, please keep in mind that you may have to hard reload your web browser (Ctrl + F5 in Chrome).  
This is caused by the browser caching the `styles.css` file. Sometimes, it won’t reload it after you visit the website once.

## 8. Wi-Fi Hotspot on Raspberry for Connection  
For more information on how to set up the Wi-Fi hotspot on the Raspberry Pi, please see [RPI.md](RPI.md).

## 9. Other To-Dos  
- DNS Server for the website (e.g., http://cocktail.app/...)
