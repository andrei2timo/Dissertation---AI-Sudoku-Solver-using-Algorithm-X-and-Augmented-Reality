![Version Tag](https://img.shields.io/badge/Version-1.0.1-blue.svg)
[![Python Tag](https://img.shields.io/badge/Python-3-green.svg)](https://www.python.org/)
[![OpenCV Tag](https://img.shields.io/badge/OpenCV-4.2.0-yellow.svg)](https://opencv.org/)
[![PyTorch Tag](https://img.shields.io/badge/PyTorch-1.6.0+cpu-orange.svg)](https://pytorch.org/)
[![PyGame Tag](https://img.shields.io/badge/PyGame-1.9.6-blueviolet.svg)](https://www.pygame.org/)


# <img width="64" height="64" src="./.images/game_logo.png"> &nbsp; AI Sudoku solver -

This project aims to solve any sudoku of N dimension, where N is a non-prime. The project uses pygame for creating the Graphical User Interface. The project is implemented in two forms -

- An option to load an image saved on the system or use the webcam to feed image to the program and then play the game on the system.
- An option to use <b>Augmented Reality</b> and solve the sudoku by showing the puzzle to the webcam.

The project uses <i>[Dancing Links](https://en.wikipedia.org/wiki/Dancing_Links)</i> in the form of <i>[Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)</i> to find the solution of the Sudoku puzzle. Sudoku is a well known NP-Complete problem and Algorithm X is a means of implementing a form of greedy depth first search to find the appropriate solution. For more understanding on the Sudoku Algorithm, read [here](./Sudoku/README.md). For understanding the Image Processing approach, read [here](./Image_Processing/README.md).


## Index -

- [Introduction](#--visionxn-sudoku--)
- [Index](#index--)
- [Installation](#installation--)
    - [Installing Pytorch](#1--install-the-necessary-dependencies-installing-pytorch)
    - [Installing other requirements](2--installing-other-requirements)
- [How to Play](#how-to-play--)
- [Game Images](#game-images--)
- [Files in the repository](#files-in-the-repository--)
- [Bibliography](#bibliography)

## Installation -

##### 1.  Install the necessary dependencies - Installing Pytorch

Find the suitable pytorch release for your system [here](https://pytorch.org/get-started/locally/).

![Installation Image](./.images/installation.png)

In my case, this command was used -

```bash
pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

##### 2.  Installing other requirements

```bash
pip3 install -r requirements.txt

or

pip install -r requirements.txt
```

##### 3.  Clone the repository to your local machine:

```
git clone https://github.com/andrei2timo/Dissertation---AI-Sudoku-Solver-using-Algorithm-X-and-Augmented-Reality.git
```

##### 4.  Navigate to the cloned repository:

```
cd Dissertation---AI-Sudoku-Solver-using-Algorithm-X-and-Augmented-Reality
```

##### 5.  Run the code:

```
python3 main.py
```
If you want to solve a Sudoku puzzle from an image, add the image path as an argument when running the code:

```
python3 main.py path/to/image.jpg
```

## How to play -

To play the game using GUI -

```bash
python3 main.py
```

To use the sudoku solver in CLI, edit the [file](./cli_main.py) according to the problem and run -

```bash
python3 cli_main.py
```

## Game Images -

<p align="center">

<img width="480" height="480" src="./.images/Demo/1.png">
<br>Opening Screen<br><br>

<img width="480" height="480" src="./.images/Demo/2.png">
<br>Play Game<br><br>

<img width="480" height="480" src="./.images/Demo/3.png">
<br>Sample Game Loaded<br><br>

<img width="480" height="480" src="./.images/Demo/4.png">
<br>Load from file<br><br>

<img width="480" height="480" src="./.images/Demo/5.png">
<br>Select File<br><br>

<img width="480" height="480" src="./.images/Demo/6.png">
<br>Succesfully Loaded<br><br>

<img width="480" height="480" src="./.images/Demo/7.png">
<br>Load from Camera: 9 X 9<br><br>

<img width="480" height="480" src="./.images/Demo/8.png">
<br>Playing the game and check if the user made any errors<br><br>

<img width="480" height="480" src="./.images/Demo/9.png">
<br>Game won message<br><br>

<img width="480" height="480" src="./.images/Demo/10.png">
<br>Solving using the Solve Button<br><br>

<img width="480" height="480" src="./.images/Demo/11.png">
<br>Augmented Reality Option<br><br>

<img width="480" height="480" src="./.images/Demo/12.png">
<br>Augmented Reality Test: 9 X 9 puzzle 1 and solution<br><br>

<img width="560" height="480" src="./.images/Demo/13.png">
<br>Augmented Reality Test: 9 X 9 puzzle 2 and solution<br><br>

<img width="560" height="480" src="./.images/Demo/14.png">
<br>Augmented Reality Test: 9 X 9 puzzle 3 and solution<br><br>

<img width="560" height="480" src="./.images/Demo/15.png">
<br>Augmented Reality Test: Displaying error message<br><br>

</p>

### Files in the Repository -
The files in the repository are :

#### GUI -

-   ##### \_\_init__.py
    The \_\_init__.py file is to make Python treat directories containing the file as packages.

-   ##### button.py
    This file contains the class for implementing a pygame button.

-   ##### camera_windows.py
	This file contains the class for implementing a camera screen in pygame.

#### Image_Processing -

-   ##### data
    This directory contains the images of digits used as the training dataset for the image classifier.
    It contains images pertaining to digits of the char74k dataset.

-	##### char74k-cnn.pth
	It is the file containing the weights of the trained model on the `data` directory.

-	##### char74k_dataset.tgz
	This zip file contains the complete char74k dataset.

-   ##### classifier.py
    This file contains the CNN Classifier for digit recognition.

-   ##### \_\_init__.py
    The \_\_init__.py file is to make Python treat directories containing the file as packages.

-   ##### process_image.py
	This file contains the class for recognition of the sudoku from image.

-   ##### pytorch_gpu_assist.py
	This file contains helper functions to implement training on GPUs.

-   ##### README.md
    This file contains details about the algorithm and its implementation.

#### Samples
This directory contains sample images of sudoku puzzles that can be used as test cases for loading the image from file option in the program.

#### Sudoku -

-   ##### DancingLinks.pdf
    This is a copy of the original paper written by `Donald Knuth` on the concept of Dancing Links.

-   ##### \_\_init__.py
    The \_\_init__.py file is to make Python treat directories containing the file as packages.

-	##### README.md
    This file contains details about the algorithm and its implementation.

-   ##### sudoku.py
	This file contains class to solve Sudoku puzzle.

#### .images
This directory contains the images for the icons and other media for the README File.

#### cli_main.py
This file can be used to solve sudoku of any dimension using CLI.

#### game_window.py
This file contains the class for implementing the GUI for the program.

#### \_\_init__.py
The \_\_init__.py file is to make Python treat directories containing the file as packages.

#### main.py
This file is used as the driver code to start the program.

#### README.md
The Description file containing details about the repository. The file that you looking at right now.

#### requirements.txt
This file contains the respective packages needed to be installed. To install the respective packages, use -

#### sample.npy
This file contains the default sudoku puzzle which will get loaded incase not last loaded file is found.

<b>Fun Fact</b>: <i>This specific puzzle is designed to work against backtracking as a solution for sudoku and will take almost forever to solve it using backtracking.</i>

## Bibliography

- <b>Game Icon:</b> Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [flaticons.com](https://www.flaticon.com/).
- <b>Camera Icon:</b> Icon made by [Freepik](https://www.flaticon.com/free-icon/camera_2088898) from [flaticons.com](https://www.flaticon.com/).
- <b>Home Icon:</b> Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [flaticons.com](https://www.flaticon.com/).
- <b>Rounded Rectangle for Buttons:</b> The code for making rounded rectangle surface in pygame is adapted from [here](https://www.pygame.org/project-AAfilledRoundedRect-2349-.html).
- <b>Char74k Dataset:</b> The dataset used for training the CNN to recognize the digits can be found [here](
http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/).
- <b>CNN Model:</b> The Model Architecture is adapted from [here](https://www.kaggle.com/juiyangchang/cnn-with-pytorch-0-995-accuracy).
- <b>Sudoku Solver:</b> The code for implementing Sudoku as an exact cover problem is adapted from [here](https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html).

[![Developers Tag]( https://img.shields.io/badge/Developer-andrei2timo-blue.svg )]( https://github.com/andrei2timo )<br>
