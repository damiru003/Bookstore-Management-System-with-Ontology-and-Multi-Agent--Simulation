# 🚀 QUICK START GUIDE

## Complete Bookstore Management System - Get Started in 2 Minutes!

---

## ✅ You Have Successfully Created a 2-File System!

### 📁 Your Files

```
✅ bookstore_system.py    (43 KB) - Complete integrated system
✅ bookstore_gui.py        (53 KB) - Interactive interface
```

**That's it! Just 2 main files with everything integrated:**
- Mesa Framework ✅
- Owlready2 Ontology ✅
- SWRL Business Rules (9 rules) ✅
- Message Bus Communication ✅

---

## 🎯 Run It Now!

### Method 1: GUI (Beautiful Interface) 🎨

```powershell
# Step 1: Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Step 2: Run GUI
python bookstore_gui.py
```

**What you'll see:**
- Configuration panel (adjust customers, employees, books, steps)
- Live metrics (revenue, satisfaction, transactions)
- 3 real-time charts
- Activity log with color-coded events
- Export buttons

**What to do:**
1. Click **"Start Simulation"** (uses default parameters)
2. Watch real-time updates
3. View charts updating live
4. Click **"Export All Data"** when done

---

### Method 2: Command Line (Quick Demo) 💻

```powershell
# Step 1: Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Step 2: Run system
python bookstore_system.py

# Step 3: Select option
# Press 1 for Quick Demo (30 steps, 5 customers)
# Press 2 for Standard (75 steps, 8 customers)
# Press 3 for Full (150 steps, 12 customers)
```

**What you'll see:**
```
🏪==================================================================🏪
    COMPLETE BOOKSTORE MANAGEMENT SYSTEM
    Mesa + Owlready2 + SWRL + Message Bus Integration
🏪==================================================================🏪

✅ System initialized successfully:
   🤖 Mesa Framework: Professional ABM structure
   🧠 Ontology (Owlready2): 25 entities
   📋 SWRL Rules: 9 business rules
   📬 Message Bus: 26 registered agents

🚀 Starting simulation for 30 steps...

📅 Step 1/30:
  👀 Alice Johnson is browsing 'The Great Adventure'
  ✅ Bob Wilson purchased 'Mystery of the Lost City' for $19.99
  📦 Sarah Manager restocked 'Science and Wonder': 4 → 24 (+20)
  🧠 SWRL inference: 2 premium, 3 active customers

...

✅ Simulation completed!

📊 COMPLETE SYSTEM RESULTS
💰 Total Revenue: $567.89
👥 Customer Satisfaction: 78.5%
🧠 SWRL Classifications: 15 total
📬 Messages Processed: 89
```

---

## 📊 What Happens During Simulation

### Every Step:
1. **Agents Execute** (in random order)
   - Customers browse and purchase books
   - Employees check and restock inventory
   - Books adjust prices dynamically

2. **Communication** (via Message Bus)
   - Purchase notifications sent
   - Restock alerts broadcast
   - Price changes announced

3. **Ontology Updates**
   - Transactions recorded
   - Inventory updated
   - Budgets adjusted

4. **SWRL Rules Applied** (every 10 steps)
   - Premium customers identified
   - Low stock detected
   - Discount eligibility calculated

5. **Data Collected**
   - Revenue tracked
   - Satisfaction measured
   - All metrics recorded

---

## 🎮 GUI Controls

### Configuration Section (Top)
- **Customers**: 3-25 (default: 8)
- **Employees**: 1-8 (default: 3)
- **Books**: 5-30 (default: 15)
- **Steps**: 20-300 (default: 100)
- **Delay**: 0.1-2.0 sec (default: 0.5)

### Control Buttons
- **🟢 Start Simulation** - Begin new simulation
- **⏸️ Pause** - Pause execution (can resume)
- **⏹️ Stop** - End simulation immediately
- **🔄 Reset** - Clear all data and reset

### Live Metrics Panel
- Current Step
- Total Revenue ($)
- Books Sold
- Customer Satisfaction (%)
- Restocks Completed
- SWRL Classifications

### Charts (Auto-updating) - ALL 4 WORKING! ✅
- **Revenue Over Time** - Blue line chart showing cumulative revenue ($)
- **Books Sold** - Green line chart showing transaction count
- **Customer Satisfaction** - Red line chart showing happiness (0-100%)
- **Message Bus Activity** - Orange line chart showing inter-agent communications

### Activity Log
Color-coded events:
- 🟢 Green: Purchases
- 🔵 Blue: Customer browsing
- 🟠 Orange: Employee restocks
- 🟣 Purple: System events

### Export Options
- **Export Charts** - Save all 4 charts as PNG
- **Export Results** - Save complete text report
- **Export All Data** - Save everything (charts + results + JSON data)

---

## 📈 Example Simulation Results

### Quick Demo (30 steps)
```
Revenue: $200-400
Transactions: 15-25
Restocks: 5-10
Satisfaction: 60-75%
Messages: 40-60
Duration: ~15 seconds
```

### Standard (75 steps)
```
Revenue: $800-1,500
Transactions: 40-70
Restocks: 15-25
Satisfaction: 65-80%
Messages: 100-150
Duration: ~45 seconds
```

### Full (150 steps)
```
Revenue: $2,000-3,500
Transactions: 90-150
Restocks: 30-50
Satisfaction: 70-85%
Messages: 200-300
Duration: ~90 seconds
```

---

## 🧠 SWRL Intelligence Examples

The system automatically classifies entities using 9 rules:

```
After 50 steps, you might see:

Premium Customers: 3        (Budget > $250)
Low Budget Customers: 2     (Budget < $100)
High Value Books: 4         (Price > $30)
Low Stock Books: 2          (Quantity < 5)
Overstocked Books: 1        (Quantity > 30)
Active Customers: 7         (Have purchases)
Discount Eligible: 2        (Premium + Active)
Restock Required: 3         (Below threshold)
High Performers: 2          (Efficient employees)
```

---

## 🛠️ Troubleshooting

### Problem: Import Error

```powershell
# Solution: Ensure packages are installed
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Problem: GUI Window Too Large

The window is 1200x750 pixels (optimized for 1366x768 screens).
If your screen is smaller, the window will still be usable.

### Problem: Simulation Runs Too Fast/Slow

In GUI:
- Adjust "Step Delay" slider (0.1-2.0 seconds)

In Console:
- Not applicable (runs at maximum speed)

### Problem: "bookstore_system.py not found"

```powershell
# Make sure you're in the correct directory
cd "d:\KDU\CSAT\MAS"
python bookstore_gui.py
```

---

## 📚 Learn More

### Documentation Files
- **FINAL_README.md** - Complete feature guide
- **SYSTEM_CONSOLIDATION_SUMMARY.md** - System overview
- **ARCHITECTURE_DIAGRAM.md** - Visual system architecture
- **BOOKSTORE_SYSTEM_REPORT.md** - 20-page technical docs

### In-Code Documentation
Both files have extensive comments and docstrings explaining:
- Class purposes
- Method behaviors
- Parameter meanings
- Return values

---

## 🎯 What to Try

### Experiment 1: Different Configurations
```
GUI: Try 20 customers, 5 employees, 25 books, 200 steps
See how the system scales!
```

### Experiment 2: Watch SWRL Classifications
```
GUI: Monitor the "SWRL Classifications" metric
See it grow as rules identify premium customers and low stock
```

### Experiment 3: Message Flow
```
Console: Run with verbose mode
Watch messages being sent between agents
```

### Experiment 4: Export and Analyze
```
GUI: Run full simulation, export all data
Open the JSON file to see complete statistics
```

---

## 🎓 Educational Value

### You Can Learn:
- ✅ How Mesa framework structures ABM
- ✅ How ontologies represent knowledge
- ✅ How SWRL rules enable reasoning
- ✅ How message buses coordinate agents
- ✅ How to build real-time GUIs
- ✅ How to integrate multiple frameworks

### Perfect For:
- MAS course projects
- Research prototypes
- Learning agent-based modeling
- Understanding semantic web
- Practicing software architecture

---

## 🚀 Ready to Go!

You have everything you need:

### ✅ System Files
- bookstore_system.py (complete backend)
- bookstore_gui.py (beautiful interface)

### ✅ Documentation
- FINAL_README.md (features & usage)
- ARCHITECTURE_DIAGRAM.md (system design)
- SYSTEM_CONSOLIDATION_SUMMARY.md (overview)

### ✅ All Features Integrated
- Mesa Framework
- Owlready2 Ontology
- SWRL Business Rules
- Message Bus Communication

---

## 🎉 Start Now!

### For GUI Experience:
```powershell
.\.venv\Scripts\Activate.ps1
python bookstore_gui.py
```

### For Quick Test:
```powershell
.\.venv\Scripts\Activate.ps1
python bookstore_system.py
# Press 1 for Quick Demo
```

---

## 💡 Pro Tips

1. **Start Small**: Use Quick Demo first to understand the system
2. **Watch Metrics**: Live metrics tell the business story
3. **Read Logs**: Activity log shows what's happening in real-time
4. **Export Data**: Save results for analysis and presentations
5. **Experiment**: Try different configurations to see system behavior

---

## 🎊 Enjoy Your Complete Bookstore System!

**You now have a professional, fully-integrated multi-agent system with:**
- Mesa framework for ABM ✅
- Ontology for knowledge ✅
- SWRL for business logic ✅
- Message bus for communication ✅
- Beautiful GUI for interaction ✅

**All in just 2 files! 🚀**

---

## 📞 Quick Reference

| Need | Command |
|------|---------|
| Run GUI | `python bookstore_gui.py` |
| Run Console | `python bookstore_system.py` |
| Check Install | `pip list \| Select-String "mesa\|owlready2"` |
| Activate Env | `.\.venv\Scripts\Activate.ps1` |
| View Docs | Open FINAL_README.md |

---

**System Status: 🟢 READY TO USE**

**Have fun exploring your complete multi-agent bookstore! 🏪✨**
