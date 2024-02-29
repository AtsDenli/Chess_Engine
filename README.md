# Chess_Engine
A neural network for playing chess.

The dataset used to train the neural network can be found here: https://www.kaggle.com/datasets/arevel/chess-games.

The script chessGamePrep.py was used to filter out the data so that only games with high elo players playing with time constraints longer than bullet chess were used to train the neural network. It also filtered out games that had notation which the code isn't built to recognise.

I used a lot of ideas from https://www.youtube.com/watch?v=aOwvRvTPQrs&t=524s. It was very useful and I would recommend it to anyone building a similar project.

I also used some ideas from https://www.youtube.com/watch?v=mozBidd58VQ. I would recommend it to anyone who is new to Pytorch programming.

This is still in progress, although the model can train, I haven't built the functionality to input and output moves yet. This will be coming soon. To train the model yourself, simply download the data from the above link, run chessGamePrep.py on this data, and then add engine.py and engineHelp.py into the same directory, and run engine.py 