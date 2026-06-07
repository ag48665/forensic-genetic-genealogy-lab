
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/ibd_results.csv")

means = {
    "Parent-child": df["parent_child"].mean(),
    "Unrelated": df["unrelated"].mean()
}

plt.figure(figsize=(8, 5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Average SNP similarity")
plt.title("SNP-based relatedness comparison")

plt.tight_layout()

plt.savefig(
    "reports/ibd_experiment.png",
    dpi=300
)

print("Plot saved.")