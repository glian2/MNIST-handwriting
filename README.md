# MNIST-sudoku

This project utilizes aspects of computer vision paired with the linear programming provided by Python to solve a sudoku puzzle.

A few things to note:

The pre-trained neural network that is provided is trained on the MNIST handwritten dataset (although this works very well for handwritten numbers, it does not perform as well with typset numbers).

To run this program, keras and Tensorflow v2.6.0 are used along with the PuLP library that is utilized by Python for Linear Programming functionality.

To begin, the classifier has to be run in order to train the Neural Network to recognize digits (in this case the dataset is the MNIST dataset).  Possible future updates will be more suited to Sudoku as a typeset dataset would be more appropriate for image recognition. 

Train and test the Neural Network by running the ```digit_classifier.py``` file which will provide a h5 model file in the output folder.

The next part is to run the main file with the h5 model and a specific image.

arguments can be passed to the main file as such:

``` main.py -m output/digit_classifier.h5 -i 12.jpg```

The output of the program (if it runs correctly ie: recognition of the appropriate digits in the Sudoku image) will be displayed in the ```sudokuout.txt``` file

Linear Programming is used to actually solve the Sudoku puzzle itself.  More details can be found at the following:
https://www.mathworks.com/help/optim/ug/sudoku-puzzles-problem-based.html

