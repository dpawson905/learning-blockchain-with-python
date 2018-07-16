from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        # self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

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
        print('5: Create wallet')
        print('6: Load wallet')
        print('7: Save wallet')
        print('q: Quit\n')

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            self.print_choices()
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signiture = self.wallet.sign_transaction(
                    self.wallet.public_key, recipient, amount=amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signiture, amount=amount):
                    print('Added transaction')
                else:
                    print(
                        f'Transaction failed you tried to send {amount} but you do not have sufficient funds!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining has failed, No wallet loaded.')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice in ['q', 'Q']:
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')

            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                break
            print(
                f'Your Balance: {self.blockchain.get_balance():6.2f}')

        # print(blockchain)
        print('Done')


if __name__ == '__main__':
    node = Node()
    node.listen_for_input()
