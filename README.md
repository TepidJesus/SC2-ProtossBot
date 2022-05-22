# SC2-ProtossBot
[PLANNING] - My first attempt at a Star Craft 2 bot using Stable baselines 3.

This bot will be specific to the Protos race. The bot will be provided with sets of scripted actions (Outlines Below) which can be picked from at any given instance.

Using the OpenAI Gym, the RNN will be trained to make decisions that support my desired strategy.


## Possible Macro Actions:
- Skirmish / Harass Enemy (Attack but never fully engage)
- Retreat (Perform a hasty retreat to a safe area)
- Last Stand (Dump all available resources into current engagement)
- Scout (Scout unseen areas of the map)
- Attack X (Attack X unit, units, structure, structures)
- Defend X (Defend X point, unit, structure)
- Take Objective (Expand Nexus to new area)
- Build X (Build X Unit, Structure)

## Desired RNN Data Inputs
- Percentage of map seen by allied units
- Composition of allied army *
- Composition of sighted enemy units *
- Allied Supply
- Estimated enemy supply
- Allied Gas
- Allied Minerals
- Enemy structures seen *
- Allied Structures *
* = Investigating how to quantify.

## Build Order:
- @14 Supply: Build Pylon At Natural
- @16 Supply: Build Gate At Natural
- @17 Supply: Take First Gas
- @20 Supply: New Nexus And Core At Natural
    - Once Core Finishes, Chrono Core and Warp-Gate And Natural
- @21 Supply: Take Second Gas
- @22 Supply: New Pylon At Main
- @150 Minerals, 100 Gas: Robotics
    - Train Observer
    - Train Immortal
- @33 Supply: Build Pylon at Main + Two Gates on Pylon
- @50 Supply: Build Twilight Council At Main (Charge It)
- @15 Workers take both gas at Natural
- @60 Supply: Build 6 WarpGates + Required Pylons + Archives
- @70 Supply:
 
## General:
- Chrono Boost All Tech Units + Upgrades
- Probes built continuously to ensuring saturation
- Always monitoring for supply block. Available Supply - Queued Units > 0