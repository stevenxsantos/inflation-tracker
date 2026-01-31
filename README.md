## Setup & Installation (All-in-One)

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/stevenxsantos/inflation-tracker.git
cd inflation-tracker
```

### 2. Install Python Packages
```bash
pip install pandas matplotlib fredapi
```

### 3. Create a FRED API Key
1. Visit https://fred.stlouisfed.org  
2. Create a free account  
3. Generate an API key  

### 4. Set API Key in Terminal

Mac/Linux:
```bash
export FRED_API_KEY="your_api_key_here"
```

Windows (PowerShell):
```powershell
setx FRED_API_KEY "your_api_key_here"
```

### 5. Run the Program
```bash
python3 inflation_tracker.py
```
