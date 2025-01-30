def validate_ean(code):
    """
    Validate the checksum of an EAN-13 code.

    This function takes a string representation of an EAN-13 code and verifies
    if the checksum is correct. The checksum is the last digit of the code and
    is calculated using a specific algorithm.

    Args:
    code (str): A string representing the EAN-13 code to be validated.

    Returns:
    bool: True if the checksum is valid, False otherwise.

    Raises:
    ValueError: If the input is not a string of exactly 13 digits.

    Example:
    >>> validate_ean("9780201310054")
    True
    >>> validate_ean("9780201310053")
    False
    """
    if not isinstance(code, str) or len(code) != 13 or not code.isdigit():
        raise ValueError("Input must be a string of exactly 13 digits.")

    digits = [int(d) for d in code]
    checksum = digits[-1]
    
    weighted_sum = sum(d * (3 if i % 2 else 1) for i, d in enumerate(digits[:-1]))
    calculated_checksum = (10 - (weighted_sum % 10)) % 10
    
    return checksum == calculated_checksum
