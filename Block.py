import hashlib
import datetime
import random
import eel
import os


def Hash(input):
    return hashlib.sha256(input.encode()).hexdigest()


class User:
    blockList = []
    prevBlock = Hash("Genesis")

    def __init__(self, name):
        self.name = name

        def __init__(self, name):
            self.name = name


class Block:
    def __init__(self, nonce, personal_hash, prev_block_hash, transaction, time_of_transaction):
        self.nonce = nonce
        self.personal_hash = personal_hash
        self.prev_block_hash = prev_block_hash
        self.transaction = transaction
        self.time_of_transaction = time_of_transaction

    def printhash(self):
        eel.console_log("Current block hash: " + self.personal_hash + "\n" +
                        "Time of transaction: " + str(self.time_of_transaction))
        eel.console_log(self.transaction)


def MineIndividualBlock(blockToMine, difficulty):
    # mines string representation of block, returns nonce
    numberToTry = 0
    timeStart = datetime.datetime.now()
    while (0 == 0):
        found = True
        for x in Hash(blockToMine + " " + str(numberToTry))[:difficulty]:
            if x != "0":
                found = False
        if found:
            data = []
            data.append(Hash(blockToMine + " " + str(numberToTry)))
            data.append(numberToTry)
            return data
        numberToTry += 1


def GenerateTransaction(userName, first_user, second_user, transaction_value):
    prev = userName.prevBlock
    time_of_transaction = datetime.datetime.now()
    transaction = first_user + " sent " + \
        str(transaction_value) + " coins to " + second_user.strip()
    data = MineIndividualBlock(
        str(transaction+str(time_of_transaction)+prev), 5)
    block_to_be_returned = Block(
        data[1], data[0], prev, transaction, time_of_transaction)
    eel.console_log("Hash of mined block: " + data[0])
    userName.prevBlock = block_to_be_returned.personal_hash
    userName.blockList.append(block_to_be_returned)


def GenerateRandomTransaction(userName):
    names = ["Rishi", "Minjoong", "Evan", "Rishabh"]
    prev = userName.prevBlock
    first_user = userName.name.strip()
    second_user = names[random.randint(0, 3)]
    transaction_value = random.randint(1, 50)
    time_of_transaction = datetime.datetime.now()
    transaction = first_user + " sent " + \
        str(transaction_value) + " coins to " + second_user.strip()
    data = MineIndividualBlock(
        str(transaction+str(time_of_transaction)+prev), 5)
    block_to_be_returned = Block(
        data[1], data[0], prev, transaction, time_of_transaction)
    eel.console_log("Hash of mined block: " + data[0])
    userName.prevBlock = block_to_be_returned.personal_hash
    userName.blockList.append(block_to_be_returned)


# eel.console_log(Hash("RishiSinh"))
user = User("BonkeyKong")


@eel.expose
def GenerateFakeTransactions():
    for i in range(5):
        GenerateRandomTransaction(user)
    for i in user.blockList:
        eel.console_log("Previous hash: " + i.prev_block_hash)
        i.printhash()


@eel.expose
def MineTransaction():
    GenerateRandomTransaction(user)
    eel.console_log("Previous hash: " + user.blockList[-1].prev_block_hash)
    user.blockList[-1].printhash()


@eel.expose
def ViewInventory():
    s = sum([int(i.transaction.split(' ')[2]) for i in user.blockList])
    eel.console_log("You have sent %d coins to other people" % s)


path = os.path.dirname(os.path.abspath(__file__))
eel.init('%s\web' % path)
eel.start('index.html', size=(1920, 1080))
