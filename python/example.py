

import PoolSpace

my_wallet_address='0x40f32d481b8bec1e5c48a3fb1254c378812d94bbeee5930f55d1571fc9d36772'
client=PoolSpace.PoolSpaceClient(my_wallet_address)

#Print all data from the endpoint
#print(client.printAll())

print("Unpaid balance: "+str(client.unpaidBalance()))
print("Total paid: "+str(client.totalPaidInXCH()))
print("Block found: "+str(client.blocksFound()))
print("Estimeted plot: "+str(client.estimatedPlots()))
print("Rank: "+str(client.rank()))




