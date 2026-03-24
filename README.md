# 🧠 Smart Scheduler

A smart task scheduling web app built with Python and HTML that automatically organizes your week based on priorities, time constraints, and intelligent randomness.

---

## 🚀 Features

* 🔴 **Fixed Tasks (Red)**
  Tasks that cannot move (e.g., school, practice)

* 🟡 **Flexible Tasks (Yellow)**
  Tasks that must be done but can be scheduled automatically

* 🟢 **Optional Tasks (Green)**
  Tasks placed only if there is free time

* ⚫ **Permanent Tasks (Black)**
  Recurring tasks that stay every week

* 🧠 **Smart Scheduling Algorithm**

  * Avoids conflicts with fixed tasks
  * Maximizes free time
  * Uses randomness for realistic schedules
  * Adapts based on average task duration

---

## ⚙️ How It Works

1. User inputs tasks with:

   * Name
   * Priority (color)
   * Duration
   * Days
   * Time range (for flexible tasks)

2. The system:

   * Locks fixed tasks in place
   * Calculates free time
   * Schedules flexible tasks intelligently
   * Adds randomness for natural variation

3. Outputs a weekly schedule in the browser

---

## 🛠️ Installation

1. Install Python (if not installed)

2. Install Flask:

```
pip install flask
```

3. Run the app:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
smart_scheduler/
│
├─ app.py
├─ scheduler.py
├─ storage.py
├─ data/
│   └─ tasks.json
├─ templates/
│   └─ index.html
```

---

## 🧪 Example Use Case

* School (🔴) → fixed
* Homework (🟡) → scheduled automatically
* Gaming (🟢) → fills free time

Result: A balanced, optimized weekly schedule.

---

## 🔒 License

This project is protected under an **All Rights Reserved License**.
You may not copy, modify, or distribute this software without permission.

---

## 💡 Future Improvements

* Calendar UI
* Notifications system
* Mobile-friendly design
* Cloud deployment

---

## 👨‍💻 Author

Created by [Your Name]

---

## ⚠️ Disclaimer

This tool is for personal productivity use. Accuracy depends on user input.
