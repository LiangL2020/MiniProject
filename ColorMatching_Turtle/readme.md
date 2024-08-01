# Color Matching Turtle (碰碰龟) [July 2024] 
This summer, I've seen this mini game super popular on TikTok live streams, and I'm eager to play as well. This folder is to mimic the game in the simplest term for me to enjoy without having to pay them and get lots of turtles in my house (which is almost useless for me). 

## Game Overview (How to play) 
You start with a certain (/any) number of turtles; the turtles are in a blind bag so you have no idea what colors you have (There are usually around 10 different colors of turtles and the board has 9 slots [slots 1-9]). You place them in order (IMPORTANT) on the board. You check for special turtles (usually with different patterns on the back) when placing; you gain an extra turtle in replacement for special turtles (special turtles don't stay for color match). After board has been filled (or turtles ran out), you check for match: 
- THREE in streak (like winning tic-tac-toes) gives you 3 extra turtles (or 5 or more depends)
- PAIRS (in any position) gives you 1 extra turtle. 
- the matched turtles are now yours (and will be shipped to you, technically) 

If the board is cleared (all turtles have a match), then you gain extra 5 (or more) turtles. If the board is full and has no match, your turtle match in holding position (slots 10 and so on). It just won't have match of threes. The game stops when you run out of turtles (completely, meaning you have no way of gaining more as well). 

## Files Overview 
- main.py contains the main loop of the game. You should start playing the game from main.py. It handles mouse/keyboard events and scene changes. 
- scene_*.py contains different scenes of the game. It handles displaying scenes and handles specific actions within the scene. 
- button.py contains the button class to create buttons easier. 
- lib.py contains global variables and functions. 
