import requests
from rich.console import Console
from report_generator import generate_report
from datetime import datetime

console = Console()

# Security headers to check
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Forces HTTPS",
    "Content-Security-Policy": "Controls sources of scripts, styles, etc.",
    "X-Frame-Options": "Prevents clickjacking",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "Referrer-Policy": "Controls referrer info leakage",
    "Permissions-Policy": "Controls access to features (camera, mic, etc.)"
}

def scan_site(url: str):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
    except Exception as e:
        console.print(f"[red]❌ Failed to fetch {url}: {e}[/red]")
        return None

    console.print(f"[bold cyan]Scanning {url}...[/bold cyan]\n")

    results = {}
    score = 0
    max_score = len(SECURITY_HEADERS)

    for header, desc in SECURITY_HEADERS.items():
        if header in headers:
            results[header] = ("✅ Present", desc)
            score += 1
        else:
            results[header] = ("❌ Missing", desc)

    grade = calculate_grade(score, max_score)

    console.print(f"\n[bold]Overall Grade: {grade}[/bold]")
    return {
        "url": url,
        "results": results,
        "grade": grade,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def calculate_grade(score, max_score):
    percentage = (score / max_score) * 100
    if percentage == 100:
        return "A+"
    elif percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        console.print("[yellow]Usage: python scanner.py <url>[/yellow]")
        sys.exit(1)

    url = sys.argv[1]
    report_data = scan_site(url)

    if report_data:
        generate_report(report_data)
        console.print("[green]Report generated successfully in ./reports[/green]")
