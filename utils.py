import random


def rand_unique_ints(
        n:int, range_min:int, range_max:int,
        insert_val:int=None, rand_insert_loc:bool=False,
        random_seed:int=None
    ) -> list[int]:
    """
    Generate a list of random unique integers in a given range.

    Args:
        n (int): Size of the output.
        range_min (int): Smallest possible random value in output (inclusive).
        range_max (int): Largest possible random value in output (exclusive).
        insert_val (int, optional): If not none, place inject into output.
        rand_insert_loc (bool): If true, place insert_val into random location
            in output list. Otherwise (default), place at middle index. This
            way, if used to create a FullNode, its data and location values will
            be the same integer.
        random_seed (int, optional): If not None, use specific seed to generate
            random integers. Otherwise (default), use the random library's
            default.

    Raises:
        InvalidRandUniqueIntGenerationInput: If input is invalid - ie n is less
            than zero or the difference between range_min and range_max is less
            than n.

    Returns:
        list[int]: list of n unique integers, each greater than or equal to
            range_min and less than range_max.  """
    
    if range_max - range_min < n or n <= 0 or range_min < 0 or range_max < 0:
        raise InvalidRandUniqueIntGenerationInput(range_min, range_max, n)
    
    if random_seed is not None:
        random.seed(random_seed)
    
    ret = random.sample(range(range_min, range_max), n)
    
    
    if insert_val and rand_insert_loc:
        ret[len(ret) // 2] = insert_val
    
    random.shuffle(ret)
    
    if insert_val and not rand_insert_loc:
        ret[len(ret) // 2] = insert_val
    
    return ret