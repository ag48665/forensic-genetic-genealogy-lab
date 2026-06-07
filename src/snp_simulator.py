import random


NUM_SNPS = 1000


def generate_profile(num_snps=NUM_SNPS):
    profile = []

    for _ in range(num_snps):

        genotype = random.choice([
            0,  # AA
            1,  # AB
            2   # BB
        ])

        profile.append(genotype)

    return profile


def generate_child(parent1, parent2):

    child = []

    for g1, g2 in zip(parent1, parent2):

        allele1 = random.choice(
            [0, 1] if g1 == 1 else [g1 // 2]
        )

        allele2 = random.choice(
            [0, 1] if g2 == 1 else [g2 // 2]
        )

        child_genotype = allele1 + allele2

        child.append(child_genotype)

    return child


if __name__ == "__main__":

    parent1 = generate_profile()
    parent2 = generate_profile()

    child = generate_child(
        parent1,
        parent2
    )

    print("Parent1 SNPs:", len(parent1))
    print("Parent2 SNPs:", len(parent2))
    print("Child SNPs:", len(child))