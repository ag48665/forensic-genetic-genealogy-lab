from snp_simulator import (
    generate_profile,
    generate_child
)

from relatedness import (
    relatedness_score
)

import pandas as pd


results = []

for _ in range(1000):

    parent1 = generate_profile()
    parent2 = generate_profile()

    child = generate_child(
        parent1,
        parent2
    )

    unrelated = generate_profile()

    parent_child_score = relatedness_score(
        parent1,
        child
    )

    unrelated_score = relatedness_score(
        unrelated,
        child
    )

    results.append({
        "parent_child": parent_child_score,
        "unrelated": unrelated_score
    })

df = pd.DataFrame(results)

print(
    "Average parent-child similarity:",
    df["parent_child"].mean()
)

print(
    "Average unrelated similarity:",
    df["unrelated"].mean()
)

df.to_csv(
    "reports/ibd_results.csv",
    index=False
)