import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Yield all floating-point numbers in the input text.

    Parameters
    ----------
    text: str
        Input text containing numbers separated by spaces.

    Yields
    ------
    float
        Next number extracted from the text.
    """
    pattern = r"\d+\.\d+"

    # Yield each number found in the text.
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(
    text: str,
    func: Callable[[str], Generator[float, None, None]],
) -> float:
    """
    Calculate the total sum pf numbers extracted from the input text.

    Parameters
    ----------
    text: str
        Input text containing numbers.
    func: Callable[[str], Generator[float, None, None]]
        Generator function that yields numbers from the text.

    Returns
    -------
    float
        Sum of all extracted numbers.
    """
    return sum(func(text))
