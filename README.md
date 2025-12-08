

---

# 🌙 **Jalali DimDate Generator**

A clean and fully automated Python script for generating a complete **Date Dimension (DimDate)** table using the **Jalali (Persian) calendar**, while preserving the original Gregorian date range.

This tool converts every Gregorian date into a rich set of Jalali-based attributes commonly used in:

* Data Warehousing
* Power BI Models
* ETL Pipelines
* Business Intelligence Systems
* Time-series Analytics

The final output is saved as an Excel file and includes all standard DimDate fields such as **DateKey**, **Year**, **Quarter**, **Semester**, **WeekOfYear**, **DayName**, **MonthName**, and more.

---

## 📌 **Features**

### ✅ Converts Gregorian → Jalali (Persian) date

### ✅ Generates a full DimDate table for a complete date range

### ✅ Produces industry-standard DimDate fields

### ✅ Stores output as an Excel file

### ✅ No external dependencies except `pandas` and `jdatetime`

### ✅ Easy to integrate into BI and SQL Server models

---

## 📅 **Generated Fields (Jalali-based)**

The script includes all the fields commonly used in enterprise date dimensions:

* **DateKey** (YYYYMMDD)
* **MiladiDate** (Gregorian)
* **JalaliDate**
* **CalendarYear**
* **Semester**, **SemesterName**
* **Quarter**, **QuarterName**
* **MonthNo**, **MonthName**
* **WeekOfMonth**, **WeekOfQuarter**, **WeekOfSemester**, **WeekOfYear**
* **DayOfWeek**, **DayName**
* **DayOfMonth**, **DayOfQuarter**, **DayOfSemester**, **DayOfYear**
* **YearMonth**, **YearMonthName**
* Placeholder fields: `SaleInvoice`, `SaleTarget`, `Treasury`

---

## 🚀 **How It Works**

1. Define a Gregorian start and end date
2. Loop through all dates in the range
3. Convert each day to Jalali
4. Calculate calendar attributes (semester, quarter, week, day, etc.)
5. Store results into a pandas DataFrame
6. Export final table as an Excel file

---

## 🛠 **Requirements**

Install required libraries:

```bash
pip install pandas jdatetime
```

---

## 📦 **Output**

The script automatically generates:

```
DimDate_2012_2030.xlsx
```

containing one row per calendar day between 2012-03-20 and 2030-12-29.

---

## 🧩 **File Structure Example**

```
├── jalali_dimdate_generator.py
├── DimDate_2012_2030.xlsx
└── README.md
```

---

## ▶️ **Running the Script**

```bash
python jalali_dimdate_generator.py
```

After running, you will see:

```
📁 File generated → DimDate_2012_2030.xlsx
Total rows: XXXX
```

---

## 📘 **Why Jalali DimDate Matters?**

Most BI, reporting, and forecasting systems in Iran require:

* Iranian fiscal year
* Jalali quarter/semester definitions
* Persian day names
* Jalali month names
* Week/season alignment based on the local calendar

This script solves that need by providing a **ready-to-use DimDate table** aligned with Iran’s calendar conventions.

---

## 🤝 **Contributing**

Pull requests, improvements, and extensions (such as adding holiday flags or fiscal calendars) are welcome.

---

## 📄 License

This project is released under the **MIT License**.

---

## ✍️ Author

**Mona Faghfouri Azar**
Data Analyst | NLP Researcher
Creator of the Jalali DimDate Generator

---

