# Brownie Simple Storage contract

### Steps:
Install pipx:

    python3 -m pip install --user pipx
    python3 pipx ensurepath

Close and reopen terminal and install brownie

    pipx install eth-brownie

Close and reopen terminal

### Create brownie project

    mkdir brownie-simple-storage
    cd brownie-simple-storage/

    brownie init

### Add SimpleStorage.sol code and compile
1. Create a file `SimpleStorage.sol` in the new `contracts/` directory
2. From the web3py-simple-storage directory, copy and paste the `SimpleStorage.sol` code into the blank   file of the same name.
3. Compile

    brownie compile

4. Deploy contract to local blockchain

    brownie run scripts/deploy.py

5. Add new accounts for testnet deployments

    brownie accounts new "account_name"

Remove or list accounts

    brownie accounts delete "account_name"
    
    brownie accounts list

### Testing

    brownie test


