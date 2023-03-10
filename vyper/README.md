# Vyper smart contracts with a virtual environment

### Setting up virtual environment

    python3 -m venv myvyper
    source myvyper/bin/activate

    to exit: deactivate

### Compile contract
        
    cd myvyper/

Returned bytecode

    vyper contracts/Crowdfund.vy

Returns all data

    vyper -f abi,bytecode,bytecode_runtime,ir,asm,source_map,method_identifiers contracts/Crowdfund.vy

### Deploy to a testnet using Remix

1. Go to https://remix.ethereum.org/
2. Install Remix plugin by clickng on the Remix `coder with headphones` logo and choose `Remix Plugin`
3. Type in `Vyper` and install plugin
4. Click on `Files` logo and create a new file such as `Crowdfund.vy`
5. Copy and paste the code from this repo for `Crowdfund.vy`
6. Choose the `V` logo in the left-hand pane.
7. Choose `Remote Compiler` and compile the contract.
8. Click on the Ether logo, then choose the `Injected provider - Metamask`. Make sure Metamask is unlocked and set to the Goerli testnet and it is funded with Goerli testnet ETH.
9. If using the `Crowdfund.vy` contract, navigate to `DEPLOY`. Click on the drop-down menu and paste your Goerli wallet address into the `_BENEFICIARY` field, `5000` into the `_GOAL` field and `32600` into the `_TIMELIMIT` field. Click on `transact`.
10. Navigate to lower left-hand panel to interact with newly deployed contract or copy and paste your new contract address into the input field at https://goerli.etherscan.io/. If you interact with the contract on Remix, you can see the transactions show up under the `Transactions` tab in the middle of the Etherscan page.

The deployed contract from this tutorial can be found at: https://goerli.etherscan.io/address/0x7a2a399d9b13405eae6db4d5f3bfa8fddb8b31b5

