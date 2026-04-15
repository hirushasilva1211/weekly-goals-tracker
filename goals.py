import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl import load_workbook
import os

FILE = "weekly_goals.xlsx"

def get_or_create_workbook():
    if os.path.exists(FILE):
        return load_workbook(FILE)
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Goals"

    # Define thick border
    thick = Side(style="thick")
    thick_border = Border(left=thick, right=thick, top=thick, bottom=thick)

    # Define background color (steel blue)
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

    # Write headers with bold font + thick border + background color
    headers = ["Week", "Goal", "Status"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")  # white text
        cell.border = thick_border
        cell.fill = header_fill

    wb.save(FILE)
    return wb

def add_week(week_label, goals):
    wb = get_or_create_workbook()
    ws = wb["Goals"]

    start_row = ws.max_row + 1  # Next empty row after existing data

    for i, (goal, status) in enumerate(goals):
        row = start_row + i
        cell1 = ws.cell(row=row, column=2, value=goal)
        cell2 = ws.cell(row=row, column=3, value="✅ Done" if status else "❌ Not Done")

    # Merge the "Week" column across all goal rows
    end_row = start_row + len(goals) - 1
    ws.merge_cells(f"A{start_row}:A{end_row}")

    # Write the week label into the merged cell
    merged_cell = ws.cell(row=start_row, column=1, value=week_label)
    merged_cell.alignment = Alignment(vertical="center", horizontal="center", wrap_text=True)
    merged_cell.font = Font(bold=True)

    wb.save(FILE)
    print(f"✅ Saved {len(goals)} goals for {week_label}")

# --- Usage ---
week = "Week 3"
goals = [
    ("Learn Docker basics", True),
    ("Complete internship task", False),
    ("Read 15 pages", True),
    ("Review Angular signals", True),
]

add_week(week, goals)