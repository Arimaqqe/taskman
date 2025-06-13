import importlib
import os
from pathlib import Path


def camel_case_to_snake_case(input_str: str) -> str:
    """
    >>> camel_case_to_snake_case("SomeSDK")
    'some_sdk'
    >>> camel_case_to_snake_case("RServoDrive")
    'r_servo_drive'
    >>> camel_case_to_snake_case("SDKDemo")
    'sdk_demo'
    """
    chars = []
    for c_idx, char in enumerate(input_str):
        if c_idx and char.isupper():
            nxt_idx = c_idx + 1
            # idea of the flag is to separate abbreviations
            # as new words, show them in lower case
            flag = nxt_idx >= len(input_str) or input_str[nxt_idx].isupper()
            prev_char = input_str[c_idx - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def import_all_models_from_src():
    exclude_dirs = {"alembic", "tests"}
    base_path = Path(__file__).resolve().parent.parent / "src"
    print("Imported models:")

    for path in base_path.rglob("*/models.py"):
        if path.parent.name in exclude_dirs:
            continue
        relative = path.relative_to(base_path.parent)
        module = str(relative).replace(os.sep, ".")[:-3]
        importlib.import_module(module)
        print(f"✅ {module}")
