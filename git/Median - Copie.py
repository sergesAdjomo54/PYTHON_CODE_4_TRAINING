def median(iterable):
    
    items = sorted(iterable)
    if len(items) == 0:
    	raise ValueError("L'argument de la fonction median() est une liste vide.")
    	
    median_index = (len(items) -1) //2
    
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index +1])/ 2.0
