import requests
import subprocess
import json


endpoint='https://api-mainnet.pool.space/api/farms/'


class PoolSpaceClient():
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        self.web_address=(endpoint+wallet_address)
        stdout=subprocess.run(f'curl {self.web_address}',shell=True,capture_output=True).stdout
        self.serialized_data=json.loads(stdout)
        
       

    def requestData(self):
        return self.serialized_data

    def unpaidBalance(self):
        return self.serialized_data["unpaidBalanceInXCH"]
    
    def totalPaidInXCH(self):
        return self.serialized_data["totalPaidInXCH"]

    def blocksFound(self):
        return self.serialized_data["blocksFound"]
    
    def estimatedPlotSizeTiB(self):
        return self.serialized_data["estimatedPlotSizeTiB"]

    def estimatedPlots(self):
        return self.serialized_data["estimatedPlots"]

    def pendingPoints(self):
        return self.serialized_data["pendingPoints"]

    def rank(self):
        return self.serialized_data["rank"]
    

    def printAll(self):
        for i in self.serialized_data:
            print(i+' ==> '+str(self.serialized_data[i]))
    


