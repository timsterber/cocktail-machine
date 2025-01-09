# The Cocktail Machine

## 1. Inspiration & Plan
The inspiration for this project came from a spontaneous and amusing idea my friend and I had:  
We want to build a cocktail machine that features multiple bottle inputs and a single output. The goal is to make it as affordable as possible. Instead of using expensive pumps to dispense liquids into the glass, we plan to use valves instead.  

Here’s our initial design concept:  
![Design Idea](images/building_plan.png)

## 2. Components
The next step is deciding which computer to use for controlling the valves, ensuring precise amounts of liquid are dispensed into the funnel.  
For this, you can use a standard microcontroller like an ESP32 or Arduino.  

However, we chose a Raspberry Pi 4 to enable a user-friendly interface. By utilizing a touchscreen and running the Raspberry Pi in Kiosk Mode, it can directly boot into a Python-based application or web server for control.  

In addition to the Raspberry Pi, the machine will require:  
- 12 valves  
- 12 relays to control the valves  
- 10 meters transparent pvc hose (for changing after usage)
- 1 funnel

not necessary, but for design ideas:
- LED light pannel
- LED lights

Here is the electronic plan:

![Electronic](images/electronic.png)
\# Picture by: https://github.com/alex9849/CocktailPi

## 3. Saving all information
There are multiple solutions for saving data with a database. On this project we are using SQLite as our database, but you are totally free to use another one which suits your needs better. Then you just need to adapt the code to your requests.

    -> Install SQLite
    -> Create Databases
    -> Create Script for requests

SQLite database plan:

Name Table:
* Input
* Bottle Name

Recipes Table:
* Recipes Name
* Amout of every Input in ml
<br>=> Name | In1 | In2 | In3 | In4 | ...

1. Programming GUI in Python, NODE-RED or HTML
2. Buying the stuff
3. Building the machine

## 4. Inputs
We have 12 possible Inputs, so you can put your own cocktails in the database and it will automatically use them for the website.

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
We need to create a function to adjust the timing for the right amount of liquid for the glass.

## 7. Other TODOs
- DNS Server for website (e.g.: http://cocktail.app/...)
- WiFI Hostspot on Raspberry for connection

