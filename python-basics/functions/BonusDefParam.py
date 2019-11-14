def grow(data=[]):
    data.append('?')
    return data


print(grow())
print(grow())
print(grow())


def grow_workaroun(data=None):
    if data is None:
        data = []
    data.append('?')
    return data


print(grow_workaroun())
print(grow_workaroun())
print(grow_workaroun())
