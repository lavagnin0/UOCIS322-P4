# UOCIS322 - Project 4 #
Brevet time calculator.
Author: Jeremy Lavagnino, jlavagni@uoregon.edu
## Overview

Reimplementation of the RUSA ACP controle time calculator with Flask and AJAX.

## About ACP controle times

That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). Some of the specifications are somewhat ambiguous, so the current RUSA ACP control time calculator ([https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html)) has been used to clarify them. Specifically, the table with minimum/maximum speeds has the boundary distances (such as 200 km) in multiple rows, making unclear which one to use. I determined that the first row the value appears in is always used (so for 200 km, that would mean a max speed of 34 km/h instead of 32), which is what my program uses. Additionally, I determined through experimentation with the online calculator that it rounds up to the nearest minute from 30+ seconds and down from 29 seconds and below, which is how I implemented the rounding behaviour in this program.


## Usage

Build a docker image starting in the brevets directory and then run it using your desired port. To use the website, simply input the distances from the start of the controle locations in either of the first two columns depending on whether you prefer to use miles or kilometers, and the start/close time columns will be calcualted and automatically filled in. Note that all distances are converted to km for backend calculations.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
