"""RFID Core Engine"""
import os, json, hashlib, struct, time

class MifareClassic:
    SECTORS_1K = 16
    BLOCKS_PER_SECTOR = 4
    BLOCK_SIZE = 16
    
    def __init__(self):
        self.uid = None
        self.data = {}
        self.keys = {}
    
    def parse_dump(self, dump_data):
        """Parse a Mifare Classic 1K dump (1024 bytes)"""
        if len(dump_data) != 1024:
            raise ValueError(f"Invalid dump size: {len(dump_data)}, expected 1024")
        self.uid = dump_data[:4].hex()
        for sector in range(self.SECTORS_1K):
            self.data[sector] = {}
            for block in range(self.BLOCKS_PER_SECTOR):
                offset = (sector * self.BLOCKS_PER_SECTOR + block) * self.BLOCK_SIZE
                self.data[sector][block] = dump_data[offset:offset+self.BLOCK_SIZE]
            # Last block is sector trailer (keys + access bits)
            trailer = self.data[sector][3]
            self.keys[sector] = {"key_a": trailer[:6].hex(), "access_bits": trailer[6:10].hex(), "key_b": trailer[10:].hex()}
        return self.data
    
    def clone_card(self, source_dump, target_uid=None):
        """Generate clone data"""
        clone = bytearray(source_dump)
        if target_uid:
            uid_bytes = bytes.fromhex(target_uid)
            clone[:4] = uid_bytes
            # Recalculate BCC
            clone[4] = clone[0] ^ clone[1] ^ clone[2] ^ clone[3]
        return bytes(clone)
    
    def crack_keys(self, known_key="FFFFFFFFFFFF"):
        """Simulate key recovery (darkside/nested attack)"""
        return {"method": "nested", "known_key": known_key,
                "status": "requires_proxmark", "note": "Use pm3 for actual key recovery"}

class EM410x:
    def decode_id(self, raw_bits):
        """Decode EM4100 ID from raw bitstream"""
        # 64-bit data: 9 header bits + 10 rows of 5 bits (4 data + 1 parity) + 4 column parity + stop
        if len(raw_bits) < 64: return None
        card_id = 0
        for row in range(10):
            offset = 9 + row * 5
            for bit in range(4):
                card_id = (card_id << 1) | raw_bits[offset + bit]
        return f"{card_id:010X}"
    
    def generate_clone_data(self, card_id):
        """Generate data for EM4100 clone"""
        return {"card_id": card_id, "format": "em410x", "frequency": "125kHz",
                "note": "Use T5577 or compatible writable tag"}
