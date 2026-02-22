<h1><b>SQLite3 with Python 🛢️🐍</b></h1>

<a href="https://www.python.org" target="_blank">
  <img src="https://img.shields.io/badge/Python-3.x-52BE80?logo=python&logoColor=white">
</a>
<a href="https://docs.python.org/3/library/sqlite3.html" target="_blank">
  <img src="https://img.shields.io/badge/SQLite3-Built--in-5DADE2">
</a>
<a href="https://sqlitebrowser.org/" target="_blank">
  <img src="https://img.shields.io/badge/DB%20Browser-Optional-E5E7E9">
</a>

<br><br>

<img src="https://i.pinimg.com/236x/ad/a4/5d/ada45de2675b6b4425137f160db5e9c2.jpg">

<p>
This repository contains practical examples developed in <b>Python</b> using the built-in 
<b>SQLite3</b> library. The goal is to teach how to connect, create, query, and manipulate 
databases in a simple and clear way. 💻🛢️
<br><br>
The examples are especially designed for beginners who want to understand how to work with 
local databases without the need to install complex systems.
</p>

---

## ✨ Features

✅ SQLite database connection  
✅ Table creation  
✅ Data insertion (CRUD)  
✅ Queries and filters  
✅ Safe connection closing  
✅ Simple and easy-to-understand examples  

---

## 📂 Project Structure

```

SQLite3Python/
│
├── data/
│   └── database.db
│
├── src/                   # main code
│   ├── crud.py
│   ├── delete.py
│   ├── insert.py
│   └── ...
│
├── README.md        # Documentation
├── LICENSE
└── .gitignore

````

---

## 🖥️ Requirements

- Python 3.x
- SQLite3 (included by default in Python)
- DB Browser for SQLite (optional, to visualize the database)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Bredalis/SQLite3Python.git
````

Enter the directory:

```bash
cd SQLite3Python
```

---

## 🚀 Usage

Run any Python file from the project:

```bash
python main.py
```

To visualize the database:

1. Open **DB Browser for SQLite**
2. Load the `.db` file from the repository

---

## 🧠 Code Example

```python
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.insert_data(1, "Perla", "Mendoza", "15-9-1998")
crud.close_database()

```

---

## 📜 License

This project is licensed under <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">
GPLv3 (GNU General Public License v3.0) </a>

---

## 👩‍💻 Author

<img src="https://avatars.githubusercontent.com/u/111624948?s=400" width="80" style="border-radius:50%">

**Bredalis Gautreaux**

[![Github](https://img.shields.io/github/followers/Bredalis?label=Follow\&style=social)](https://github.com/Bredalis)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square\&logo=Linkedin\&logoColor=white)](https://www.linkedin.com/in/bredalis-gautreaux/)

😊 Programmer passionate about technology, artificial intelligence, and continuous learning.
#python #sqlite #ai #nlp

---

## ⭐ Support the Project

If this repository helped you, consider giving it a ⭐ on GitHub.
