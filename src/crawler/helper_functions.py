def get_degree_type(argument):
    types = {
        0: 'Undergraduate',
        1: 'Masters',
        2: 'Research',
    }

    return types.get(argument)
