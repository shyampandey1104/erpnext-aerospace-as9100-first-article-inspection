# ERPNext Aerospace AS9100 Rev D & SAE AS9102 First Article Inspection (FAI) Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![Aerospace Quality](https://img.shields.io/badge/AS9100-Rev%20D%20Certified-blue.svg)]()
[![SAE AS9102](https://img.shields.io/badge/SAE-AS9102%20FAI%20Form%201--3-orange.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Precision CNC machining and composite manufacturing suppliers delivering flight-critical components to aerospace OEMs (Airbus, Boeing, HAL, ISRO) must comply with **SAE AS9102 First Article Inspection (FAI)** under AS9100 Rev D quality management systems:
1. **Three Mandatory AS9102 Forms:** FAI packages require complete generation of **Form 1** (Part Number Accountability), **Form 2** (Product Process & Materials), and **Form 3** (Characteristic Design Verification).
2. **Drawing Ballooning & CMM Verification:** Every dimension, geometric tolerance, and note on the engineering blueprint must be mapped to CMM (Coordinate Measuring Machine) inspection logs with strict upper and lower tolerance limits.
3. **Catastrophic Shipment Rejection:** A single non-conforming dimension or unverified raw material test certificate (MTC) causes the entire aerospace batch to be quarantined with severe commercial chargebacks.

This Frappe application implements an automated AS9102 FAI execution engine with drawing balloon mapping and automated pass/fail sign-offs.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Customer Aerospace PO & Ballooned Engineering Drawing"] -->|Generate FAI Traveler| B["AS9102 FAI Master Package"]
    B -->|Form 1: Part & Sub-tier Indexing| C["Part Number Accountability"]
    B -->|Form 2: Mill Test Certs & NADCAP Processes| D["Material & Process Verification"]
    B -->|Form 3: Ballooned Dimension Matrix| E["Characteristic Design Verification"]
    F["CMM Automated Measurement Logs (CSV / Direct)| Ingestion"] --> E
    E -->|Evaluate Upper & Lower Tolerance Limits| G{"All Dimensions Conforming?"}
    G -->|Yes (Zero Deviations)| H["Status: ACCEPTED AS9102 COMPLIANT (Airworthiness Release)"]
    G -->|No (Out of Tolerance)| I["Status: REJECTED (Non-Conformance Quarantine Lock)"]
```

---

## 🚀 Key Engineering Capabilities

- **SAE AS9102 Form 1, 2, 3 Generation:** Programmatically compiles full First Article Inspection dossiers.
- **Automated CMM Tolerance Evaluation:** Ingests dimensional readings and validates against dynamic micron-level upper/lower tolerances.
- **Airworthiness Release Gate:** Software locks prevent ERPNext Delivery Notes from submitting until the FAI package is digitally signed off.
- **Raw Material & NADCAP Traceability:** Tracks heat numbers, mill test reports, and special process certifications.

---

## 📂 Frappe DocType Schema & Data Structure

```text
aerospace_as9100_fai/
├── aerospace_as9100_fai_core/
│   ├── doctype/
│   │   ├── as9102_fai_package/
│   │   │   ├── as9102_fai_package.json
│   │   │   ├── as9102_fai_package.py
│   │   │   └── as9102_fai_package.js
│   │   └── fai_characteristic_dimension/
│   │       └── fai_characteristic_dimension.json
│   └── workspace/
│       └── aerospace_as9100_fai_workspace/
│           └── aerospace_as9100_fai_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/aerospace_as9100_fai.api.record_cmm_measurement`
- **Whitelisted Method:** `@frappe.whitelist() def sign_off_as9102_fai_package()`
- **Hooks Event:** `before_submit` of `Delivery Note` checks for approved AS9102 FAI certificates.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/erpnext-aerospace-as9100-first-article-inspection
bench --site erp.yourdomain.com install-app aerospace_as9100_fai
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Aerospace Machining Facilities, Defence Contractors, and Precision Toolrooms.
