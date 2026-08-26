# 📅 Persian (Jalali) Date Dimension Generator

A Python-based **Date Dimension Generator** designed for **Power BI, Business Intelligence, Data Warehousing, reporting systems, and time-series analytics** that require support for the **Persian (Jalali/Shamsi) calendar**.

The project automatically generates a complete date dimension covering a predefined Gregorian date range, converts every date to the corresponding Persian calendar date, calculates multiple time intelligence attributes, identifies holidays, and exports the final dataset to an Excel file.

It is particularly useful for Iranian BI environments where standard Gregorian date tables are not sufficient for reporting, filtering, aggregation, and time-based analysis.

---

## 🚀 Project Overview

Date dimensions are one of the fundamental components of analytical data models.

In many BI systems, however, built-in date functions are primarily designed around the Gregorian calendar. This creates challenges when reports need to operate using the Persian calendar.

This project solves that problem by generating a reusable **Jalali Date Dimension** with attributes required for:

* Power BI dashboards
* Data warehouses
* Sales analytics
* Financial reporting
* KPI monitoring
* Time-series analysis
* Monthly and quarterly reporting
* Iranian business calendars
* Holiday-aware analysis
* ETL and data preparation pipelines

The generated table can be imported directly into analytical systems and used as a central date dimension.

---

# ✨ Key Features

## 📆 Gregorian → Jalali Conversion

Every Gregorian date in the configured date range is automatically converted to its equivalent Persian/Jalali date.

Example:

```text
Gregorian Date  →  Jalali Date
2026-03-21      →  1405/01/01
```

The conversion is performed using the `jdatetime` Python library.

---

## 🔑 Numeric DateKey

A numeric date key is generated for every record using the following structure:

```text
YYYYMMDD
```

For example:

```text
1405/01/01
```

becomes:

```text
14050101
```

This field is particularly useful as a surrogate/business key in:

* Star schemas
* Data warehouses
* Power BI relationships
* Fact-to-dimension joins

---

## 📊 BI-Ready Time Hierarchies

The generated dataset contains several calendar hierarchy levels that make it suitable for analytical models.

The hierarchy includes:

```text
Year
 ├── Semester
 │    ├── Quarter
 │    │    ├── Month
 │    │    │    ├── Week
 │    │    │    │    └── Day
```

This makes it possible to create drill-down structures such as:

```text
Year → Quarter → Month → Day
```

inside Power BI or other BI platforms.

---

# 🌓 Semester Classification

Each Persian year is divided into two semesters.

```text
Months 1–6  → Semester 1
Months 7–12 → Semester 2
```

The generated fields include:

```text
Semester
SemesterName
```

This makes six-month performance comparisons easy to implement.

---

# 🌱 Persian Quarter Classification

Each Persian year is divided into four quarters.

| Quarter | Persian Months      | Season |
| ------- | ------------------- | ------ |
| Q1      | Farvardin – Khordad | Spring |
| Q2      | Tir – Shahrivar     | Summer |
| Q3      | Mehr – Azar         | Autumn |
| Q4      | Dey – Esfand        | Winter |

Both numeric and descriptive quarter information are generated.

Example:

```text
Quarter = 1
QuarterName = بهار
```

This allows quarterly sales, revenue, target, and operational analyses based on the Iranian calendar rather than Gregorian quarters.

---

# 🗓️ Persian Month Support

The script assigns the corresponding Persian month to each date.

The Persian calendar contains the following months:

```text
Farvardin
Ordibehesht
Khordad
Tir
Mordad
Shahrivar
Mehr
Aban
Azar
Dey
Bahman
Esfand
```

The generated dataset contains both:

```text
MonthNo
MonthName
```

This is useful for correctly sorting Persian month names in BI reports.

---

# 📅 Persian Weekday Names

The script maps Python's weekday values to Persian weekday names.

The supported values include:

```text
دوشنبه
سه‌شنبه
چهارشنبه
پنجشنبه
جمعه
شنبه
يكشنبه
```

The generated columns include:

```text
DayOfWeek
DayName
```

These fields can be used to analyze patterns such as:

* Sales by weekday
* Weekend performance
* Daily customer activity
* Operational workload by day
* Working-day behavior

---

# 🔥 Holiday Detection

One of the most useful features of the project is the built-in **holiday indicator**.

The script determines whether a date should be treated as a holiday.

A date receives:

```text
is holiday = 1
```

when:

1. The day is Friday, or
2. The Jalali date exists in the predefined holiday list.

Otherwise:

```text
is holiday = 0
```

This makes the date dimension suitable for business analyses where holidays can significantly influence sales, traffic, demand, productivity, or customer behavior.

---

# 🇮🇷 Iranian Holiday Calendar

The project contains manually defined holiday dates for selected Persian years.

The current implementation includes holiday definitions for:

```text
1399
1400
1401
1402
1403
1404
1405
```

Each holiday is stored using:

```python
(month, day)
```

For example:

```python
(1, 1)
```

represents the first day of Farvardin.

> **Important:** Holiday definitions should be reviewed and updated when extending the project to future years or when organizational/business-specific holidays need to be included.

---

# 📈 Advanced Time Intelligence Fields

The generated date dimension goes beyond basic year/month/day information.

It calculates multiple attributes that can simplify analytical calculations.

### Day-level attributes

```text
DayOfWeek
DayOfMonth
DayOfQuarter
DayOfSemester
DayOfYear
```

### Week-level attributes

```text
WeekOfMonth
WeekOfQuarter
WeekOfSemester
WeekOfYear
```

These fields are useful for creating analyses such as:

```text
Week-over-Week Sales
Quarter-to-Date Performance
Semester Progress
Day-of-Year Comparisons
Week-of-Month Performance
```

without repeatedly rebuilding the underlying calendar logic.

---

# 🔢 Year-Month Keys

The script also generates a numeric `YearMonth` value.

For example:

```text
1405/01
```

becomes:

```text
140501
```

This is especially useful for:

* Sorting monthly data
* Joining monthly aggregate tables
* Creating time-series charts
* Monthly forecasting
* Period-based filtering

---

# 🏷️ Human-Readable Year-Month Labels

In addition to numeric keys, the script generates readable Persian period labels.

For example:

```text
ماه فروردين سال 1405
```

This makes report slicers and chart labels easier for Persian-speaking users to understand.

---

# 📦 Generated Columns

The final Date Dimension contains fields such as:

| Column           | Description                       |
| ---------------- | --------------------------------- |
| `DateKey`        | Numeric Jalali date identifier    |
| `MiladiDate`     | Gregorian date                    |
| `Date`           | Persian/Jalali date               |
| `CalendarYear`   | Persian calendar year             |
| `Semester`       | Semester number                   |
| `Quarter`        | Quarter number                    |
| `MonthNo`        | Persian month number              |
| `WeekOfMonth`    | Week number within the month      |
| `WeekOfQuarter`  | Week number within the quarter    |
| `WeekOfSemester` | Week number within the semester   |
| `WeekOfYear`     | ISO week number                   |
| `DayOfWeek`      | Numeric weekday                   |
| `DayOfMonth`     | Day within the Persian month      |
| `DayOfQuarter`   | Day within the Persian quarter    |
| `DayOfSemester`  | Day within the Persian semester   |
| `DayOfYear`      | Day-of-year indicator             |
| `DayName`        | Persian weekday name              |
| `MonthName`      | Persian month name                |
| `QuarterName`    | Persian season/quarter name       |
| `SemesterName`   | Persian semester label            |
| `YearMonth`      | Numeric year-month key            |
| `YearMonthName`  | Human-readable Persian year-month |
| `is holiday`     | Holiday indicator                 |
| `SaleInvoice`    | Placeholder analytical column     |
| `SaleTarget`     | Placeholder analytical column     |
| `Treasury`       | Placeholder analytical column     |

---

# 🏗️ How It Works

The processing pipeline is straightforward:

```text
Gregorian Date Range
        ↓
Iterate Through Each Date
        ↓
Convert Gregorian → Jalali
        ↓
Extract Year / Month / Day
        ↓
Calculate Semester
        ↓
Calculate Quarter
        ↓
Calculate Week Attributes
        ↓
Calculate Day Attributes
        ↓
Assign Persian Names
        ↓
Check Holiday Status
        ↓
Create Date Dimension Record
        ↓
Build Pandas DataFrame
        ↓
Export to Excel
```

This approach creates one complete analytical record for every calendar date in the configured period.

---

# 📆 Default Date Range

The current configuration generates dates from:

```python
start_date = datetime.date(2012, 3, 20)
end_date   = datetime.date(2030, 12, 29)
```

You can easily customize this range.

For example:

```python
start_date = datetime.date(2020, 1, 1)
end_date   = datetime.date(2035, 12, 31)
```

---

# 🛠️ Technologies Used

The project is built with:

* **Python**
* **Pandas**
* **jdatetime**
* **datetime**
* **Excel**

It can easily be integrated into larger ETL, analytics, or BI workflows.

---

# 📦 Requirements

Install the required Python packages before running the script:

```bash
pip install pandas jdatetime openpyxl
```

Main dependencies:

```text
pandas
jdatetime
openpyxl
```

`datetime` is included in the Python standard library and does not require separate installation.

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR_REPOSITORY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the generator:

```bash
python Ana_Date.py
```

After execution, the script generates:

```text
DimDate_2012_2030.xlsx
```

The console also displays the generated filename and total number of date records.

---

# 📂 Recommended Repository Structure

A clean GitHub repository could use the following structure:

```text
persian-date-dimension/
│
├── Ana_Date.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── output/
│   └── DimDate_2012_2030.xlsx
│
└── screenshots/
    ├── excel_preview.png
    └── powerbi_preview.png
```

For larger projects, the generated Excel file can also be excluded from Git and generated locally by users.

---

# 📄 requirements.txt

A minimal `requirements.txt` file can contain:

```text
pandas
jdatetime
openpyxl
```

---

# 📊 Power BI Integration

The generated Excel file can be imported directly into Power BI.

A typical workflow is:

```text
Python Generator
       ↓
DimDate Excel File
       ↓
Power BI
       ↓
Date Dimension
       ↓
Relationships with Fact Tables
       ↓
Time Intelligence & Reporting
```

For example, `DateKey` or the appropriate date field can be connected to fact tables containing:

```text
Sales
Targets
Financial Transactions
Inventory
Customer Activity
```

The date dimension can then be used for slicers, filters, drill-down hierarchies, and time-based calculations.

---

# 💼 Example Business Use Cases

### Sales Analysis

Analyze:

```text
Daily Sales
Monthly Sales
Quarterly Sales
Holiday vs. Non-Holiday Sales
Weekday Sales Patterns
Year-over-Year Performance
```

### Demand Forecasting

The calendar attributes can be combined with historical demand data to create features such as:

```text
Month
Quarter
Week
Day of Week
Holiday Indicator
Season
```

These features can then be used in forecasting and machine-learning pipelines.

### Financial Reporting

Organizations operating on the Persian calendar can use the generated table for:

```text
Monthly Financial Reports
Quarterly Performance
Semester Analysis
Fiscal Reporting
Treasury Analysis
```

### KPI Dashboards

The date dimension can provide consistent filtering across multiple KPI tables and dashboards.

---

# 🧠 Why Use a Dedicated Date Dimension?

A dedicated date dimension centralizes calendar logic.

Instead of calculating Persian dates independently in every dashboard, query, or analytical model, the logic is generated once and reused throughout the system.

This provides:

* Consistent calendar definitions
* Cleaner BI models
* Easier filtering
* Better reporting hierarchies
* Reusable holiday logic
* Simpler time-based calculations
* Easier integration across multiple fact tables

---

# 🔧 Customization

The project is intentionally easy to customize.

You can modify:

### Date Range

```python
start_date = ...
end_date = ...
```

### Holiday Calendar

Add or modify holiday dates inside the `holidays` dictionary.

### Business Holidays

Company-specific shutdowns or operational holidays can also be added.

### Output Columns

Additional attributes can be included inside:

```python
build_dimdate_record()
```

For example:

```text
FiscalYear
FiscalQuarter
WorkingDay
WeekendFlag
SeasonCode
CampaignPeriod
PayrollPeriod
```

---

# ⚠️ Important Notes

The holiday calendar is explicitly defined in the source code for selected Jalali years.

Therefore, before using the project in a production environment:

* Validate holiday dates against your authoritative calendar source.
* Add holiday definitions for additional years when necessary.
* Review company-specific working-day rules.
* Confirm whether Friday alone or additional weekdays should be considered non-working days.
* Validate week-number definitions against your organization's reporting requirements.

---

# 🔮 Future Improvements

Potential future versions could include:

* Automatic Iranian holiday retrieval
* Dynamic holiday calculation
* Configurable weekend rules
* Fiscal calendar support
* CSV export
* SQL export
* Direct database insertion
* Power BI-ready output mode
* Working-day calculations
* Previous/next working-day fields
* Holiday names
* Configurable date ranges through CLI arguments
* Automated tests
* Python package distribution

---

# 🎯 Who Is This Project For?

This project can be useful for:

* Data Analysts
* BI Developers
* Power BI Developers
* Data Engineers
* Data Scientists
* Financial Analysts
* Sales Analysts
* Iranian organizations using the Jalali calendar
* Developers building Persian-language analytical systems

---

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

If you find an issue or would like to add new functionality, feel free to:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request

---

# ⭐ Support

If you find this project useful, consider giving the repository a **star ⭐**.

It helps make the project easier for other developers, analysts, and Power BI users working with the Persian calendar to discover.

---

## 👩‍💻 Author

**Mona Faghfouri Azar**

Data Analyst | Python Developer | Business Intelligence | Data Analytics

GitHub: `MonaFaghfouri`

---

## 📌 Project Summary

> A Python-based Persian/Jalali Date Dimension Generator for Power BI, data warehouses, business intelligence, and time-series analytics, featuring Gregorian-to-Jalali conversion, Persian calendar hierarchies, advanced time attributes, and holiday detection.
