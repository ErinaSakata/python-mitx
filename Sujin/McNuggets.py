def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n < 0:
        return False
    elif n == 0:
        return True
    else: 
        return McNuggets(n - 6) or McNuggets(n - 9) or McNuggets(n - 20)
