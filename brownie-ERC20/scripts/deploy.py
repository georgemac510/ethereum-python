from brownie import accounts, config, SafePy, network

def deploy_safe_py():
    account = get_account()
    safe_py = SafePy.deploy({"from":account}, publish_source=True)
    print(safe_py)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else: 
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_safe_py() 