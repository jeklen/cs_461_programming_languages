from functools import reduce as _reduce

__all__ = ['toposort', 'toposort_flatten']

def toposort(data):
    """Dependencies are expressed as a dictionary whose keys are items and whose values are a set of dependent items. Output is a list of set in topological order. Then first set consists of items with no dependences, each subsequent set consists of items that depend upon items in the preceeding sets
    """
    # Special case empty input
    if len(data) == 0:
        return

    # Copy the input so as to leave it unmodified
    data = data.copy()

    # Ignore self dependencies
    for k, v in data.items():
        v.discard(k)
    # Find all items that don't depend on anything
    extra_items_in_deps = _reduce(set.union, data.values()) - set(data.keys())
    # Add empty empty dependences where needed
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item, dep in data.items() if len(dep) == 0)
        if not ordered:
            break
        yield ordered
        data = {item: (dep - ordered)
                for item, dep in data.items()
                    if item not in ordered}
    if len(data) != 0:
        raise ValueError('Cyclic dependencies exist among these items:{}'.format(', '.join(repr(x) for x in data.items())))

def toposort_flatten(data, sort=True):
    """Returns a single list of dependencies. For any set returned by toposort(), those items are sorted and appended to the result (just to make the results deterministic)."""
    result = []
    for d in toposort(data):
        result.extend((sorted if sort else list)(d))
    return result

li = list(toposort({2: {11},
                    9: {11, 8, 10},
                    10: {11, 3},
                    11: {7, 5},
                    8: {7, 3},
                    }))
print(li)


