from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

BASE_DIR = Path(__file__).resolve().parent.parent
MEMBERS_DIR = BASE_DIR / "content/pages/members"

today = datetime.today().date()

expired_per_staff = defaultdict(list)


def extract_field(content, field):
    match = re.search(rf"^{field}:\s*(.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else None


for md_file in MEMBERS_DIR.glob("*.md"):
    content = md_file.read_text(encoding="utf-8")

    member_name = extract_field(content, "name")
    check_staff = extract_field(content, "check_staff")
    check_date = extract_field(content, "check_date")

    if not member_name or not check_staff or not check_date:
        continue

    try:
        date_obj = datetime.strptime(check_date, "%Y-%m-%d").date()
    except ValueError:
        print(f"Skipping invalid date in {md_file.name}: {check_date}")
        continue

    if date_obj < today:
        expired_per_staff[check_staff].append((member_name, check_date))


if not expired_per_staff:
    print("No expired checks found.")
else:
    for staff in sorted(expired_per_staff):
        print(f"\n=== {staff} ===")

        for member, date in sorted(expired_per_staff[staff], key=lambda x: x[1]):
            print(f"- {member}")