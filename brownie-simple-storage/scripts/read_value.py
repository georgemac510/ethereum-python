from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    # take the index that is one less than the length
    print(simple_storage.retrieve())


def main():
    read_contract()