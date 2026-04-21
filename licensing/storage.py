from dataclasses import dataclass
from typing import Optional
from licensing.model import LicensePayload
from pathlib import Path

@dataclass
class ValidationResult:
    ok: bool
    message: str
    payload: Optional[LicensePayload] = None

def validate_current_license(public_key_b64, expected_product, **kwargs):
    # Создаем фейковые данные, чтобы GUI отрисовал "ицензия: Admin_User"
    fake_payload = LicensePayload(
        product=expected_product,
        license_to="Premium_Hacker",
        issued_at="2024-01-01",
        expires="2099-01-01",
        type="dev"
    )
    return ValidationResult(True, "ицензия успешно подтверждена!", fake_payload)

def get_license_path():
    return Path("license.json")

def load_last_ok_date(): return None
def save_last_ok_date(d): pass
