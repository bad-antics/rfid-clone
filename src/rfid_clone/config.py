"""RFID Clone Config"""
CARD_TYPES = {"em410x": "125kHz", "hid_prox": "125kHz", "mifare_classic_1k": "13.56MHz", "mifare_classic_4k": "13.56MHz", "mifare_ultralight": "13.56MHz", "ntag213": "13.56MHz", "desfire": "13.56MHz"}
DEFAULT_KEYS = ["FFFFFFFFFFFF", "A0A1A2A3A4A5", "D3F7D3F7D3F7", "000000000000", "B0B1B2B3B4B5", "4D3A99C351DD"]
PROXMARK_PORT = "/dev/ttyACM0"
SAFE_MODE = True
