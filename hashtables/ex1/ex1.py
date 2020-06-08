def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    answer = []

    for weight in weights:
        # store each weight in the input list as keys
        key = weight
        cache[key] = weights.index(weight) # Note: If index isnt found we'll return an error so I might need to fix this as I did in line 25 of ex.5
        
        # see if the hash table contains an entry[key] for `limit - weight`
        if limit - weight == key:
            # return indices of weights. 
            answer.extend([weights.index(weight), weights.index(key)]) # now do largest to smallest

    answer.sort()
    print(answer)
    return tuple(answer)


'''
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]
since these are the indices of weights 15 and 6 whose sum equals 21

* If we store each weight's list index as its value, we can then check
  to see if the hash table contains an entry for `limit - weight`. If it
  does, then we've found the two items whose weights sum up to the
  `limit`!
'''