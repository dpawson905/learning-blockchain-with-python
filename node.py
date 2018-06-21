from uuid import uuid4

from blockchain import Blockchain
from verification import Verification


class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'Darrell'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returns the input of the user (a new transaction amount) as a float. """
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Enter your transaction amount please: '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)

    def print_choices(self):
        """ Gives the options to the user for the blockchain """
        print('\nPlease choose')
        print('1: Add a new transaction')
        print('2: Mine a new block')
        print('3: Output the blockchain blocks')
        print('4: Check transaction validity')
        print('q: Quit\n')

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            self.print_choices()
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction')
                else:
                    print('Transaction failed')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')

            elif user_choice in ['q', 'Q']:
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            verifier = Verification()
            if not verifier.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                break
            print(
                f'{self.id}\'s Balance: {self.blockchain.get_balance():6.2f}')

        # print(blockchain)
        print('Done')


node = Node()
node.listen_for_input()
