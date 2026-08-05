from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Create a Fibonacci function with memorization.

    Returns
    -------
    Callable[[int], int]
        A function that computes Fibonacci numbers using recursion
        and caching.
    """
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Return the n-th Fibonacci number.

        Parameters
        ----------
        n: int
            Index of the Fibonacci number.

        Returns
        -------
        int
            The n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Return the cached value if it has already been computed.
        if n in cache:
            return cache[n]

        # Compute and cache the result for future calls.
        cache[n] = fibonacci(n - 1) + fibonacci (n - 2)
        return cache[n]
    
    return fibonacci
