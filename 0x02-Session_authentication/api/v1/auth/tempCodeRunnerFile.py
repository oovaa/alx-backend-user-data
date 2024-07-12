        if path[-1] == '/':
            path = path[:-1]
        for i, p in enumerate(excluded_paths):
            if p[-1] == '/':
                excluded_paths[i] = p[:-1]
