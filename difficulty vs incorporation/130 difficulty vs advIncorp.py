import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("qualitative.csv")
seq = 1
prec = 3
rev = 0
data = data[(data['con.sequence'] == seq) & (data['con.precise'] == prec) & (data['con.reveal'] == rev)]

f1a = data[(data["difficulty"] == "Extremely easy") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1b = data[(data["difficulty"] == "Moderately easy") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1c = data[(data["difficulty"] == "Slightly easy") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1e = data[(data["difficulty"] == "Slightly difficult") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1f = data[(data["difficulty"] == "Moderately difficult") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]
f1g = data[(data["difficulty"] == "Extremely difficult") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")].shape[0]

f2a = data[(data["difficulty"] == "Extremely easy") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2b = data[(data["difficulty"] == "Moderately easy") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2c = data[(data["difficulty"] == "Slightly easy") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2e = data[(data["difficulty"] == "Slightly difficult") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2f = data[(data["difficulty"] == "Moderately difficult") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]
f2g = data[(data["difficulty"] == "Extremely difficult") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")].shape[0]

f3a = data[(data["difficulty"] == "Extremely easy") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3b = data[(data["difficulty"] == "Moderately easy") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3c = data[(data["difficulty"] == "Slightly easy") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3e = data[(data["difficulty"] == "Slightly difficult") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3f = data[(data["difficulty"] == "Moderately difficult") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]
f3g = data[(data["difficulty"] == "Extremely difficult") & (data["adviceIncorporate"] == "Always followed the AI advice closely")].shape[0]


d1 = {
    "f1a": f1a,
    "f1b": f1b,
    "f1c": f1c,
    "f1d": f1d,
    "f1e": f1e,
    "f1f": f1f,
    "f1g": f1g
}

d2 = {
    "f2a": f2a,
    "f2b": f2b,
    "f2c": f2c,
    "f2d": f2d,
    "f2e": f2e,
    "f2f": f2f,
    "f2g": f2g
}

d3 = {
    "f3a": f3a,
    "f3b": f3b,
    "f3c": f3c,
    "f3d": f3d,
    "f3e": f3e,
    "f3f": f3f,
    "f3g": f3g
}



keys1 = list(d1.keys())
keys2 = list(d2.keys())
keys3 = list(d3.keys())

keys = list(["Extremely easy", "\nModerately easy", "Slightly easy", "\n\nNeither easy nor difficult", "Slightly difficult", "\nModerately difficult", "Extremely difficult"])

vals1 = np.array(list(d1.values()))
vals2 = np.array(list(d2.values()))
vals3 = np.array(list(d3.values()))

print(vals1)
print(vals2)
print(vals3)


plt.bar(keys, vals1, color = "green", label = "Did not follow the advice at all or only rarely", alpha = 1)
plt.bar(keys, vals2, bottom = vals1, color = "green", label = "Generally followed the advice but deviated sometimes when I thought I had a better strategy", alpha = 0.66)
base = vals1
plt.bar(keys, vals3, bottom = base + vals2, color = "green", label = "Always followed the AI advice closely", alpha = 0.33)
plt.title("difficulty vs adviceIncorporate" + "\n" + f"sequence: {seq}  precise: {prec}  reveal: {rev}")
plt.xlabel("difficulty")
plt.ylabel("adviceIncorporation counts")
plt.tight_layout()

plt.show()