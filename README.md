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

## 3. TODO
1. Programming GUI in Python, NODE-RED or HTML
2. Buying the stuff
3. Building the machine