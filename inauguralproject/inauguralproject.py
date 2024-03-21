# create a demand function
# such that it can be used
import numpy as np

class demand:
    """
    The class function returns the demand function
    for each consumer.
    The fraction determines the alpha and beta of the
    consumer, while the good determines wether
    its good 1 or 2
    """

    def __init__(self, fraction, good):
        self.fraction = 1 - fraction if good == 2 else fraction
        self.good = good

    def function(self, good, price):
        """
        The function returns the demand for the chosen
        good in the first the defined class.
        Args:
            good: A list of integers representing the demand for the good
            defined initially
            price: A list of intergers representing the price for each
            good.

        Returns:
            The total demand for the good 1 or 2

        """
        # 1) coerce good and price
        # to numpy arrays
        good = np.array(good)
        price = np.array(price)

        demand = self.fraction * sum(price * good) / price[self.good - 1]

        return np.maximum(demand, 0)

def utility(fraction, good):
    good_1 = np.array(np.maximum(good[0], 0)) ** fraction
    good_2 = np.array(np.maximum(good[1], 0)) ** (1-fraction)

    return np.multiply(good_1, good_2)
