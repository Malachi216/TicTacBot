### **Tic Tac Toe Symbol Classifier with Minimax AI**

---

#### **Project Overview**
This project implements a system to classify Tic Tac Toe board states from images and predict the next optimal move using a trained Convolutional Neural Network (CNN) and the Minimax algorithm. The project is capable of:
1. Identifying `X`, `O`, and blank cells from images of Tic Tac Toe boards.
2. Visualizing the board state with clear markings for `X`, `O`, and predicted moves.
3. Using Minimax to calculate the best possible move for `O` (computer).

---

#### **Key Features**
1. **CNN Model**:
   - Trained to classify Tic Tac Toe symbols (`X`, `O`, blank) from grayscale images.
   - Architecture:
     - Convolutional layers for feature extraction.
     - Max-pooling for dimensionality reduction.
     - Fully connected layers for classification.

2. **Minimax Algorithm**:
   - Implements a recursive algorithm to calculate the best move for `O`.
   - Handles game-winning, losing, and tie scenarios.

3. **Visualization**:
   - Displays the current board state with:
     - `X` and `O` in blue.
     - Predicted next move for `O` highlighted in green.

---

#### **Workflow**
1. **Image Classification**:
   - Input: Image of the Tic Tac Toe board.
   - Output: Board state (`X`, `O`, blank) as a 2D list.

2. **Move Prediction**:
   - Uses the classified board state to compute the best move for `O` using the Minimax algorithm.

3. **Visualization**:
   - Displays the current board and highlights the next predicted move.

---

#### **Setup Instructions**
1. **Dependencies**:
   - Install required libraries:
     ```bash
     pip install tensorflow keras matplotlib numpy opencv-python
     ```

2. **Training the Model**:
   - Train the CNN model on labeled data of Tic Tac Toe symbols.
   - Save the trained model for inference.

3. **Running the System**:
   - Load an image of the Tic Tac Toe board.
   - Use the trained model to classify each cell.
   - Predict the next move and visualize the board.

---

#### **File Structure**
```
.
├── data/
│   ├── train/       # Training dataset
│   ├── test/        # Testing dataset
├── model/
│   └── tic_tac_toe_model.h5  # Pre-trained CNN model
├── scripts/
│   ├── train_model.py       # CNN training script
│   ├── classify_board.py    # Board classification script
│   ├── minimax_ai.py        # Minimax implementation
│   └── visualize_board.py   # Board visualization script
└── README.md                # Project overview and instructions
```

---

#### **Usage Example**
```python
from classify_board import classify_board
from visualize_board import visualize_board_with_next_move

# Load an image
image_path = "path_to_board_image.png"

# Classify board state
board_state = classify_board(image_path)

# Visualize board and predict next move
visualize_board_with_next_move(board_state)
```

---

#### **Future Improvements**
1. Integrate additional heuristics into the Minimax algorithm for faster decision-making.
2. Extend functionality for variable board sizes (e.g., 4x4 Tic Tac Toe).
3. Enhance CNN model accuracy with more robust training data.

---

Let me know if you need additional details or edits for this!
