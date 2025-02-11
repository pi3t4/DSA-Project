import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block(Index: {self.index}, Timestamp: {self.timestamp}, Data: {self.data}, Previous Hash: {self.previous_hash}, Hash: {self.hash})"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(index=0, timestamp=time.time(), data="Genesis Block", previous_hash="0")

    def add_block(self, data):
        last_block = self.chain[-1]
        new_index = last_block.index + 1
        new_timestamp = time.time()
        new_previous_hash = last_block.hash
        new_block = Block(new_index, new_timestamp, data, new_previous_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash for block {current_block.index}")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash for block {current_block.index}")
                return False

        return True

    def __repr__(self):
        return "\n".join(str(block) for block in self.chain)

# Example Workflow
blockchain = Blockchain()
blockchain.add_block("Alice paid Bob $10")
blockchain.add_block("Bob paid Charlie $5")

print("Blockchain:")
print(blockchain)
print("\nIs the blockchain valid?", blockchain.is_chain_valid())
print("\nTampering with Block 1...")
blockchain.chain[1].data = "Alice paid Bob $1000"
blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

print("\nTampered Blockchain:")
print(blockchain)
print("\nIs the blockchain valid after tampering?", blockchain.is_chain_valid())
