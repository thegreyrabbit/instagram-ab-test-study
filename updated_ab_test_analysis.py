
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv('ab_test_data.csv')

# Recalculate engagement rate (if needed)
followers = 3200
data['Engagement_Rate'] = ((data['Likes'] + data['Comments']) / followers) * 100

# Summary statistics
summary = data.groupby('Photograph_Style').mean()[['Likes', 'Comments', 'Engagement_Rate', 'Impressions', 'Saves']]
print(summary)

# T-test
high_fashion_rates = data[data['Photograph_Style'] == 'High Fashion Style']['Engagement_Rate']
portrait_rates = data[data['Photograph_Style'] == 'Portrait Style']['Engagement_Rate']
t_stat, p_value = ttest_ind(high_fashion_rates, portrait_rates)
print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")

# Visualizations
# Likes and Comments Trends by Photograph Style
plt.figure(figsize=(8, 5))
for style in data["Photograph_Style"].unique():
    subset = data[data["Photograph_Style"] == style]
    plt.plot(subset["Post"], subset["Likes"], marker="o", label=f"{style} - Likes")
    plt.plot(subset["Post"], subset["Comments"], marker="x", label=f"{style} - Comments")

plt.title("Likes and Comments Trends by Photograph Style")
plt.ylabel("Count")
plt.xlabel("Posts")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("likes_comments_trends.png")
plt.show()

# Engagement Rate Distribution
plt.figure(figsize=(8, 5))
for style in data["Photograph_Style"].unique():
    subset = data[data["Photograph_Style"] == style]
    plt.hist(subset["Engagement_Rate"], alpha=0.5, bins=5, label=f"{style} Engagement Rate")

plt.title("Engagement Rate Distribution")
plt.ylabel("Frequency")
plt.xlabel("Engagement Rate (%)")
plt.legend()
plt.tight_layout()
plt.savefig("engagement_rate_distribution.png")
plt.show()

# Impressions vs Saves Scatter Plot
plt.figure(figsize=(8, 5))
for style in data["Photograph_Style"].unique():
    subset = data[data["Photograph_Style"] == style]
    plt.scatter(subset["Impressions"], subset["Saves"], label=style)

plt.title("Impressions vs Saves by Photograph Style")
plt.ylabel("Saves")
plt.xlabel("Impressions")
plt.legend()
plt.tight_layout()
plt.savefig("impressions_vs_saves.png")
plt.show()
