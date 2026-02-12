# %%
import pandas as pd

# %%
s = pd.Series([1, 10e1, 10e2, 10e3, 10e4])
s

# %%
d = pd.DataFrame(
    {
        "col1": range(100),
        "col2": [i * 2 for i in range(100)],
        "col3": [i**2 for i in range(100)],
    }
)
d

# %%
d.head()

# %%
d.tail()

# %%
d.head(10)

#%%
list(d.columns)

# %%
d.tail(2)

# %%
d.columns

# %%
d.index

# %%
d["col1"]

# %%
d[["col1", "col3"]]

#%%
l = [1,2,3,23,355,643]
l[:3]
#l[starting index(inclusive):ending index(exclusive)]
#starting index where i want to select
#ending index - starting index: size of the selection


# %%
d[13:27]

# %%
d.iloc[55]

# %%
d.loc[55]

# %%
d.index = [f"a{i}" for i in range(100)]
d.loc["a33"]

# %%
d.loc[
    
    [f"a{i}" for i in [10, 20, 30, 40]], 
    
    ["col1", "col3"]

]

# %%
d.loc[:, ["col1", "col3"]]

# %%
d["col3"] < 400

# %%
d[ d["col3"] < 400 ]

# %%
d[ (d["col3"] < 400) & (d["col1"] > 3) ]


#and or not
# & | ~

# %%
d[(d["col3"] < 400) & (d["col1"] > 3)][["col2", "col1"]]

# %%
d[(d["col3"] > 400) | (d["col1"] < 3)]

# %%
d[~(d["col3"] < 400)]

# %%
import numpy as np

d.loc["a0", "col1"] = np.nan
d.loc["a1", "col2"] = np.nan
d.loc["a2", "col3"] = np.nan
d


# %%
duplicate_d = pd.DataFrame(d)
duplicate_d.dropna(inplace = True)
duplicate_d = duplicate_d.dropna()
duplicate_d
# %%
d.dropna()



# %%
d.fillna(-100)

# %%
d.isna()

# %%
d.max()

# %%
d.min()

# %%
d.count()

# %%
d.shape

# %%
d.isna().sum()

# %%
d.sum()

# %%
d.mean()

# %%
d.describe()

# %%
e = pd.DataFrame(d)
e
# %%
e["col4"]= "haha"
e["col5"] = ["a","b","c","d"] * 25

e.describe(include="all")

# %%
d.mean(axis=1)


# %%
def func():
    return 1


# %%
def custom_mean(col):
    return 1+ col.sum() / col.count()


d.apply(custom_mean)

# %%
d.apply(lambda col: 1+col.sum() / col.count())

# %%
d.apply(lambda row: row["col1"] + row["col3"], axis=1)

# %%
a = d["col3"].astype(str)
a

# %%
a = a.str.rstrip(".0")
a.str.zfill(6)

# %%
s = pd.Series(np.random.randint(0, 7, size=100))
s

# %%
s.value_counts()

# %%
s.value_counts()[:3]

# %%
s.value_counts(ascending=True)[:3]

# %%
df = pd.DataFrame(
    {
        "col1": ["A", "A", "B", np.nan, "D", "C"],
        "col2": [2, 1, 9, 8, 7, 4],
        "col3": [0, 1, 9, 4, 2, 3],
    }
)
df

# %%
df.sort_values("col1")

# %%
df.sort_values(["col1"], na_position="first")

# %%
df.sort_values(by=["col1", "col2"])

# %%
df.sort_values(by=["col1", "col2"], ascending=False)

# %%
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": [
            "x",
            "x",
            "y",
            "z",
            "y",
            "y",
            "x",
            "z",
        ],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df

# %%
df.groupby("A").sum(numeric_only=True)

# %%
df.groupby("A").min(numeric_only=True)

# %%
df.groupby("A").apply(lambda d: d["C"].sum()+1)

# %%
df.groupby(["A", "B"]).sum()

# %%
for key, group_df in df.groupby("A"):
    print(f"{key}: {type(group_df)}")
    print(group_df)
    print()

# %%
df.to_csv("foo.csv")

# %%
df.to_csv("foo.csv", index=False)

# %%
pd.read_csv("foo.csv")

# %%
df.to_excel("foo.xlsx")

# %%
pd.read_excel("foo.xlsx")

# %%
df.to_pickle("foo.pkl")

# %%
pd.read_pickle("foo.pkl")

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%
tips = sns.load_dataset("tips")
tips

# %%
ax = sns.scatterplot(
    x="total_bill", 
    y="tip", 
    data=tips
)

# %%
sns.scatterplot(
    x=tips["total_bill"], 
    y=tips["tip"]
)

# %%
ax = sns.scatterplot(
    x="total_bill", 
    y="tip", 
    hue="time", 
    data=tips
)
plt.title("Some Title")
plt.xlabel("Some xaxis label")
plt.ylabel("Some yaxis label")

# %%
ax = sns.scatterplot(
    x="total_bill", y="tip", hue="time", data=tips
)
ax.set(
    title="Some Title", 
    xlabel="xlabel", 
    ylabel="ylabel")


# %%
ax = sns.scatterplot(
    x="total_bill", 
    y="tip", 
    hue="time", 
    size="size", 
    data=tips
)
plt.title("Fancy Chart")
plt.xlabel("Total Bill")
plt.ylabel("$ Tips")

# %%
ax = sns.barplot(
    x="day", y="total_bill", data=tips
)

# %%
ax = sns.barplot(
    x="day", 
    y="total_bill", 
    data=tips.groupby("day").mean(numeric_only=True).reset_index()
)



# %%
fmri = sns.load_dataset("fmri")
ax = sns.lineplot(
    x="timepoint", 
    y="signal", hue="event", 
    data=fmri)

# %%
titanic = sns.load_dataset("titanic")
titanic
# %%
ax = sns.countplot(y="class", data=titanic)

# %%
ax = sns.countplot(x="class", data=titanic)

# %%
ax = sns.countplot(
    y="class", hue="who", 
    data=titanic)

# %%
import numpy as np

x = np.random.randn(100)
ax = sns.displot(x)

# %%
ax = sns.displot(data=fmri, x="signal",bins=10)

# %%
ax = sns.histplot(data=fmri, x="signal")


# %%
exercise = sns.load_dataset("exercise")
ax = sns.catplot(
    x="time", y="pulse", hue="kind", col="diet", data=exercise
)

# %%
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [
    ["Milk", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
    ["Dill", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
    ["Milk", "Apple", "Kidney Beans", "Eggs"],
    ["Milk", "Unicorn", "Corn", "Kidney Beans", "Yogurt"],
    ["Corn", "Onion", "Onion", "Kidney Beans", "Ice cream", "Eggs"],
]

# %%
te = TransactionEncoder()
te.fit(dataset)
te_ary = te.transform(dataset)
te_ary

# %%
import pandas as pd
df = pd.DataFrame(te_ary, columns=te.columns_)
df


# %%
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets

# %%
from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, min_threshold=0.1)
rules

# %%
import seaborn as sns
ax = sns.scatterplot(
    x="support", y="confidence", alpha=0.5, data=rules)

# %%
length = frequent_itemsets["itemsets"].apply(len)
frequent_itemsets["length"] = length
frequent_itemsets

# %%
frequent_itemsets["zero"] = 9
frequent_itemsets

# %%
frequent_itemsets["zero"] = [9] * frequent_itemsets.shape[0]
frequent_itemsets

# %%
rules.sort_values("confidence", ascending=False).head(3)

# %%
