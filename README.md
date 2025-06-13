# blackjack-hi-lo
# 🃏 OpenCV Blackjack Card Detector

This project is a Python application that uses OpenCV to detect playing cards from a webcam feed and calculate their value in a Blackjack game.

## Overview

- Detects and identifies playing cards in real-time using computer vision.
- Calculates the Blackjack score of the detected hand.
- Displays the results (card names, score, FPS) directly on the camera feed.
- Works with any standard USB webcam.

##  Blackjack Scoring Rules

| Card   | Value     |
|--------|-----------|
| 2–10   | Face value |
| J, Q, K| 10         |
| Ace    | 11 (or 1, if total exceeds 21) |


##  Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Numpy

##  How to Run

1. Clone this repository or download the source code.
2. Make sure your webcam is connected.
3. Ensure the `Card_Imgs/` folder contains the correct card rank and suit images named exactly as:
   - Ranks: `Ace.jpg`, `Two.jpg`, ..., `King.jpg`
   - Suits: `Hearts.jpg`, `Spades.jpg`, `Clubs.jpg`, `Diamonds.jpg`
4. Run the main script:

```bash
python cam_blackjack.py
