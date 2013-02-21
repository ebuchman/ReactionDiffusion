def fix_boundaries(systems, boundaries):
    for i in xrange(len(systems)):
        systems[i][0, :] = boundaries[i]
        systems[i][-1, :] = boundaries[i]
        systems[i][:, 0] = boundaries[i]
        systems[i][:, -1] = boundaries[i]
        
    return systems