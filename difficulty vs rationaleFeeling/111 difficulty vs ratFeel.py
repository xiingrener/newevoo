import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("qualitative.csv")
seq = 1
prec = 1
rev = 1
data = data[(data['con.sequence'] == seq) & (data['con.precise'] == prec) & (data['con.reveal'] == rev)]

f1a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]
f1g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Extremely negative")].shape[0]

f2a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]
f2g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Moderately negative")].shape[0]

f3a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]
f3g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Slightly negative")].shape[0]

f4a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]
f4g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Neither positive nor negative")].shape[0]

f5a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]
f5g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Slightly positive")].shape[0]

f6a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]
f6g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Moderately positive")].shape[0]

f7a = data[(data["difficulty"] == "Extremely easy") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7b = data[(data["difficulty"] == "Moderately easy") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7c = data[(data["difficulty"] == "Slightly easy") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7d = data[(data["difficulty"] == "Neither easy nor difficult") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7e = data[(data["difficulty"] == "Slightly difficult") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7f = data[(data["difficulty"] == "Moderately difficult") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]
f7g = data[(data["difficulty"] == "Extremely difficult") & (data["rationaleFeeling"] == "Extremely positive")].shape[0]


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

d4 = {
    "f4a": f4a,
    "f4b": f4b,
    "f4c": f4c,
    "f4d": f4d,
    "f4e": f4e,
    "f4f": f4f,
    "f4g": f4g
}

d5 = {
    "f5a": f5a,
    "f5b": f5b,
    "f5c": f5c,
    "f5d": f5d,
    "f5e": f5e,
    "f5f": f5f,
    "f5g": f5g
}

d6 = {
    "f6a": f6a,
    "f6b": f6b,
    "f6c": f6c,
    "f6d": f6d,
    "f6e": f6e,
    "f6f": f6f,
    "f6g": f6g
}

d7 = {
    "f7a": f7a,
    "f7b": f7b,
    "f7c": f7c,
    "f7d": f7d,
    "f7e": f7e,
    "f7f": f7f,
    "f7g": f7g
}


keys1 = list(d1.keys())
keys2 = list(d2.keys())
keys3 = list(d3.keys())
keys4 = list(d4.keys())
keys5 = list(d5.keys())
keys6 = list(d6.keys())
keys7 = list(d7.keys())
keys = list(["Extremely easy", "\nModerately easy", "Slightly easy", "\n\nNeither easy nor difficult", "Slightly difficult", "\nModerately difficult", "Extremely difficult"])

vals1 = np.array(list(d1.values()))
vals2 = np.array(list(d2.values()))
vals3 = np.array(list(d3.values()))
vals4 = np.array(list(d4.values()))
vals5 = np.array(list(d5.values()))
vals6 = np.array(list(d6.values()))
vals7 = np.array(list(d7.values()))
print(vals1)
print(vals2)
print(vals3)
print(vals4)
print(vals5)
print(vals6)
print(vals7)

plt.bar(keys, vals1, color = "green", label = "Extremely negative", alpha = 0.98)
plt.bar(keys, vals2, bottom = vals1, color = "green", label = "Moderately negative", alpha = 0.84)
base = vals1
plt.bar(keys, vals3, bottom = base + vals2, color = "green", label = "Slightly negative", alpha = 0.70)
base += vals2
plt.bar(keys, vals4, bottom = base + vals3, color = "green", label = "Neither positive nor negative", alpha = 0.56)
base += vals3
plt.bar(keys, vals5, bottom = base + vals4, color = "green", label = "Slightly positive", alpha = 0.42)
base += vals4
plt.bar(keys, vals6, bottom = base + vals5, color = "green", label = "Moderately positive", alpha = 0.28)
base += vals5
plt.bar(keys, vals7, bottom = base + vals6, color = "green", label = "Extremely positive", alpha = 0.14)
plt.title("difficulty vs rationaleFeeling" + "\n" + f"sequence: {seq}  precise: {prec}  reveal: {rev}")
plt.xlabel("difficulty")
plt.ylabel("rationaleFeeling")
plt.tight_layout()

plt.show()