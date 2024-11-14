
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

# Visualize engagement rate
plt.figure(figsize=(8, 5))
summary['Engagement_Rate'].plot(kind='bar', title='Engagement Rate Comparison (High Fashion vs Portrait Style)')
plt.ylabel('Engagement Rate (%)')
plt.xlabel('Photograph Style')
plt.tight_layout()
plt.savefig('engagement_rate_comparison.png')  # Save the chart as an image
plt.show()
