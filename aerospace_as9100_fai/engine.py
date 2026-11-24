"""Aerospace AS9100 Rev D & SAE AS9102 First Article Inspection (FAI Form 1, 2, 3) Engine."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional

@dataclass
class FAIDimensionalCharacteristic:
    char_index: int             # Balloon # from drawing
    dimension_name: str         # e.g., "Outer Flange Diameter"
    nominal_dimension_mm: float
    lower_tolerance_mm: float   # e.g., -0.02
    upper_tolerance_mm: float   # e.g., +0.02
    actual_measured_cmm_mm: float
    is_conforming: bool = False

class AerospaceAS9102FAIEngine:
    def __init__(self, part_number: str, serial_number: str, customer_po: str):
        self.part_number = part_number
        self.serial_number = serial_number
        self.customer_po = customer_po
        self.characteristics: List[FAIDimensionalCharacteristic] = []
        self.fai_status = "IN_PROGRESS"

    def record_cmm_measurement(self, char: FAIDimensionalCharacteristic) -> Dict[str, Any]:
        lower_limit = char.nominal_dimension_mm + char.lower_tolerance_mm
        upper_limit = char.nominal_dimension_mm + char.upper_tolerance_mm
        
        char.is_conforming = lower_limit <= char.actual_measured_cmm_mm <= upper_limit
        self.characteristics.append(char)

        return {
            "char_index": char.char_index,
            "dimension": char.dimension_name,
            "measured_value": char.actual_measured_cmm_mm,
            "is_conforming": char.is_conforming
        }

    def sign_off_as9102_fai_package(self) -> Dict[str, Any]:
        if not self.characteristics:
            raise ValueError("Cannot sign off empty FAI package.")
        
        all_passed = all(c.is_conforming for c in self.characteristics)
        self.fai_status = "ACCEPTED_AS9102_COMPLIANT" if all_passed else "REJECTED_NON_CONFORMANCE"

        return {
            "part_number": self.part_number,
            "serial_number": self.serial_number,
            "total_characteristics_evaluated": len(self.characteristics),
            "fai_decision": self.fai_status,
            "airworthiness_release_ready": all_passed
        }
