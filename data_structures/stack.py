"""Stack implementation for undo functionality."""

class Stack:
    """
    A simple stack implementation using Python list.

    Operations:
        push(item)   -> Add item to top (O(1))
        pop()        -> Remove and return top item (O(1))
        peek()       -> View top item without removing (O(1))
        is_empty()   -> Check if stack is empty (O(1))
        size()       -> Get number of items (O(1))
        clear()      -> Remove all items (O(n))
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """
        Push an item onto the top of the stack.

        Args:
            item: Any Python object to store.

        Time Complexity: O(1)
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item, or None if stack is empty.

        Time Complexity: O(1)
        """
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top item, or None if stack is empty.

        Time Complexity: O(1)
        """
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.

        Time Complexity: O(1)
        """
        return len(self._items) == 0

    def size(self):
        """
        Get the number of items in the stack.

        Returns:
            int: Number of items.

        Time Complexity: O(1)
        """
        return len(self._items)

    def clear(self):
        """
        Remove all items from the stack.

        Time Complexity: O(n)
        """
        self._items = []

    def __str__(self):
        """
        String representation of the stack (top first).

        Returns:
            str: e.g., "Stack([action3, action2, action1])"
        """
        return f"Stack({self._items})"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        """Allow len(stack) syntax."""
        return self.size()

