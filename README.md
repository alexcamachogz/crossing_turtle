# Turtle Crossing Game

The Turtle Crossing Game is a simple arcade-style game implemented using the Turtle graphics library in Python. The objective of the game is to help the turtle cross a busy road without getting hit by the cars. The game features a player-controlled turtle, moving cars, a scoreboard to track the player's progress, and increasing difficulty levels.

![Imgur](https://i.imgur.com/hVBTBN4.png)

## Feature

* Control the turtle using the Up arrow key or the 'w' key on the keyboard.
* Dodge the moving cars and safely reach the other side of the road.
* The game speed and the number of cars increase as the player progresses.
* The game ends if the turtle collides with any of the cars.
* The score increases each time the turtle successfully crosses the road.

## Installation

1. Make sure you have Python 3.x installed on your machine. 
2. Clone this repository to your local machine or download the ZIP file and extract it. 
3. Open a terminal or command prompt and navigate to the project directory. 

## Usage
1. Run the game by executing the following command in the terminal or command prompt:
``` python main.py ```
2. Use the Up arrow key or the 'w' key to move the turtle upwards.
3. Avoid the moving cars and try to reach the other side of the road.
4. The score will increase each time the turtle successfully crosses the road.
5. If the turtle collides with any of the cars, the game ends and the final score is displayed.

## Customization

You can customize certain aspects of the game by modifying the following variables in the code:

* `STARTING_MOVE_DISTANCE`: Initial speed of the cars.
* `MOVE_INCREMENT`: Amount by which the car speed increases after each successful crossing.
* `COLORS`: List of colors used for the cars.
* `screen.setup(width, height)`: Set the dimensions of the game window.

Feel free to experiment with these variables to adjust the difficulty and visual appearance of the game.

## Contributing
Contributions to the Turtle Crossing Game project are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.

## Acknowledgments

* This project was inspired by the classic Frogger game.
* The Turtle graphics library in Python makes it easy to create simple games and visualizations.

Enjoy the game and have fun crossing the road with the turtle!

## License
> This project is licensed under the [MIT License](LICENSE)
