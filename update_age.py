import re
from datetime import date

BIRTH_DATE = date(2007, 9, 16)  # <-- change to your birth date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

age = calculate_age(BIRTH_DATE)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!--AGE-->.*?<!--/AGE-->",
    f"<!--AGE-->{age}<!--/AGE-->",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
