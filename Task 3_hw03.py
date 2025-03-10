"""    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   """

import re
def normalize_phone(phone_number: str) -> str:
    # Remove all symbols except numbers and '+'
    corrected_number = re.sub(r"\D", "", phone_number)
    if not corrected_number.startswith("+"):
        return f'+{corrected_number}'
    if not corrected_number.startswith("380"):
        return f'+{corrected_number}'
    if not corrected_number.startswith("/d"):
        return f'+38{corrected_number}' 
   

    return corrected_number

raw_numbers = [
    "    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)