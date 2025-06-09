import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

# Create a simple chain of 3 blocks
blockchain = []
genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

block1 = Block(1, "Block 1 Data", genesis_block.hash)
blockchain.append(block1)

block2 = Block(2, "Block 2 Data", block1.hash)
blockchain.append(block2)

# Print block hashes
for block in blockchain:
    print(f"Block {block.index} Hash: {block.hash}")

# Tampering Block 1
print("\nTampering Block 1...")
block1.data = "Hacked Data"
block1.hash = block1.calculate_hash()

# Print block hashes again
for block in blockchain:
    print(f"Block {block.index} Hash: {block.hash}")
