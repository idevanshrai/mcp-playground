# 🗓️ LeaveManager (MCP Server)

LeaveManager is a lightweight **Leave Management MCP Server** built in **Python** using the **Model Context Protocol (MCP)**.
It exposes structured tools for checking leave balance, applying leave for specific dates, and viewing leave history — designed to work seamlessly with **Claude Desktop** via MCP.

The project focuses on **clean API design**, **stateful behavior**, and **clarity over complexity**, making it ideal as a learning project and a strong portfolio piece.

---

## ✨ Features

* 🧠 **MCP-Native Design** — built using `FastMCP` for clean tool and resource definitions.
* 🗂️ **In-Memory State Management** — simulates a real backend without database overhead.
* 📅 **Date-Based Leave Application** — apply leave for specific days instead of vague ranges.
* 📊 **Leave Balance Tracking** — fetch remaining leave balance instantly.
* 🕒 **Timestamped Responses** — subtle observability for better system insight.
* 🤝 **Claude-Ready** — installable directly into Claude Desktop via MCP CLI.

---

## 🧩 MCP Tools Overview

### 🔧 `get_leave_balance`

Returns the remaining leave balance for an employee.

**Input**

* `employee_id` (e.g. `E001`)

---

### 🔧 `apply_leave`

Applies leave for a list of specific dates.

**Input**

* `employee_id`
* `leave_dates` (e.g. `["2025-01-15", "2025-01-16"]`)

---

### 🔧 `get_leave_history`

Fetches the complete leave history for an employee.

**Input**

* `employee_id`

---

### 📎 Resource: Greeting

A simple greeting resource available at:

```
greeting://{name}
```

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **Model Context Protocol (MCP)**
* **FastMCP**
* Claude Desktop (for tool execution)

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11+
* `uv` installed
* Claude Desktop (macOS)

---

### Setup & Run

1. Clone the repository:

```bash
git clone https://github.com/idevanshrai/mcp-playground.git
cd mcp-playground
```

2. Initialize and pin Python:

```bash
uv init
uv python pin 3.11
uv venv
```

3. Install dependencies:

```bash
uv pip install "mcp[cli]"
```

4. Run the server:

```bash
uv run python main.py
```

---

### Install into Claude Desktop

```bash
uv run mcp install main.py
```

Restart Claude Desktop after installation.

---

## 🧪 Example Usage in Claude

```
Use the LeaveManager tool to apply leave
employee_id: E001
leave_dates: 2025-01-15, 2025-01-16, 2025-01-17
```

Claude will automatically invoke the MCP tool and return structured output.

---

## 📂 Project Structure

```
LeaveManager-MCP/
├─ main.py              # MCP server definition
├─ README.md            # Project documentation
└─ .venv/               # Virtual environment (local)
```

---

## 🚧 Roadmap / Future Enhancements

* [ ] Employee registry as a separate resource
* [ ] Date-range support (auto-expand to dates)
* [ ] Leave approval / rejection flow
* [ ] Persistent storage (SQLite / Supabase)
* [ ] Role-based tools (employee vs manager)
* [ ] Audit logging for leave actions

---

## 🤝 Contributing

Contributions are welcome.
Feel free to fork the repo, open issues, or submit pull requests.

---

## 👤 Author

**Devansh Rai**
