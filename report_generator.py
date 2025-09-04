from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_report(data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    html_output = template.render(data=data)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    file_path = reports_dir / f"scan_{data['timestamp'].replace(':', '-')}.html"
    file_path.write_text(html_output, encoding="utf-8")

    return str(file_path)
