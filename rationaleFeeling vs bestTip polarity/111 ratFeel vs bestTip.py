import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

seq = 1
prec = 1
rev = 1

file_path = f"rationaleFeeling vs bestTip polarity\sent.csv"
df = pd.read_csv(file_path)
df = df[(df['con.sequence'] == seq) & (df['con.precise'] == prec) & (df['con.reveal'] == rev)]

# clean msising
df_cleaned = df.dropna(subset=["sentiment_polarity"])

groups_cleaned = [group['sentiment_polarity'].values for name, group in df_cleaned.groupby("rationaleFeeling")]

anova_result_cleaned = stats.f_oneway(*groups_cleaned)

print("F-statistic:", anova_result_cleaned.statistic)
print("p-value:", anova_result_cleaned.pvalue)

plt.figure(figsize=(10, 6))
sns.boxplot(data = df_cleaned, x = "rationaleFeeling", y = "sentiment_polarity")

plt.title("rationaleFeeling vs bestTip polarity" + "\n" + f"sequence: {seq}  precise: {prec}  reveal: {rev}")
plt.xlabel("rationaleFeeling")
plt.ylabel("tip sentiment polarity")
plt.xticks(rotation = 10)

plt.show()