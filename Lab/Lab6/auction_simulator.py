"""
Implements the observer pattern and simulates a simple auction.
"""
import random


def get_valid_user_input_for_specified_type(msg, type_converter_function):
    """
    Asks user to enter input until the user enters an input that can be converted using the type_converter_function.
    :param msg: A string message that prompts for user input.
    :param type_converter_function: A function that converts the parameter to a type, such as built in function int().
    :return: User input in specified type.
    """
    while True:
        try:
            return_value = type_converter_function(input(msg))
            return return_value
        except ValueError:
            continue


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def get_highest_bid(self):
        """
        Returns the current highest bid amount.
        :return: A positive number
        """
        return self._highest_bid

    def get_highest_bidder(self):
        """
        Returns the current highest bidder.
        :return: A Bidder
        """
        return self._highest_bidder

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()
        self._highest_bidder = None
        self._highest_bid = 0

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            if bidder is not self._highest_bidder:
                bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            if bidder != "Starting Bid":
                print(bidder, " bidded", int(bid), " in response to ", self._highest_bidder, "'s bid of ",
                      int(self._highest_bid), "!")

            self._highest_bid = bid
            self._highest_bidder = bidder
            self._notify_bidders()


class Bidder:

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        if self.bid_probability > random.random():
            new_bid_amount = auctioneer.get_highest_bid() * self.bid_increase_perc
            if self.budget >= new_bid_amount:
                auctioneer.accept_bid(new_bid_amount, self)
                self.highest_bid = new_bid_amount

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._bidders = bidders

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        auctioneer = Auctioneer()

        print("Auctioning ", item, "starting at ", start_price)
        for bidder in self._bidders:
            auctioneer.register_bidder(bidder)
        auctioneer.accept_bid(start_price, "Starting Bid")

        print("\nTHe winner of the auction is:", auctioneer.get_highest_bidder(), "at", auctioneer.get_highest_bid(),
              "\n")

        bidder_dict = {bidder: bidder.highest_bid for bidder in self._bidders}
        for bidder, highest_bid in bidder_dict.items():
            print("Bidder", bidder, "Highest Bid:", highest_bid)


def main():
    list_of_bidders = []

    item = input("Enter item to auction: ")
    starting_price = get_valid_user_input_for_specified_type("Enter the starting price: ", float)
    hard_coded_or_manual_bidders = get_valid_user_input_for_specified_type("Enter 1 for hardcoded users\n "
                                                                           "Enter 2 for custom users\n", int)
    if hard_coded_or_manual_bidders == 1:
        list_of_bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
        list_of_bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
        list_of_bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
        list_of_bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
        list_of_bidders.append(Bidder("Scott", 4000, random.random(), 2))
    else:
        num_bidders = get_valid_user_input_for_specified_type("Enter the number of bidders: ", int)

        while list_of_bidders.__len__() != num_bidders:
            name = input("Enter bidder name:")
            budget = get_valid_user_input_for_specified_type("Enter the budget: ", float)
            bid_increase_perc = get_valid_user_input_for_specified_type("Enter bid percentage increase in decimal "
                                                                        "form: ", float)
            bid_chance = 1
            while bid_chance >= 1:
                bid_chance = get_valid_user_input_for_specified_type("Enter chance, a decimal between 0 and 1 "
                                                                     "exclusive: ", float)
            list_of_bidders.append(Bidder(name, budget,bid_chance, bid_increase_perc))

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(list_of_bidders)
    my_auction.simulate_auction(item, starting_price)


if __name__ == '__main__':
    main()
