def get_degree_type(argument):
    types = {
        1: 'Undergraduate',
        2: 'Masters',
        3: 'Research',
    }

    return types.get(argument)
