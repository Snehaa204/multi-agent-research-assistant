from datetime import datetime
import os


def save_report(report_content):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    return filename