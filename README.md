# 📅 Weekly Goals Tracker

A lightweight Python CLI tool to **log, track, and review your weekly goals** inside a beautifully formatted Excel spreadsheet — built with `openpyxl`.

No dashboards. No apps. Just a clean `.xlsx` file you own.

---

## ✨ Features

- ✅ Add weekly goals with a **Done / Not Done** status
- 📊 Auto-generates a styled `.xlsx` file (`weekly_goals.xlsx`)
- 🔵 **Bold headers** with blue background and white text
- 🔀 **Merged week cells** — vertically centered for clean readability
- 📁 Persists across runs — appends new weeks without overwriting existing data

---

## 📸 Preview

| Week   | Goal                     | Status      |
|--------|--------------------------|-------------|
| Week 1 | Learn Docker basics      | ✅ Done      |
| Week 1 | Complete internship task | ❌ Not Done  |
| Week 2 | Read 15 pages            | ✅ Done      |

*(The actual `.xlsx` file includes styled headers and merged week cells)*

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weekly-goals-tracker.git
cd weekly-goals-tracker
```

### 2. Install dependencies

```bash
pip install openpyxl
```

### 3. Add your goals

Open `goals.py` and edit the bottom section:

```python
week = "Week 1"
goals = [
    ("Learn Docker basics", True),       # True = Done
    ("Complete internship task", False),  # False = Not Done
    ("Read 15 pages", True),
]

add_week(week, goals)
```

### 4. Run the script

```bash
python goals.py
```

Your goals are saved to `weekly_goals.xlsx` in the same directory. ✅

---

## 📁 Project Structure

```
weekly-goals-tracker/
│
├── goals.py             # Main script — add your weekly goals here
├── weekly_goals.xlsx    # Auto-generated output file (created on first run)
└── README.md
```

---

## 🛠️ How It Works

1. On first run, a new `weekly_goals.xlsx` is created with styled headers.
2. Each call to `add_week()` appends goals to the next available row.
3. The **Week** column is automatically merged across all goal rows for that week.
4. Status is displayed as `✅ Done` or `❌ Not Done` based on the boolean you pass.

---

## 📦 Dependencies

| Package    | Purpose                        |
|------------|--------------------------------|
| `openpyxl` | Read/write and style Excel files |

Install via:

```bash
pip install openpyxl
```

---

## 🔮 Planned Improvements

- [ ] CLI interface — add goals directly from the terminal (`python goals.py add "Read a book" --done`)
- [ ] Conditional formatting — highlight incomplete goals in red
- [ ] Weekly summary stats — % goals completed per week
- [ ] Export to Google Sheets via API

---

## 🤝 Contributing

Pull requests are welcome! If you have a feature idea or find a bug:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Built for makers, learners, and builders who want a simple system to stay accountable — week by week.**