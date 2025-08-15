# 🔍 Username Checker OSINT Tool

A fast, asynchronous **OSINT (Open Source Intelligence)** tool to check if a given username exists across multiple platforms.  
Supports **username variations** for more thorough investigations.

---

## 🚀 Features

- **Multi-platform search**: Checks username availability on major social media platforms.
- **Username variations**: Optionally generates common variations (e.g., underscores, numbers, "official" tags).
- **Asynchronous requests** for faster scanning.
- **Color-coded output** for quick result interpretation.
- **Customizable platform list** via `PLATFORMS` dictionary.

---

## 🖥 Supported Platforms

- Facebook  
- GitHub  
- Instagram  
- Twitter (X)  
- Reddit  
- YouTube  
- TikTok  
- LinkedIn  
- Pinterest  
- Twitch  
- Snapchat  
- WhatsApp  

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/username-checker-osint.git
cd username-checker-osint
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Requirements:**
- Python **3.8+**
- `aiohttp` for async requests
- `colorama` for colored terminal output

---

## 📜 Usage

Run the script:
```bash
python main.py
```

**Example session:**
```
Enter username to check: hmida
Do you want to check variations? (y/n): y
```

**Output:**
```
=== Username Check Results ===

Facebook     hmida         FOUND      https://www.facebook.com/hmida
GitHub       hmida_123     NOT FOUND
Twitter      hmida         FOUND      https://twitter.com/hmida
LinkedIn     hmida         NOT FOUND
...
```

---

## ⚙ Configuration

You can modify `platforms.py` to add/remove platforms or update URL patterns:
```python
PLATFORMS = {
    "Facebook": "https://www.facebook.com/{}",
    "GitHub": "https://github.com/{}",
    ...
}
```


---

## ⚠️ Disclaimer
This tool is for **educational and research purposes only**.  
Do not use it for any illegal activity.  
The author is **not responsible** for any misuse.


