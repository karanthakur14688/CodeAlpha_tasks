# CodeAlpha — Python Programming Internship

Welcome to my **CodeAlpha Python Internship** repository!
This repo contains all 3 completed tasks as part of the internship program.

**Program:** Python Programming Internship — CodeAlpha

---

## 📁 Repository Structure

```
CodeAlpha_tasks/
├── Hangman-Game/             # Task 1 — Hangman Game
├── Stock-Portfolio-Tracker/  # Task 2 — Stock Portfolio Tracker
└── Chatbot/                  # Task 3 — Basic Chatbot 
```

---

## ✅ Tasks Overview

| # | Project | Description |
|---|---------|-------------|
| 1 | 🎮 Hangman Game | Text-based word guessing game |
| 2 | 📈 Stock Portfolio Tracker | Track & manage stock investments |
| 3 | 🤖 Basic Chatbot  | Keyword-based conversational chatbot |

---

## 🎮 Task 1 — Hangman Game

### About
A classic text-based Hangman game built with Python. The program selects a random word and the player guesses one letter at a time to uncover it before running out of attempts.

### Features
- Random word selection from a built-in word list
- Letter-by-letter guessing with visual feedback
- Tracks correct and incorrect guesses separately
- Limited number of wrong guesses (lives system)
- Displays the hangman ASCII art as lives decrease
- Prevents duplicate guess entries

### How to Run
```bash
cd Hangman-Game
python hangman.py
```

### Sample Gameplay
```
Word: _ _ _ _ _ _
Guess a letter: p
✅ Good guess!
Word: p _ _ _ _ _

Guess a letter: z
❌ Wrong! Lives remaining: 5
```

### Concepts Used
- `random` module for word selection
- Lists and string manipulation
- Loops and conditionals
- ASCII art rendering

---

## 📈 Task 2 — Stock Portfolio Tracker

### About
A Python-based stock portfolio tracking tool that lets users add, remove, and monitor their stock investments. Uses a hardcoded price dictionary with 15 real stock symbols for demo purposes — no API key or internet required!

### Available Stocks (15 supported)

| Symbol | Company | Symbol | Company |
|--------|---------|--------|---------|
| AAPL | Apple | NVDA | NVIDIA |
| TSLA | Tesla | META | Meta |
| MSFT | Microsoft | NFLX | Netflix |
| GOOGL | Google | AMD | AMD |
| AMZN | Amazon | INTC | Intel |
| DIS | Disney | JPM | JPMorgan |
| V | Visa | WMT | Walmart |
| BABA | Alibaba | | |

### Features
- 📋 List all 15 available stocks with live-style prices
- ➕ Add stocks to portfolio (supports adding more shares to existing holdings)
- 👁️ View full portfolio with per-stock value and grand total
- ❌ Remove stocks from portfolio
- 💾 Save portfolio report as `.txt` file
- 📊 Export portfolio data as `.csv` file
- Input validation with helpful error messages

### How to Run
```bash
cd Stock-Portfolio-Tracker
python stock_tracker.py
```
> No external libraries needed — uses only built-in `csv` and `os` modules!

### Menu Options
```
--- MENU ---
  1. List available stocks
  2. Add stock to portfolio
  3. View portfolio & total value
  4. Remove a stock
  5. Save as TXT
  6. Save as CSV
  0. Exit
```

### Concepts Used
- Dictionaries for stock price mapping and portfolio storage
- `csv` module for CSV export
- String formatting with f-strings and alignment
- Input validation with `try/except`
- File I/O for saving `.txt` and `.csv` reports

---

## 🤖 Task 3 — Basic Chatbot

### About
A friendly command-line chatbot built in pure Python — no external libraries needed! ChatBot responds to common greetings, questions, and commands using exact and keyword-based matching.

### Features
- Responds to greetings, questions, and casual conversation
- Two-layer matching: exact match + keyword/partial match
- Tells programming jokes 😄
- Handles unknown inputs with a helpful fallback message
- Clean exit on `bye`, `exit`, or `quit`

### How to Run
```bash
cd Chatbot
python chatbot.py
```

### Supported Commands

| Input | Response |
|---|---|
| `hello` / `hi` | Friendly greeting |
| `how are you` | Status reply |
| `what is your name` | Bot introduces itself |
| `who made you` | Origin story |
| `what can you do` | Lists capabilities |
| `tell me a joke` | Tells a programming joke |
| `help` | Shows available commands |
| `thanks` / `thank you` | Polite acknowledgement |
| `bye` / `exit` / `quit` | Exits the chatbot |

```

### Concepts Used
- Dictionaries for response mapping
- String methods (`.lower()`, `.strip()`, `in`)
- Loops and conditionals
- Input/output handling

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `random`, `string` (Hangman) · `csv`, `os` — no external libs (Stock Tracker) · No external libs (Chatbot)

---

## 🚀 Getting Started

Clone the repository and navigate to any task folder:

```bash
git clone https://github.com/karanthakur14688/CodeAlpha_tasks.git
cd CodeAlpha_tasks
```

Then follow the **How to Run** instructions under each task above.

---

## 👤 Author

**karan**
