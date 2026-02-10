from rfid_clone.core import MifareClassic
m = MifareClassic()
print(f"Mifare Classic 1K: {m.SECTORS_1K} sectors, {m.BLOCKS_PER_SECTOR} blocks/sector")
print(f"Block size: {m.BLOCK_SIZE} bytes")
print(f"Total: {m.SECTORS_1K * m.BLOCKS_PER_SECTOR * m.BLOCK_SIZE} bytes")
