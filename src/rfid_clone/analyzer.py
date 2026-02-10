"""RFID security analysis"""
import json

class AccessControlAnalyzer:
    VULNERABILITIES = {
        "default_keys": {"severity": "CRITICAL", "desc": "Default Mifare keys in use"},
        "no_diversification": {"severity": "HIGH", "desc": "Same keys across all sectors"},
        "uid_only_auth": {"severity": "CRITICAL", "desc": "Authentication based only on UID"},
        "static_uid": {"severity": "MEDIUM", "desc": "Non-random UID"},
    }
    
    def analyze_card(self, card_data):
        findings = []
        if isinstance(card_data, dict) and "keys" in card_data:
            keys = card_data["keys"]
            default_keys = ["FFFFFFFFFFFF", "A0A1A2A3A4A5", "000000000000"]
            for sector, key_data in keys.items():
                if key_data.get("key_a","").upper() in default_keys:
                    findings.append({"sector": sector, **self.VULNERABILITIES["default_keys"]})
            all_keys = [k.get("key_a") for k in keys.values()]
            if len(set(all_keys)) == 1:
                findings.append(self.VULNERABILITIES["no_diversification"])
        return findings
    
    def recommend_mitigations(self):
        return ["Use diversified keys per card", "Implement mutual authentication",
                "Use DESFire EV2+ instead of Classic", "Implement anti-clone measures",
                "Add server-side validation", "Use encrypted communication"]
