from datetime import date, datetime
import unittest
import Block

class TestingStringMethods(unittest.TestCase):
    # string equal

    def test_hash_function(self): 
        # testing if hash function works as expected 
        self.assertTrue(Block.Hash("Rishi Sinha") != Block.Hash("Rishi Sinha  "))
        self.assertTrue(Block.Hash("hello") == Block.Hash("hello"))
        self.assertTrue(Block.Hash("1234") == Block.Hash("1234"))
        self.assertTrue(Block.Hash("chicken ") != Block.Hash("fish"))
    # comparing the two strings
    def test_mining_Functionality(self):
        user = Block.User("BonkeyKong")

        prev_block_hash = user.prevBlock
        time_of_transaction = datetime.now
        Block.GenerateTransaction(user,"Rishi", "Minjoong", 100)
        prev_block_hash = user.prevBlock
        Block.GenerateTransaction(user,"Rishi", "Minjoong",200)
        current_block = user.blockList[len(user.blockList)-1]

        ### checking size of chain
        self.assertTrue(current_block.personal_hash != prev_block_hash)
        self.assertTrue(current_block.time_of_transaction != time_of_transaction)
        self.assertTrue(current_block.prev_block_hash == prev_block_hash)

        self.assertTrue(user.blockList[len(user.blockList)-1].personal_hash != user.blockList[0].personal_hash)
        for x in user.blockList:
            self.assertTrue(x.personal_hash[:5] == "00000")

    def test_transaction_generation(self):
        user = Block.User("BonkeyKong")
        prev_block_hash = user.prevBlock
        time_of_transaction = datetime.now
        for x in range(5):
            Block.GenerateRandomTransaction(user)

        self.assertTrue(user.blockList[len(user.blockList)-1].personal_hash != user.blockList[0].prev_block_hash)
        self.assertTrue(user.blockList[len(user.blockList)-1].time_of_transaction != user.blockList[0].time_of_transaction)
        self.assertTrue(user.blockList[len(user.blockList)-1].prev_block_hash != user.blockList[0].prev_block_hash)
        self.assertTrue(user.blockList[len(user.blockList)-1].personal_hash != user.blockList[0].personal_hash)
        self.assertTrue(user.blockList[len(user.blockList)-1].time_of_transaction )
        for x in user.blockList:
            self.assertTrue(x.personal_hash[:5] == "00000")





    # def test_string_case(self):
    #     # if both arguments are equal then it's succes
    #     self.assertEqual('tutorialspoint'.upper(), 'TUTORIALSPOINT')
    # # checking whether a string is upper or not
    # def test_is_string_upper(self):
    #     # used to check whether the statement is True or False
    #     # the result of expression inside the **assertTrue** must be True to pass the test case
    #     # the result of expression inside the **assertFalse** must be False to pass the test case
    #     self.assertTrue('TUTORIALSPOINt'.isupper())
    #     self.assertFalse('TUTORIALSpoint'.isupper())
# running the tests
unittest.main()


