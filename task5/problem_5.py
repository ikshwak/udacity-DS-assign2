import hashlib, time

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = self.getGMT()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous_block = None

    def __str__(self):
        return "\ntimestamp:{}\ndata:{}\nhash:{}\nprevious hash:{}".format(self.timestamp, self.data, self.hash, self.previous_hash)

    def calc_hash(self):
          sha = hashlib.sha256()
          hashData = self.data + self.timestamp
          if self.previous_hash != None:
              hashData += self.previous_hash
          hash_str = hashData.encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()

    def getGMT(self):
            gmtime = time.gmtime(time.time())
            fmtStr = "{0}-{1}-{2}:{3}/{4}/{5}"
            timestamp = fmtStr.format(gmtime.tm_hour, gmtime.tm_min, gmtime.tm_sec, gmtime.tm_mon, gmtime.tm_mday, gmtime.tm_year)
            return timestamp

class BlockList:

    def __init__(self):
        self.tail = None
        
    def __str__(self):
        temp = self.tail
        val = "MY BLOCK CHAIN"
        if temp == None:
            val += "\r\nEMPTY BLOCKCHAIN"
        while temp:
            val += "{}".format(str(temp))
            temp = temp.previous_block
            if temp != None:
                val += "\n|\n|\n\/"
        return val

    def addBlock(self,data):
        if data == None:
            print("Invalid data! cannot create the chain")
            return
        prvHash = None
        if self.tail != None:
            prvHash = self.tail.hash        

        block = Block(data,prvHash)

        if self.tail != None:
            block.previous_block = self.tail
            
        self.tail = block
        return


def test_case1():
    print("\r\nTEST CASE 1\r\n")
    blockChain = BlockList()
    count = 0
    while count <= 20:
        testDataStr = "test" + str(count)
        blockChain.addBlock(testDataStr)
        count += 1

    print(blockChain)
"""
TEST CASE 1


MY BLOCK CHAIN
timestamp:23-45-48:5/28/2019
data:test20
hash:8a92dec2608e55982adcbae0967a1db82816f9230175c697cfc46fa2594c591c
previous hash:8d30d2f69df9de83bfee81c3cfa72d7a22d49f901fa7973ef6767328c3e628d2
|
|
\/
timestamp:23-45-48:5/28/2019
data:test19
hash:8d30d2f69df9de83bfee81c3cfa72d7a22d49f901fa7973ef6767328c3e628d2
previous hash:42bc0d84a856fe8943e20e2ccaaada59d2434e39b912e1d7d96edf1590299346
|
|
\/
timestamp:23-45-48:5/28/2019
data:test18
hash:42bc0d84a856fe8943e20e2ccaaada59d2434e39b912e1d7d96edf1590299346
previous hash:32a5c76538cafeae75dd854e47d05f2338dbfcc1232ebfbd7894483b2ed9fee3
|
|
\/
timestamp:23-45-48:5/28/2019
data:test17
hash:32a5c76538cafeae75dd854e47d05f2338dbfcc1232ebfbd7894483b2ed9fee3
previous hash:8255e181d5337b5af104131113e401289dd17a463c6dbc9a5aa6d73c632ecc4d
|
|
\/
timestamp:23-45-48:5/28/2019
data:test16
hash:8255e181d5337b5af104131113e401289dd17a463c6dbc9a5aa6d73c632ecc4d
previous hash:c64be5aabfe6f02e7a64fe1ddb9641fe877c70556f929636e23222a0d99d1c05
|
|
\/
timestamp:23-45-48:5/28/2019
data:test15
hash:c64be5aabfe6f02e7a64fe1ddb9641fe877c70556f929636e23222a0d99d1c05
previous hash:c43b1762081fc6818ee38162fad1062d8bb2508b2e8510ab83222e58ddf61394
|
|
\/
timestamp:23-45-48:5/28/2019
data:test14
hash:c43b1762081fc6818ee38162fad1062d8bb2508b2e8510ab83222e58ddf61394
previous hash:53e408f187bc98bf39851075a760ab18f9a727d65581f140263aa6c5020225eb
|
|
\/
timestamp:23-45-48:5/28/2019
data:test13
hash:53e408f187bc98bf39851075a760ab18f9a727d65581f140263aa6c5020225eb
previous hash:a61fd4d56da3db8e9e11660ddeac95b632b3faabe0b092fefee3704fd257a320
|
|
\/
timestamp:23-45-48:5/28/2019
data:test12
hash:a61fd4d56da3db8e9e11660ddeac95b632b3faabe0b092fefee3704fd257a320
previous hash:a0339c92c2f17aef15fc17cac6263aa6da02d480fee66b1dd3ff376500a3f569
|
|
\/
timestamp:23-45-48:5/28/2019
data:test11
hash:a0339c92c2f17aef15fc17cac6263aa6da02d480fee66b1dd3ff376500a3f569
previous hash:a9924616b96b1d21621bc952e3aa98efb4e24dffeb70b29be3684158069e36f1
|
|
\/
timestamp:23-45-48:5/28/2019
data:test10
hash:a9924616b96b1d21621bc952e3aa98efb4e24dffeb70b29be3684158069e36f1
previous hash:73532dfb52ac4d0dacf829265d615c7bb0781d66e17e313b1d9a94e83346b3cd
|
|
\/
timestamp:23-45-48:5/28/2019
data:test9
hash:73532dfb52ac4d0dacf829265d615c7bb0781d66e17e313b1d9a94e83346b3cd
previous hash:a1c859c9d5345b63f61bd9c6fc514f75ad853013642591b02d7b3366c4070ad5
|
|
\/
timestamp:23-45-48:5/28/2019
data:test8
hash:a1c859c9d5345b63f61bd9c6fc514f75ad853013642591b02d7b3366c4070ad5
previous hash:c02098c582d843552c310a3ec3076ac706635bf532f39b83de617cc589d37f94
|
|
\/
timestamp:23-45-48:5/28/2019
data:test7
hash:c02098c582d843552c310a3ec3076ac706635bf532f39b83de617cc589d37f94
previous hash:205cae75ece241734bb24e8b49287c70af6244607b44a4ff4d62343427e902a1
|
|
\/
timestamp:23-45-48:5/28/2019
data:test6
hash:205cae75ece241734bb24e8b49287c70af6244607b44a4ff4d62343427e902a1
previous hash:0828c003b1938df142f8ce65099f82ec2621af1edcba365a823cafe7d44038a6
|
|
\/
timestamp:23-45-48:5/28/2019
data:test5
hash:0828c003b1938df142f8ce65099f82ec2621af1edcba365a823cafe7d44038a6
previous hash:7c268771197af7256407173ce2d2493ce8b2c4649e7c501c32622ab0bd23824a
|
|
\/
timestamp:23-45-48:5/28/2019
data:test4
hash:7c268771197af7256407173ce2d2493ce8b2c4649e7c501c32622ab0bd23824a
previous hash:237ad305d054f4c7f06a801c43c21e6786864e07c83e86db6cc7ad93835c9a92
|
|
\/
timestamp:23-45-48:5/28/2019
data:test3
hash:237ad305d054f4c7f06a801c43c21e6786864e07c83e86db6cc7ad93835c9a92
previous hash:09bfe9c10fe3850ccdc2bde4cf02bf9fdfe89d797962cc261742dd20a67b1f6e
|
|
\/
timestamp:23-45-48:5/28/2019
data:test2
hash:09bfe9c10fe3850ccdc2bde4cf02bf9fdfe89d797962cc261742dd20a67b1f6e
previous hash:a1ac245601eb751cd16c17dfd12762738f810ceacc84e6923a76aae0352b16fe
|
|
\/
timestamp:23-45-48:5/28/2019
data:test1
hash:a1ac245601eb751cd16c17dfd12762738f810ceacc84e6923a76aae0352b16fe
previous hash:590c9f8430c7435807df8ba9a476e3f1295d46ef210f6efae2043a4c085a569e
|
|
\/
timestamp:23-45-48:5/28/2019
data:test0
hash:590c9f8430c7435807df8ba9a476e3f1295d46ef210f6efae2043a4c085a569e
previous hash:None
"""
test_case1()


def test_case2():
    print("\r\nTEST CASE 2\r\n")
    blockChain = BlockList()
    print(blockChain)
"""
MY BLOCK CHAIN
EMPTY BLOCKCHAIN
"""
test_case2()


def test_case3():
    print("\r\nTEST CASE 3\r\n")
    blockChain = BlockList()
    count = 0
    while count <= 20:
        testDataStr = None
        blockChain.addBlock(testDataStr)
        count += 1

    print(blockChain)
"""
TEST CASE 3


Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
Invalid data! cannot create the chain
MY BLOCK CHAIN

EMPTY BLOCKCHAIN
"""
test_case3()
