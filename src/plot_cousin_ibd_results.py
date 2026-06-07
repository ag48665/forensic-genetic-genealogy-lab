import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/cousin_ibd_results.csv")

means = {
    "First cousins": df["cousins"].mean(),
    "Unrelated": df["unrelated"].mean()
}

plt.figure(figsize=(8, 5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Average SNP similarity")
plt.title("First Cousin vs Unrelated SNP Similarity")

plt.tight_layout()

plt.savefig(
    "reports/cousin_ibd_experiment.png",
    dpi=300
)

print("Plot saved.")