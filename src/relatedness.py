def relatedness_score(profile1, profile2):

    matches = 0

    for a, b in zip(profile1, profile2):

        if a == b:
            matches += 1

    return matches / len(profile1)