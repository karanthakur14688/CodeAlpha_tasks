# 📈 Stock Portfolio Tracker

A simple command-line Python project that calculates total investment value based on manually defined stock prices.

---

## 🎯 Project Goal

Build a stock tracker that:
- Takes stock name and quantity as user input
- Uses a hardcoded dictionary of stock prices
- Calculates total investment value
- Saves the result to a `.txt` or `.csv` file

---

## 📁 Project Structure

```
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py   # Main Python file
├── README.md                    # Project documentation
├── portfolio.txt                # (Generated after saving)
└── portfolio.csv                # (Generated after saving)
```

---

## 🚀 How to Run

```bash
python3 stock_portfolio_tracker.py
```

---

## 📋 Menu Options

| Option | Action |
|--------|--------|
| `1` | List all available stocks with prices |
| `2` | Add a stock to your portfolio |
| `3` | View portfolio and total investment |
| `4` | Remove a stock from portfolio |
| `5` | Save portfolio as `.txt` file |
| `6` | Save portfolio as `.csv` file |
| `0` | Exit the program |

---

## 📦 Available Stocks (Hardcoded)

| Symbol | Company | Price (USD) |
|--------|---------|-------------|
| AAPL | Apple Inc. | $189.50 |
| TSLA | Tesla Inc. | $248.00 |
| MSFT | Microsoft Corp. | $415.30 |
| GOOGL | Alphabet Inc. | $175.80 |
| AMZN | Amazon.com Inc. | $195.60 |
| NVDA | NVIDIA Corp. | $875.40 |
| META | Meta Platforms | $520.10 |
| NFLX | Netflix Inc. | $625.80 |
| AMD | Advanced Micro Devices | $165.20 |
| INTC | Intel Corp. | $31.45 |
| DIS | Walt Disney Co. | $112.30 |
| JPM | JPMorgan Chase | $198.50 |
| V | Visa Inc. | $278.40 |
| WMT | Walmart Inc. | $68.20 |
| BABA | Alibaba Group | $78.90 |

---

## 🧠 Key Concepts Used

| Concept | Where Used |
|---------|------------|
| `dictionary` | `STOCK_PRICES` stores symbol → price |
| `input/output` | User enters stock symbol and quantity |
| `basic arithmetic` | `price × quantity = total value` |
| `file handling` | Save to `.txt` and `.csv` |
| `functions` | Each feature is a separate function |
| `loops` | Menu keeps running until user exits |

---

## ⚙️ Requirements

- Python 3.x
- No external libraries needed (uses built-in `csv` and `os` modules)