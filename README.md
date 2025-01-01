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

## 4. Programming
After some research, it was possible to build a website in python with flask.
Now there are several actions we need to identify.

## 5. Inputs
We have 12 possible Inputs.

- Cuba Libre
    + Cola, Rum
- Mojito
    + Soda, Rum, Limettensaft
- Vodka Lemon
    + Soda, Vodka, Zitronensaft
- Long Island Iced Tea
    + Vodka, Rum, Tequila, Gin, Triple Sec, Zitronensaft, Cola
- Tequila Sunrise
    + Tequila, Orangensaft
- 


1. Vodka
2. Rum
3. Gin
4. Tequila
5. Triple Sec
6. Korn
7. Cola
8. Fanta
9. Sprite
10. Cranberrysaft
11. Zitronensaft
12. Orangensaft

- Cola Vodka
- Cola Rum
- Sprite Vodka
- ...

## 6. Database Commands

```sql
DROP TABLE table_name;      -- Delete Table
DELETE FROM table_name;     -- Delete all entries
SELECT * FROM table_name;   -- Show whole Table

.read database/schema.sql   -- Create Table for Cocktails
.schema                     -- Verify Schema
.tables                     -- List Tables
```