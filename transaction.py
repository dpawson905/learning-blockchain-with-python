from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain.

    Attributes:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :signiture: The signiture of the transaction.
        :amount: The amount of coins sent.
    """

    def __init__(self, sender, recipient, signiture, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signiture = signiture

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
