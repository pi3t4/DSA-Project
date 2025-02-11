# Simple Blockchain Implementation in Python

This Python script implements a basic blockchain system using the `hashlib` library for cryptographic hashing and the `time` module for timestamping. The implementation includes classes for blocks and the blockchain itself, as well as methods to add blocks, validate the chain, and demonstrate tampering detection.

---

## Table of Contents

1. [Overview](#overview)
2. [Key Components](#key-components)
3. [How It Works](#how-it-works)
4. [Usage Instructions](#usage-instructions)

---

## Overview

A blockchain is a distributed ledger technology that allows data to be stored globally on thousands of servers while letting anyone see every transaction that occurs. This implementation provides a simplified version of a blockchain with the following features:

- **Blocks**: Each block contains an index, timestamp, data, previous hash, and its own hash.
- **Blockchain**: A collection of blocks linked together via their hashes.
- **Validation**: Ensures the integrity of the blockchain by checking the consistency of hashes and previous hashes.

---

## Key Components

### 1. Block Class
- Represents a single block in the blockchain.
- **Attributes**:
  - `index`: Position of the block in the chain.
  - `timestamp`: Time when the block was created.
  - `data`: Information stored in the block (e.g., transaction details).
  - `previous_hash`: Hash of the previous block in the chain.
  - `hash`: Cryptographic hash of the block's contents.
- **Methods**:
  - `calculate_hash()`: Computes the SHA-256 hash of the block's data.
  - `__repr__()`: Provides a string representation of the block for easy debugging.

### 2. Blockchain Class
- Represents the entire blockchain.
- **Attributes**:
  - `chain`: List of blocks in the blockchain.
- **Methods**:
  - `create_genesis_block()`: Creates the first block in the chain (genesis block).
  - `add_block(data)`: Adds a new block with the specified data to the chain.
  - `is_chain_valid()`: Verifies the integrity of the blockchain by checking hashes and previous hashes.
  - `__repr__()`: Provides a string representation of the entire blockchain.

---

## How It Works

1. **Initialization**:
   - A `Blockchain` object is initialized with a genesis block, which serves as the starting point of the chain.

2. **Adding Blocks**:
   - New blocks are created with incremental indices, current timestamps, provided data, and the hash of the previous block.
   - Each block calculates its own hash based on its attributes.

3. **Validation**:
   - The `is_chain_valid()` method ensures that:
     - Each block's hash matches the result of recalculating its hash.
     - Each block's `previous_hash` matches the hash of the preceding block.

4. **Tampering Detection**:
   - If any block's data or hash is altered, the validation process will detect inconsistencies and flag the blockchain as invalid.

---

## Usage Instructions

1. Ensure Python 3.x is installed on your system.
2. Save the code to a file, e.g., `Min-Block.py`.
3. Run the script using the command:
   ```bash
    git clone https://github.com/pi3t4/Mini-Blockchain.git  
   cd Mini-Blockchain
   python Min-Block.py
   ```
