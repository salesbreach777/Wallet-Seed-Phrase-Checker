import os
from web3 import Web3
from eth_account import Account

# Configure your Ethereum node URL
INFURA_URL = "https://mainnet.infura.io/v3/34d318c229e849488890fac329d58122"

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    print("Error: Unable to connect to the Ethereum node.")
    exit()

# Load seed phrases
def load_seeds(file_path="seeds.txt"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        exit()
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

# Check balance for a wallet address
def check_balance(address):
    try:
        balance = web3.eth.get_balance(address)
        return web3.fromWei(balance, "ether")
    except Exception as e:
        print(f"Error checking balance for {address}: {e}")
        return None

# Main function
def main():
    seeds = load_seeds()
    print(f"Loaded {len(seeds)} seed phrases.")
    results = []

    for i, seed in enumerate(seeds, 1):
        try:
            # Generate wallet from seed
            wallet = Account.from_mnemonic(seed)
            address = wallet.address
            print(f"[{i}/{len(seeds)}] Checking wallet: {address}")

            # Check wallet balance
            balance = check_balance(address)
            if balance and balance > 0:
                print(f"Wallet {address} has a balance of {balance} ETH.")
                results.append(f"{address} - {balance} ETH (Seed: {seed})")
            else:
                print(f"Wallet {address} has no balance.")
        except Exception as e:
            print(f"Error with seed: {seed}, {e}")

    # Save results
    if results:
        with open("results.txt", "w") as file:
            file.write("\n".join(results))
        print("Results saved to results.txt")
    else:
        print("No wallets with balance found.")

if __name__ == "__main__":
    main()
