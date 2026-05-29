# 🤖 Basic Chatbot — Simple Rule-Based Chatbot in Python

---

## 📌 About the Project

**Basic Chatbot** is a simple rule-based chatbot built using core Python concepts.  
It accepts user input from the terminal and replies with predefined responses based on what the user types.

This project was built as **Task 4** of a Python learning roadmap to practice:
- `if-elif` conditions
- Functions
- Loops
- Input/Output
- Dictionaries

---

## 🎯 Features

- 💬 Responds to common inputs like `hello`, `how are you`, `bye`
- 📖 Uses a **dictionary** for clean and scalable response mapping
- 🔍 Supports both **exact match** and **keyword match**
- 🚫 Handles **empty input** gracefully
- 👋 Exits on `bye`, `quit`, or `exit`
- 😄 Friendly personality with emojis
- 🎤 Tells jokes on demand

---

## 🗂️ Project Structure

```
chatbot/
│
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## ▶️ How to Run

### 1. Run the chatbot
```bash
python chatbot.py
```

---

## 🧠 Key Concepts Used

| Concept        | Where Used                                      |
|----------------|-------------------------------------------------|
| `if-elif-else` | Matching user input to responses                |
| `Functions`    | `get_response()` and `run_chatbot()`            |
| `while` loop   | Keeps the chatbot running until user exits      |
| `Dictionary`   | Stores all predefined responses cleanly         |
| `input/print`  | Taking user input and displaying bot response   |
| `.lower()`     | Makes matching case-insensitive                 |
| `.strip()`     | Removes accidental leading/trailing spaces      |

---

## 👨‍💻 Author

**Karan**  
 
---

## 📄 License

This project is open-source and free to use for learning purposes.