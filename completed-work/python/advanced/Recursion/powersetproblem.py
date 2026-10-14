original_set=[1,2,4,6,7,10]

def makepowerset(set, powerset=[]):
    if not set:
        powerset.append([])
        return powerset
    
    first = set[0]
    rest = set[1:]
    
    # Recurse on the rest first
    makepowerset(rest, powerset)
    
    # For every existing subset, add a new version that includes `first`
    new_subsets = [subset + [first] for subset in powerset]
    powerset.extend(new_subsets)
    
    return powerset


       
    
print(makepowerset(original_set))