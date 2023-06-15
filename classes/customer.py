class Customer:
    """
    Represents a customer.

    Attributes:
        rewards_member (bool): Indicates whether the customer is a rewards member.
    """
    def __init__(self, rewards_member):
        """
        Initializes a Customer object with the specified rewards membership.

        Args:
            rewards_member (bool): Indicates whether the customer is a rewards member.
        """
        self._rewards_member = rewards_member

    def __str__(self):
        """
        Returns a string representation of the customer.

        Returns:
            str: A string representation of the customer.
        """
        return (
            f"Client is a rewards member"
            if self.rewards_member
            else f"Client is not a rewards member"
        )

    @property
    def rewards_member(self):
        """
        Gets the rewards membership status of the customer.

        Returns:
            bool: Indicates whether the customer is a rewards member.
        """
        return self._rewards_member

    @rewards_member.setter
    def rewards_member(self, value):
        """
        Sets the rewards membership status of the customer.

        Args:
            value (bool): Indicates whether the customer is a rewards member.
        """
        self._rewards_member = value

    @rewards_member.deleter
    def rewards_member(self):
        """
        Deletes the rewards membership status of the customer.
        """
        del self._rewards_member
