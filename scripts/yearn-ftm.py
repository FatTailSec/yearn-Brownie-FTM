from brownie import *
import csv 
import scripts.interface

def main():
    yearnVaults_ftm = [
        "0x637eC617c86D24E421328e6CAEa1d92114892439", # DAI yVault (DAI)
        "0x0DEC85e74A92c52b7F708c4B10207D9560CEFaf0", # WFTM yVault (WFTM)
        "0xEF0210eB96c7EB36AF8ed1c20306462764935607", # USDC yVault (USDC)
        "0xF137D22d7B23eeB1950B3e19d1f578c053ed9715", # Curve Geist Pool yVault (Curve Geist)
        "0xCe2Fc0bDc18BD6a4d9A725791A3DEe33F3a23BB7", # WETH yVault (WETH)
        "0x148c05caf1Bb09B5670f00D511718f733C54bC4c", # USDT yVault (USDT)
        "0x2C850cceD00ce2b14AA9D658b7Cad5dF659493Db", # YFI yVault (YFI)
        "0x0fBbf9848D969776a5Eb842EdAfAf29ef4467698", # BOO yVault (BOO)
        "0x0A0b23D9786963DE69CB2447dC125c49929419d8", # MIM yVault (MIM)
        "0xCbCaF8cB8cbeAFA927ECEE0c5C56560F83E9B7D9", # Curve Tricrypto Pool yVault (Curve Tricrypto)
        "0xf2d323621785A066E64282d2B407eAc79cC04966", # LINK yVault (LINK)
        "0x357ca46da26E1EefC195287ce9D838A6D5023ef3", # FRAX yVault (FRAX)
        "0x1e2fe8074a5ce1Bb7394856B0C618E75D823B93b", # fBEETS yVault (fBEETS)
        "0xA97E7dA01C7047D6a65f894c99bE8c832227a8BC" # Curve MIM Pool Vault (Curve MIM 3Pool)
    ]

    blockNumber = web3.eth.blockNumber
    fileName = "yearnVault-Info-ftm" + str(blockNumber) + ".csv"

    vaultHeader = [
        "Vault Name",
        "Block Number",
        "Vault Asset",
        "Price per Share",
        "Total Assets in Vault", 
        "Total Shares of Vault"
    ]
    f = open(fileName, 'w')
    writer = csv.writer(f)
    writer.writerow(vaultHeader)

    for x in range(0, len(yearnVaults_ftm)):
        vault = Contract.from_abi("null", yearnVaults_ftm[x], scripts.interface.abi)
        totalAssets_vault = vault.totalAssets()
        underlying = vault.token()
        totalSharesVault = vault.totalSupply()
        reportedPricePerShare = vault.pricePerShare()
        vaultName = vault.name()

        vault_data = [
            vaultName,
            blockNumber,
            underlying,
            yearnVaults_ftm[x],
            reportedPricePerShare,
            totalAssets_vault,
            totalSharesVault
        ]

        # Write the data to the sheet 
        writer.writerow(vault_data)

