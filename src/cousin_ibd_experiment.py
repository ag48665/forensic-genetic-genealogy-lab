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

    grandparent1 = generate_profile()
    grandparent2 = generate_profile()

    grandparent3 = generate_profile()
    grandparent4 = generate_profile()

    parent_a = generate_child(
        grandparent1,
        grandparent2
    )

    parent_b = generate_child(
        grandparent1,
        grandparent2
    )

    spouse_a = generate_profile()
    spouse_b = generate_profile()

    cousin1 = generate_child(
        parent_a,
        spouse_a
    )

    cousin2 = generate_child(
        parent_b,
        spouse_b
    )

    unrelated = generate_profile()

    cousin_score = relatedness_score(
        cousin1,
        cousin2
    )

    unrelated_score = relatedness_score(
        cousin1,
        unrelated
    )

    results.append({
        "cousins": cousin_score,
        "unrelated": unrelated_score
    })

df = pd.DataFrame(results)

print(
    "Average cousin similarity:",
    df["cousins"].mean()
)

print(
    "Average unrelated similarity:",
    df["unrelated"].mean()
)

df.to_csv(
    "reports/cousin_ibd_results.csv",
    index=False
)