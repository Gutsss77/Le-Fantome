# Le-Fantome
Program that controls my machine ^_^
# 👻 Le-Fantome

> A local AI agent that understands natural-language commands and controls your machine.

Le-Fantome is an experimental **local PC agent** powered by **Qwen3 4B** running through **Ollama**.

The goal is simple:

```text
You → Le-Fantome → Local LLM → Tools → Your Machine
```

Instead of manually performing every step, you give Le-Fantome a command in your terminal and it determines the actions required to complete it.

---

## 🧠 Architecture

```text
                    ┌──────────────┐
                    │    User      │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Le-Fantome   │
                    │    Agent     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Qwen3 4B   │
                    │   + Ollama   │
                    └──────┬───────┘
                           │
                       Tools
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Terminal          Browser         File System
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                         macOS
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Le-Fantome
```

---

## 2. Install Python

Le-Fantome is built with Python.

Check whether Python is already installed:

```bash
python3 --version
```

Python **3.11+** is recommended.

If Python is not installed, install it using Homebrew:

```bash
brew install python
```

Then verify:

```bash
python3 --version
```

---

## 3. Install Ollama

Le-Fantome uses Ollama to run the LLM locally.

Install Ollama from:

https://ollama.com

After installation, verify:

```bash
ollama --version
```

---

## 4. Download Qwen3 4B

Pull the local model:

```bash
ollama pull qwen3:4b
```

Verify that it is installed:

```bash
ollama list
```

You should see:

```text
qwen3:4b
```

Test the model:

```bash
ollama run qwen3:4b
```

Try asking:

```text
Hello, what can you do?
```

Exit with:

```text
/bye
```

---

## 5. Create a Python virtual environment

It is recommended to use a virtual environment instead of installing project dependencies globally.

From the project directory:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv)
```

in your terminal prompt.

To deactivate later:

```bash
deactivate
```

---

## 6. Install Python dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

For a fresh development environment, you can also install the Ollama Python client directly:

```bash
pip install ollama
```

Then update the requirements file:

```bash
pip freeze > requirements.txt
```

---

## 7. Verify the installation

Check Python:

```bash
python --version
```

Check Ollama:

```bash
ollama --version
```

Check the model:

```bash
ollama list
```

Check the Python Ollama package:

```bash
pip show ollama
```

---

# 🧪 Test Le-Fantome

Make sure Qwen3 4B is available:

```bash
ollama list
```

Then run:

```bash
python main.py
```

The program should communicate with the locally running Qwen3 4B model.

---

# 🛠️ Development

Activate the environment whenever you start working on the project:

```bash
cd Le-Fantome
source .venv/bin/activate
```

Then run:

```bash
python main.py
```

---

# 📁 Project Structure

```text
Le-Fantome/
│
├── le_fantome/
│   ├── agent/
│   │   └── __init__.py
│   │
│   ├── tools/
│   │   └── __init__.py
│   │
│   ├── config/
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Planned Capabilities

- [x] Local LLM communication
- [ ] Natural-language command interface
- [ ] Agent reasoning loop
- [ ] Terminal control
- [ ] Application launching
- [ ] File and folder operations
- [ ] Browser automation
- [ ] Keyboard control
- [ ] Mouse control
- [ ] Screenshot / screen awareness
- [ ] Multi-step task execution
- [ ] Error detection and recovery
- [ ] Permission and confirmation system
- [ ] Voice interaction

---

# 🔐 Safety

Le-Fantome is designed to control the local machine, so security and safety are important.

The LLM should **not** receive unrestricted access to the operating system.

Actions will pass through a tool and permission layer:

```text
LLM
 │
 ▼
Requested Action
 │
 ▼
Permission / Safety Layer
 │
 ├── Allowed → Execute
 │
 └── Dangerous → Ask for Confirmation
```

Potentially destructive operations should require explicit confirmation.

---

# 🧪 Current Status

**Early development — v0.1**

The current milestone is establishing communication between:

```text
Python
   ↓
Ollama
   ↓
Qwen3 4B
```

The next milestone is the first actual agent loop:

```text
User Command
      ↓
Qwen3 4B
      ↓
Tool Selection
      ↓
Permission Check
      ↓
Tool Execution
      ↓
Result
      ↓
Qwen3 4B
      ↓
Final Response
```

---

# 🎯 Long-Term Goal

The long-term goal of Le-Fantome is to become a **fully local computer-use agent** capable of understanding high-level instructions and carrying out the required actions on the user's machine.

> **Give it a command. Let Le-Fantome handle the work.**

---

## License

See [LICENSE](LICENSE).