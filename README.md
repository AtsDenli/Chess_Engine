# Chess_Engine
A neural network for playing chess.

The dataset used to train the neural network can be found here: https://www.kaggle.com/datasets/arevel/chess-games.

The script chessGamePrep.py was used to filter out the data so that only games with high elo players playing with time constraints longer than bullet chess were used to train the neural network. It also filtered out games that had notation which the code isn't built to recognise.

I used a lot of ideas from https://www.youtube.com/watch?v=aOwvRvTPQrs&t=524s. I used it for inspiration and didn't copy the code. It was very useful and would recommend it to anyone building a similar project.