## CS 128 FA 21 Cryptocurrency Simulation Final Project
Group Name: Final Projecters  

Team members: Evan Coats(efcoats2), Rahul Gupta(rahulag2), Minjoong Kim(msk6), Rishi Sinha (rishis5)


# Overview:
For our CS128 final project, our group wanted to create working simple simulation of cryptocurrency, on a small scale. To accomplish this, our group implemented the key ideas behind how cryptocurrency works, such as coin generating, hashing, mining, and blockchain. By implementing functions as well as tests and a GUI, the user is able to simulate a blockchain cryptocurrency environment. Our program is written entirely in Python, and the GUI makes use of the Python Eel library. There was also a sizeable amount of HTML code used to create the design and interface for our project.



# Setup: 
Have python3 installed on your computer.

Run

    pip3 install eel
    
To install the required eel module for the GUI.

To run the project, simply type

    python3 Block.py

# Usage:

Upon running the commands, an interface will appear with 3 main options, showcasing our projects functionality. The first option on the left is called "Generate Transactions", 
and will randomly generate blockchain transactions for the user. The persons that the transactions are taking place between will be randomly generated, as well as the generated hashes based on the SHA-256 algorithm. To verify the blockchain's accuracy, the previous hash will also be displayed to make sure the blockchain link is accurate. 

The "Mine Transactions" will simply generate a single coin, which is then mined by the user, based on the hash, through a simple bruteforce algorithm. The info about the mined block is then displayed on the screen.  

The View Wallet option will display the total amount of coins that were sent by the user, based on the generated transactions, giving an overview of the transactions that have taken place. 

...
