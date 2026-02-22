"""
Generate HTML table from SQLite usage logs database.
For mockup screenshot purposes.
"""

import sqlite3

DB_PATH = "projects/streamlit-center/streamlit_usage_logs.db"
HTML_PATH = "projects/streamlit-center/usage_logs_table.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>Usage Logs</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #ffffff;
            color: #333333;
            padding: 20px;
        }}
        h2 {{
            color: #333333;
            margin-bottom: 16px;
        }}
        table {{
            border-collapse: collapse;
            width: auto;
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
        }}
        th {{
            background-color: #f5f5f5;
            color: #333333;
            padding: 6px 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #e0e0e0;
        }}
        td {{
            padding: 5px 12px;
            border-top: 1px solid #e0e0e0;
        }}
        tr:hover {{
            background-color: #f9f9f9;
        }}
    </style>
</head>
<body>
    <h2>usage_logs</h2>
    <table>
        <thead>
            <tr>
                <th>id</th>
                <th>visit_date</th>
                <th>user_id</th>
                <th>page_visited</th>
            </tr>
        </thead>
        <tbody>
{rows}
        </tbody>
    </table>
</body>
</html>
"""


def generate_html():
    """Read from database and generate HTML table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, visit_date, user_id, page_visited FROM usage_logs ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    # Generate table rows
    row_html = ""
    for row in rows:
        row_html += f"            <tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n"

    html_content = HTML_TEMPLATE.format(rows=row_html.rstrip())

    with open(HTML_PATH, "w") as f:
        f.write(html_content)

    print(f"HTML table generated at: {HTML_PATH}")


if __name__ == "__main__":
    generate_html()
