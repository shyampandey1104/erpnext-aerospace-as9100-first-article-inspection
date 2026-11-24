import unittest
from aerospace_as9100_fai.engine import FAIDimensionalCharacteristic, AerospaceAS9102FAIEngine

class TestAerospaceAS9102FAIEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AerospaceAS9102FAIEngine(
            part_number="A320-WING-RIB-042", serial_number="SN-2026-AER-001", customer_po="PO-AIRBUS-9981"
        )

    def test_fai_acceptance(self):
        c1 = FAIDimensionalCharacteristic(1, "Bore ID", 25.000, -0.010, 0.010, 25.004)
        c2 = FAIDimensionalCharacteristic(2, "Flange Thickness", 12.500, -0.050, 0.050, 12.520)
        self.engine.record_cmm_measurement(c1)
        self.engine.record_cmm_measurement(c2)

        res = self.engine.sign_off_as9102_fai_package()
        self.assertEqual(res["fai_decision"], "ACCEPTED_AS9102_COMPLIANT")
        self.assertTrue(res["airworthiness_release_ready"])

    def test_fai_rejection_out_of_tolerance(self):
        c_bad = FAIDimensionalCharacteristic(1, "Pin Diameter", 10.000, -0.005, 0.005, 10.015) # out of tolerance
        self.engine.record_cmm_measurement(c_bad)
        res = self.engine.sign_off_as9102_fai_package()
        self.assertEqual(res["fai_decision"], "REJECTED_NON_CONFORMANCE")
        self.assertFalse(res["airworthiness_release_ready"])

if __name__ == "__main__":
    unittest.main()
