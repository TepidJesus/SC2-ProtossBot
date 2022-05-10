# SC2-ProtossBot
[PLANNING] - My first attempt at a Star Craft 2 bot using Stable baselines 3.

This bot will be specific to the Protos race. The bot will be provided with sets of scripted actions (Outlines Below) which can be picked from at any given instance.

Using the OpenAI Gym the RNN will trained to make decisions that support my desired strategy.


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
