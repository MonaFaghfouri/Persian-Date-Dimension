"""
Persian (Jalali) Date Dimension Generator
=========================================

This script generates a complete Date Dimension table for Business Intelligence,
Data Warehousing, Power BI, reporting, and time-series analysis environments that
need support for the Persian (Jalali/Shamsi) calendar.

Main features
-------------
- Generates a continuous Gregorian date range
- Converts Gregorian dates to Jalali dates
- Creates a numeric Jalali DateKey
- Calculates Persian year, semester, quarter, month, week, and day attributes
- Adds Persian weekday and month names
- Detects Fridays and predefined holidays
- Exports the final Date Dimension to Excel

Dependencies
------------
pip install pandas jdatetime openpyxl
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import jdatetime
import pandas as pd


# =============================================================================
# CONFIGURATION
# =============================================================================

# Gregorian date range to generate.
START_DATE = dt.date(2012, 3, 20)
END_DATE = dt.date(2030, 12, 29)

# Output file.
OUTPUT_FILE = Path("DimDate_2012_2030.xlsx")


# =============================================================================
# PERSIAN CALENDAR LABELS
# =============================================================================

PERSIAN_MONTH_NAMES = [
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند",
]

# Python datetime.date.weekday():
# Monday = 0
# Tuesday = 1
# Wednesday = 2
# Thursday = 3
# Friday = 4
# Saturday = 5
# Sunday = 6
PERSIAN_WEEKDAY_NAMES = [
    "دوشنبه",
    "سه‌شنبه",
    "چهارشنبه",
    "پنجشنبه",
    "جمعه",
    "شنبه",
    "یکشنبه",
]


# =============================================================================
# HOLIDAY CALENDAR
# =============================================================================

# Holidays are stored as:
#     Jalali year -> set of (month, day)
#
# Note:
# These dates are manually defined and should be validated against an
# authoritative Iranian calendar source before production use.
HOLIDAYS: dict[int, set[tuple[int, int]]] = {
    1399: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 12), (1, 13), (1, 21),
        # Khordad
        (3, 4), (3, 5), (3, 14), (3, 15), (3, 28),
        # Mordad
        (5, 18),
        # Shahrivar
        (6, 8), (6, 9),
        # Mehr
        (7, 17), (7, 25), (7, 26),
        # Aban
        (8, 4), (8, 13),
        # Dey
        (10, 28),
        # Bahman
        (11, 22),
        # Esfand
        (12, 7), (12, 21), (12, 29),
    },
    1400: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 9), (1, 12), (1, 13),
        # Ordibehesht
        (2, 14), (2, 23), (2, 24),
        # Khordad
        (3, 14), (3, 15), (3, 16),
        # Tir
        (4, 30),
        # Mordad
        (5, 7), (5, 27), (5, 28),
        # Mehr
        (7, 5), (7, 13), (7, 15),
        # Aban
        (8, 2),
        # Dey
        (10, 16),
        # Bahman
        (11, 22), (11, 26),
        # Esfand
        (12, 10), (12, 27), (12, 29),
    },
    1401: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 12), (1, 13),
        # Ordibehesht
        (2, 3), (2, 13), (2, 14),
        # Khordad
        (3, 5), (3, 14), (3, 15),
        # Tir
        (4, 19), (4, 27),
        # Mordad
        (5, 16), (5, 17),
        # Shahrivar
        (6, 26),
        # Mehr
        (7, 3), (7, 5), (7, 13), (7, 22),
        # Dey
        (10, 6),
        # Bahman
        (11, 15), (11, 22), (11, 29),
        # Esfand
        (12, 17), (12, 29),
    },
    1402: {
        # Farvardin
        (1, 1), (1, 4), (1, 12), (1, 13), (1, 23),
        # Ordibehesht
        (2, 2), (2, 3), (2, 26),
        # Khordad
        (3, 14), (3, 15),
        # Tir
        (4, 8), (4, 16),
        # Mordad
        (5, 5),
        # Shahrivar
        (6, 15), (6, 23), (6, 25),
        # Mehr
        (7, 2), (7, 11),
        # Azar
        (9, 26),
        # Bahman
        (11, 5), (11, 19), (11, 22),
        # Esfand
        (12, 6), (12, 29),
    },
    1403: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 12), (1, 13), (1, 22), (1, 23),
        # Ordibehesht
        (2, 15),
        # Khordad
        (3, 14), (3, 15), (3, 28),
        # Tir
        (4, 5), (4, 25), (4, 26),
        # Shahrivar
        (6, 4), (6, 12), (6, 14), (6, 22), (6, 31),
        # Azar
        (9, 15),
        # Dey
        (10, 25),
        # Bahman
        (11, 9), (11, 22),
        # Esfand
        (12, 29), (12, 30),
    },
    1404: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 11), (1, 12), (1, 13),
        # Ordibehesht
        (2, 4),
        # Khordad
        (3, 14), (3, 15), (3, 16), (3, 24), (3, 25), (3, 26),
        (3, 27), (3, 28), (3, 29), (3, 30), (3, 31),
        # Tir
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
        (4, 14), (4, 15),
        # Mordad
        (5, 23), (5, 31),
        # Shahrivar
        (6, 2), (6, 10), (6, 19),
        # Azar
        (9, 3),
        # Dey
        (10, 13), (10, 27),
        # Bahman
        (11, 15), (11, 22),
        # Esfand
        (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14),
        (12, 15), (12, 16), (12, 17), (12, 18), (12, 19), (12, 20),
        (12, 21), (12, 22), (12, 23), (12, 24), (12, 25), (12, 26),
        (12, 27), (12, 28), (12, 29),
    },
    1405: {
        # Farvardin
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 12), (1, 13), (1, 25),
        # Khordad
        (3, 6), (3, 14),
        # Tir
        (4, 3), (4, 4), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18),
        # Mordad
        (5, 13), (5, 21), (5, 22),
        # Shahrivar
        (6, 8),
        # Dey
        (10, 2), (10, 16),
        # Bahman
        (11, 4), (11, 22),
        # Esfand
        (12, 9), (12, 19), (12, 20), (12, 29),
    },
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def is_holiday(jalali_date: jdatetime.date, persian_day_name: str) -> int:
    """
    Return 1 when the date is considered a holiday, otherwise return 0.

    A date is treated as a holiday when:
    1. It is Friday, or
    2. Its Jalali month/day pair exists in the holiday list for that Jalali year.
    """
    if persian_day_name == "جمعه":
        return 1

    year_holidays = HOLIDAYS.get(jalali_date.year, set())
    return int((jalali_date.month, jalali_date.day) in year_holidays)


def get_semester(month: int) -> tuple[int, str]:
    """
    Return the Persian semester number and label for a given Jalali month.

    Months 1-6  -> Semester 1
    Months 7-12 -> Semester 2
    """
    if month <= 6:
        return 1, "نیمسال اول"
    return 2, "نیمسال دوم"


def get_quarter(month: int) -> tuple[int, str]:
    """
    Return the Persian quarter number and season label for a given Jalali month.
    """
    if month <= 3:
        return 1, "بهار"
    if month <= 6:
        return 2, "تابستان"
    if month <= 9:
        return 3, "پاییز"
    return 4, "زمستان"


def jalali_month_start_gregorian(year: int, month: int) -> dt.date:
    """
    Return the Gregorian date corresponding to the first day of a Jalali month.
    """
    return jdatetime.date(year, month, 1).togregorian()


def calculate_week_of_month(miladi_date: dt.date, jalali_year: int, jalali_month: int) -> int:
    """
    Calculate week number within the Jalali month.

    The calculation follows the same ISO-week-based logic as the original script:
    current ISO week - first day ISO week + 1.
    """
    first_day_of_month = jalali_month_start_gregorian(jalali_year, jalali_month)
    return miladi_date.isocalendar().week - first_day_of_month.isocalendar().week + 1


def build_dimdate_record(miladi_date: dt.date) -> dict[str, object]:
    """
    Build one complete Date Dimension record for a Gregorian date.

    The function:
    - converts the Gregorian date to Jalali,
    - calculates calendar hierarchy attributes,
    - calculates week/day position attributes,
    - assigns Persian labels,
    - identifies holidays,
    - returns one dictionary suitable for conversion to a pandas DataFrame.
    """
    jalali_date = jdatetime.date.fromgregorian(date=miladi_date)

    year = jalali_date.year
    month = jalali_date.month
    day = jalali_date.day

    # Numeric business key in YYYYMMDD format.
    date_key = int(f"{year}{month:02d}{day:02d}")

    # Human-readable Jalali date.
    shamsi_date = f"{year}/{month:02d}/{day:02d}"

    # Semester and quarter classifications.
    semester, semester_name = get_semester(month)
    quarter, quarter_name = get_quarter(month)

    # Persian month and weekday names.
    month_name = PERSIAN_MONTH_NAMES[month - 1]
    day_name = PERSIAN_WEEKDAY_NAMES[miladi_date.weekday()]

    # Holiday indicator.
    holiday_flag = is_holiday(jalali_date, day_name)

    # Gregorian day of year.
    # This intentionally preserves the behavior of the original script.
    gregorian_year_start = dt.date(miladi_date.year, 1, 1)
    day_of_year = (miladi_date - gregorian_year_start).days + 1

    # Jalali quarter start converted to Gregorian for date arithmetic.
    quarter_start_month = {
        1: 1,
        2: 4,
        3: 7,
        4: 10,
    }[quarter]

    quarter_start = jalali_month_start_gregorian(year, quarter_start_month)
    day_of_quarter = (miladi_date - quarter_start).days + 1

    # Jalali semester start converted to Gregorian for date arithmetic.
    semester_start_month = 1 if semester == 1 else 7
    semester_start = jalali_month_start_gregorian(year, semester_start_month)
    day_of_semester = (miladi_date - semester_start).days + 1

    # ISO week number of the Gregorian date.
    week_of_year = miladi_date.isocalendar().week

    # Week position attributes.
    week_of_month = calculate_week_of_month(miladi_date, year, month)
    week_of_quarter = ((day_of_quarter - 1) // 7) + 1
    week_of_semester = ((day_of_semester - 1) // 7) + 1

    # Numeric month key in YYYYMM format.
    year_month = int(f"{year}{month:02d}")

    # Human-readable Persian month/year label.
    year_month_name = f"ماه {month_name} سال {year}"

    return {
        "DateKey": date_key,
        "MiladiDate": miladi_date.strftime("%Y-%m-%d"),
        "Date": shamsi_date,
        "CalendarYear": year,
        "Semester": semester,
        "Quarter": quarter,
        "MonthNo": month,
        "WeekOfMonth": week_of_month,
        "WeekOfQuarter": week_of_quarter,
        "WeekOfSemester": week_of_semester,
        "WeekOfYear": week_of_year,
        "DayOfWeek": miladi_date.weekday() + 1,
        "DayOfMonth": day,
        "DayOfQuarter": day_of_quarter,
        "DayOfSemester": day_of_semester,
        "DayOfYear": day_of_year,
        "DayName": day_name,
        "MonthName": month_name,
        "QuarterName": quarter_name,
        "SemesterName": semester_name,
        "YearMonth": year_month,
        "YearMonthName": year_month_name,
        "is holiday": holiday_flag,

        # Placeholder columns preserved from the original project.
        # They can be populated later by joining fact tables or analytical data.
        "SaleInvoice": 0,
        "SaleTarget": 0,
        "Treasury": 0,
    }


def generate_date_dimension(
    start_date: dt.date = START_DATE,
    end_date: dt.date = END_DATE,
) -> pd.DataFrame:
    """
    Generate the full Date Dimension between start_date and end_date, inclusive.

    Raises
    ------
    ValueError
        If start_date is later than end_date.
    """
    if start_date > end_date:
        raise ValueError("START_DATE cannot be later than END_DATE.")

    records: list[dict[str, object]] = []
    current_date = start_date

    while current_date <= end_date:
        records.append(build_dimdate_record(current_date))
        current_date += dt.timedelta(days=1)

    return pd.DataFrame(records)


def export_to_excel(dataframe: pd.DataFrame, output_file: Path = OUTPUT_FILE) -> None:
    """
    Export the generated Date Dimension to an Excel file.
    """
    dataframe.to_excel(output_file, index=False)


def main() -> None:
    """
    Main execution entry point.
    """
    print("=" * 70)
    print("Persian (Jalali) Date Dimension Generator")
    print("=" * 70)
    print(f"Gregorian range: {START_DATE} -> {END_DATE}")

    dim_date = generate_date_dimension()
    export_to_excel(dim_date)

    print(f"File generated: {OUTPUT_FILE.resolve()}")
    print(f"Total rows: {len(dim_date):,}")
    print("Generation completed successfully.")


if __name__ == "__main__":
    main()
