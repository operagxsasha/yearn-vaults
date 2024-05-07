from ape import project, accounts, chain
from pprint import pprint

def main():
    dev = accounts.test_accounts[0]
    # deploy token
    token = project.Token.deploy('Yearn Test', 'YFI', sender=dev)
    token.mint(dev, '30000 ether', sender=dev)
    # deploy registry
    registry = project.Registry.deploy(sender=dev)
    # deploy template
    template = project.Vault.deploy(sender=dev)
    # create release
    registry.newRelease(template, sender=dev)
    # create vault
    registry.newVault(token, dev, dev, 'Yearn Test Vault', 'yvYFI', sender=dev)
    # deploy ypermit
    ypermit = project.YearnPermit.deploy(registry, sender=dev)

    pprint({
        'chain_id': chain.provider.chain_id,
        'dev': str(dev),
        'token': str(token),
        'registry': str(registry),
        'template': str(template),
        'vault': str(registry.latestVault(token)),
        'ypermit': str(ypermit),
    })
