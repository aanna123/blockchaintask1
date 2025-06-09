import hashlib
import time

class Block:
    def __init__(self, data, previous_hash=''):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        print("Mining block...")
        target = '0' * difficulty
        attempts = 0
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            attempts += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {round(end_time - start_time, 2)} seconds")

block = Block("Test Mining Block")
block.mine_block(difficulty=4)
