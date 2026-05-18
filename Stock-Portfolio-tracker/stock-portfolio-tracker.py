import csv
import os

# --- Hardcoded stock price dictionary ---
STOCK_PRICES = {
    "AAPL":  189.50,
    "TSLA":  248.00,
    "MSFT":  415.30,
    "GOOGL": 175.80,
    "AMZN":  195.60,
    "NVDA":  875.40,
    "META":  520.10,
    "NFLX":  625.80,
    "AMD":   165.20,
    "INTC":   31.45,
    "DIS":   112.30,
    "JPM":   198.50,
    "V":     278.40,
    "WMT":    68.20,
    "BABA":   78.90,
}

# --- Portfolio dictionary: symbol -> quantity ---
portfolio = {}


def show_available_stocks():
    print("\n📈 Available Stocks:")
    print(f"  {'Symbol':<8} {'Price (USD)':>12}")
    print("  " + "-" * 22)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:>11.2f}")
    print()


def add_stock():
    symbol = input("Enter stock symbol (e.g. AAPL): ").strip().upper()

    if symbol not in STOCK_PRICES:
        print(f"  ❌ '{symbol}' not found. Use 'list' to see available stocks.")
        return

    try:
        qty = int(input(f"Enter quantity of {symbol} shares: ").strip())
        if qty <= 0:
            print("  ❌ Quantity must be a positive number.")
            return
    except ValueError:
        print("  ❌ Invalid quantity. Please enter a whole number.")
        return

    if symbol in portfolio:
        portfolio[symbol] += qty
        print(f"  ✅ Added {qty} more shares of {symbol}. Total: {portfolio[symbol]} shares.")
    else:
        portfolio[symbol] = qty
        print(f"  ✅ Added {qty} shares of {symbol} at ${STOCK_PRICES[symbol]:.2f} each.")


def show_portfolio():
    if not portfolio:
        print("\n  Your portfolio is empty. Add stocks first!")
        return

    total = 0
    print("\n" + "=" * 52)
    print(f"  {'Symbol':<8} {'Price':>10} {'Shares':>8} {'Value':>12}")
    print("  " + "-" * 44)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<8} ${price:>9.2f} {qty:>8} ${value:>11.2f}")

    print("  " + "-" * 44)
    print(f"  {'TOTAL INVESTMENT':>28}   ${total:>11.2f}")
    print("=" * 52)


def save_to_txt():
    if not portfolio:
        print("  ❌ Portfolio is empty. Nothing to save.")
        return

    filename = input("Enter filename (without extension) [default: portfolio]: ").strip()
    if not filename:
        filename = "portfolio"
    filename += ".txt"

    total = 0
    with open(filename, "w") as f:
        f.write("=== STOCK PORTFOLIO REPORT ===\n\n")
        f.write(f"{'Symbol':<8} {'Price':>10} {'Shares':>8} {'Value':>12}\n")
        f.write("-" * 44 + "\n")
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            total += value
            f.write(f"{symbol:<8} ${price:>9.2f} {qty:>8} ${value:>11.2f}\n")
        f.write("-" * 44 + "\n")
        f.write(f"{'TOTAL INVESTMENT':>28}   ${total:>11.2f}\n")

    print(f"  ✅ Portfolio saved to '{filename}'")


def save_to_csv():
    if not portfolio:
        print("  ❌ Portfolio is empty. Nothing to save.")
        return

    filename = input("Enter filename (without extension) [default: portfolio]: ").strip()
    if not filename:
        filename = "portfolio"
    filename += ".csv"

    total = 0
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Price (USD)", "Shares", "Total Value (USD)"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            total += value
            writer.writerow([symbol, f"{price:.2f}", qty, f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{total:.2f}"])

    print(f"  ✅ Portfolio saved to '{filename}'")


def remove_stock():
    if not portfolio:
        print("  ❌ Portfolio is empty.")
        return
    symbol = input("Enter stock symbol to remove: ").strip().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"  ✅ {symbol} removed from portfolio.")
    else:
        print(f"  ❌ {symbol} is not in your portfolio.")


def print_menu():
    print("\n--- MENU ---")
    print("  1. List available stocks")
    print("  2. Add stock to portfolio")
    print("  3. View portfolio & total value")
    print("  4. Remove a stock")
    print("  5. Save as TXT")
    print("  6. Save as CSV")
    print("  0. Exit")


def main():
    print("\n🚀 Welcome to Stock Portfolio Tracker!")
    print("   Prices are hardcoded for demo purposes.\n")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_available_stocks()
        elif choice == "2":
            add_stock()
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            remove_stock()
        elif choice == "5":
            save_to_txt()
        elif choice == "6":
            save_to_csv()
        elif choice == "0":
            print("\n👋 Goodbye! Happy investing!\n")
            break
        else:
            print("  ❌ Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    main()