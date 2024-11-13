import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("qualitative.csv")
seq = 1
prec = 2
rev = 0
data = data[(data['con.sequence'] == seq) & (data['con.precise'] == prec) & (data['con.reveal'] == rev)]

f1 = data[data["adviceIncorporate"] == "Did not follow the advice at all or only rarely"]
f2 = data[data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy"]
f3 = data[data["adviceIncorporate"] == "Always followed the AI advice closely"]


inco_average_dict = {
    "rarely followed": f1["total_bonus"].mean(),
    "generally followed": f2["total_bonus"].mean(), 
    "always followed": f3["total_bonus"].mean()
}

incokeys = list(inco_average_dict.keys())
incovalues = list(inco_average_dict.values())

plt.bar(incokeys, incovalues)
plt.title("adviceIncorporate vs total_bonus" + "\n" + f"sequence: {seq}  precise: {prec}  reveal: {rev}")
plt.xlabel("adviceIncorporate")
plt.ylabel("average total_bonus")
plt.tight_layout()

plt.show()