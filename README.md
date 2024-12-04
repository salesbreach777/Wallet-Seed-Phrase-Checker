# Wallet Seed Phrase Checker  

**Disclaimer**: This project is for educational purposes only. Using this tool to access wallets that do not belong to you is illegal and unethical. Always ensure you have permission to access any wallet with this tool. Misuse of this tool is strictly discouraged.  

---

## Overview  

The Wallet Seed Phrase Checker reads a `seeds.txt` file containing wallet seed phrases, generates wallet addresses, and checks if any of them have a balance. The results are saved in a `results.txt` file for further review.  

---

## Features  

- Load seed phrases from a `seeds.txt` file.  
- Generate wallet addresses from each seed phrase.  
- Check wallet balances via the Ethereum blockchain.  
- Save wallets with balances into a `results.txt` file.  

---

## Getting Started  

### Prerequisites  

- Python 3.x  
- Ethereum node (e.g., Infura)  

### Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/FITIMDOTORG/Wallet-Seed-Phrase-Checker.git

## Usage
Add your Ethereum node connection URL (e.g., Infura) in checker.py.
Populate seeds.txt with seed phrases to check.
## Run the script:
- python checker.py
Check results.txt for wallets with balances.
   
## Important Notes
Ensure you have permission to check the wallets listed in seeds.txt.
Misuse of this tool can lead to legal consequences.
Consider implementing rate-limiting or additional error handling for large datasets.
   
