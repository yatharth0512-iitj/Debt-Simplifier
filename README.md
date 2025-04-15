
# 💸 Cashflow Minimizer Visualizer

A Streamlit web application to visualize and simplify debt transactions among a group of people. Instead of tracking who owes what to whom manually, this app helps you:
- Input multiple debt transactions
- View the original debt network
- Simplify and minimize the number of transactions needed to settle debts
- Visualize both original and simplified debt graphs

---

## 🚀 Features

- Add multiple transactions between any people
- Prevents invalid transactions (e.g., owing to self)
- Clear all transactions with one click
- Visualizes the debt network before and after simplification using network graphs

---

## 🧑‍💻 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [NetworkX](https://networkx.org/) – For graph operations and debt visualization
- [Matplotlib](https://matplotlib.org/) – For rendering graphs

---

## 📦 Installation

1. **Clone the repository / unzip project**
```bash
git clone https://github.com/yourusername/debt-simplifier.git
cd debt-simplifier
```

2. **(Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
Debt Simplifier/
├── app.py                    # Main Streamlit app
├── requirements.txt          # Dependencies
├── utils/
│   ├── binary_heap.py             
│   └── visualizer.py
    └── solver.py       
└── README.md                 
```

---

## 🧠 How It Works

1. You input transactions like "Person 1 owes Person 2 $30"
2. The app keeps a running list of all transactions
3. It calculates each person's net balance (how much they owe or are owed)
4. It minimizes the number of transactions required to settle all debts
5. The result is shown in a simplified graph

---

## ✨ Future Improvements

- Export transactions to CSV
- Edit/delete specific transactions
- Group-based transaction summaries

