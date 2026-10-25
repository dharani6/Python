from pathlib import Path
import xml.etree.ElementTree as ET


RESULTS_FOLDER = Path(__file__).parent / "results"
OUTPUT_XML = RESULTS_FOLDER / "output.xml"
MARKDOWN_REPORT = RESULTS_FOLDER / "README.md"


def main():
    if not OUTPUT_XML.exists():
        raise FileNotFoundError(
            f"Robot output not found: {OUTPUT_XML}. Run the Robot suite first."
        )

    root = ET.parse(OUTPUT_XML).getroot()
    summary = root.find("./statistics/total/stat")
    if summary is None:
        raise ValueError(f"Robot test summary is missing from {OUTPUT_XML}")

    tests = []
    for test in root.iter("test"):
        status = test.find("status")
        if status is not None:
            tests.append((test.get("name", "Unnamed test"), status.get("status", "UNKNOWN")))

    generated = root.get("generated", "Unknown")
    lines = [
        "# Robot Framework Test Results",
        "",
        f"**Run time:** {generated}",
        "",
        "## Summary",
        "",
        f"- **Passed:** {summary.get('pass', '0')}",
        f"- **Failed:** {summary.get('fail', '0')}",
        f"- **Skipped:** {summary.get('skip', '0')}",
        "",
        "## Test cases",
        "",
        "| Test | Result |",
        "| --- | --- |",
    ]

    for name, status in tests:
        icon = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️"}.get(status, "❔")
        lines.append(f"| {name} | {icon} {status} |")

    lines.extend(
        [
            "",
            "For the full Robot Framework report, open [report.html](report.html).",
            "For detailed test steps and messages, open [log.html](log.html).",
            "",
        ]
    )
    MARKDOWN_REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown report created: {MARKDOWN_REPORT}")


if __name__ == "__main__":
    main()
