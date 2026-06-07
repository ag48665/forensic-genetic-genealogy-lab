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

    sibling1 = generate_child(
        parent1,
        parent2
    )

    sibling2 = generate_child(
        parent1,
        parent2
    )

    unrelated = generate_profile()

    sibling_score = relatedness_score(
        sibling1,
        sibling2
    )

    unrelated_score = relatedness_score(
        sibling1,
        unrelated
    )

    results.append({
        "siblings": sibling_score,
        "unrelated": unrelated_score
    })

df = pd.DataFrame(results)

print(
    "Average sibling similarity:",
    df["siblings"].mean()
)

print(
    "Average unrelated similarity:",
    df["unrelated"].mean()
)

df.to_csv(
    "reports/sibling_ibd_results.csv",
    index=False
)