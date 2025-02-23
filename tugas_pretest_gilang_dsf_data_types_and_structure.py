# -*- coding: utf-8 -*-
"""TUGAS_PRETEST_GILANG_DSF - Data Types and Structure.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pYA1iYq1ON2nKRs_UuGAm5DeiaMTceOk

# **1. Import Library**
"""

import pandas as pd
from sklearn import datasets

"""# **2. Read Dataset**"""

# Memuat dataset IRIS dari scikit-learn
gilang_tes = datasets.load_iris()

X = gilang_tes.data    # inputan untuk machine learning
y = gilang_tes.target  # output yang dinginkan dari machine learning

# Mengonversi data fitur dan target menjadi DataFrame
df_X = pd.DataFrame(X, columns=gilang_tes.feature_names)
df_y = pd.Series(y, name='target')

df_X

df_y

# Gabungkan fitur dan target dalam satu DataFrame
df = pd.concat([df_X, df_y], axis=1)

df.head(100)

df.info()

df['target'].unique()

df.describe()

"""# **3. Split Data**"""

from sklearn.model_selection import train_test_split

# Membagi data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)

"""# **4. Train the Model**

**- Menggunakan 4 Model Machine Learning Logistic Regression, Decision Tree, Random Forest Dan Naive Bayes**
"""

# Inisialisasi model
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import mpl_toolkits.mplot3d

from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

nb_model = GaussianNB()
lr_model = LogisticRegression(max_iter=200)
dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier(n_estimators=100)

"""# **5. VISUALISASI**"""

gilang_tes = datasets.load_iris()

_, ax = plt.subplots()
scatter = ax.scatter(gilang_tes.data[:, 0], gilang_tes.data[:, 1], c=gilang_tes.target)
ax.set(xlabel=gilang_tes.feature_names[0], ylabel=gilang_tes.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], gilang_tes.target_names, loc="lower right", title="Classes"
)

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(gilang_tes.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=gilang_tes.target,
    s=40,
)

ax.set_title("First three PCA dimensions")
ax.set_xlabel("1st Eigenvector")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2nd Eigenvector")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3rd Eigenvector")
ax.zaxis.set_ticklabels([])

plt.show()

X = gilang_tes.data
y = gilang_tes.target
target_names = gilang_tes.target_names

# Apply PCA
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit_transform(X, y)

# Explained variance ratio
print("Explained variance ratio (first two components):", pca.explained_variance_ratio_)

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
colors = ["navy", "turquoise", "darkorange"]
lw = 2

# Plot PCA result on the left
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    axes[0].scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)
axes[0].legend(loc="best", shadow=False, scatterpoints=1)
axes[0].set_title("PCA of IRIS dataset")

# Plot LDA result on the right
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    axes[1].scatter(X_r2[y == i, 0], X_r2[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)
axes[1].legend(loc="best", shadow=False, scatterpoints=1)
axes[1].set_title("LDA of IRIS dataset")

plt.show()

ax = plt.axes()

im = ax.imshow(np.corrcoef(X.T), cmap="RdBu_r", vmin=-1, vmax=1)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(list(gilang_tes.feature_names), rotation=90)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(list(gilang_tes.feature_names))

plt.colorbar(im).ax.set_ylabel("$r$", rotation=0)
ax.set_title("Iris feature correlation matrix")
plt.tight_layout()

n_comps = 2

methods = [
    ("PCA", PCA()),
    ("Unrotated FA", FactorAnalysis()),
    ("Varimax FA", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(8, 5), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    # The user was trying to call a method 'arange' on the Bunch object, but should be using np.arange instead.
    ax.set_yticks(np.arange(len(gilang_tes.feature_names)))
    ax.set_yticklabels(gilang_tes.feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("Factors")
plt.tight_layout()
plt.show()

"""#**6. Predict & Evaluate**

- Membuat Model Naive Bayes
"""

nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
accuracy_nb = accuracy_score(y_test, y_pred_nb)

print("\nModel: Naive Bayes")
print(f"Akurasi: {accuracy_nb * 100:.2f}%")

cm_nb = confusion_matrix(y_test, y_pred_nb)
plt.figure(figsize=(8, 5))
sns.heatmap(cm_nb, annot=True, fmt="d", cmap="Blues",
            xticklabels=gilang_tes.target_names, yticklabels=gilang_tes.target_names)
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.title("Confusion Matrix - Naive Bayes")
plt.show()

print("Laporan Klasifikasi: Naive Bayes")
print(classification_report(y_test, y_pred_nb, target_names=gilang_tes.target_names))

"""- Membuat Model Logistic Regression"""

lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
accuracy_lr = accuracy_score(y_test, y_pred_lr)

print("\nModel: Logistic Regression")
print(f"Akurasi: {accuracy_lr * 100:.2f}%")

cm_lr = confusion_matrix(y_test, y_pred_lr)
plt.figure(figsize=(8, 5))
sns.heatmap(cm_lr, annot=True, fmt="d", cmap="Blues",
            xticklabels=gilang_tes.target_names, yticklabels=gilang_tes.target_names)
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.title("Confusion Matrix - Logistic Regression")
plt.show()

print("Laporan Klasifikasi: Logistic Regression")
print(classification_report(y_test, y_pred_lr, target_names=gilang_tes.target_names))

"""- Membuat Model Random Forest"""

rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("\nModel: Random Forest")
print(f"Akurasi: {accuracy_rf * 100:.2f}%")

cm_rf = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(8, 5))
sns.heatmap(cm_rf, annot=True, fmt="d", cmap="Blues",
            xticklabels=gilang_tes.target_names, yticklabels=gilang_tes.target_names)
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.title("Confusion Matrix - Random Forest")
plt.show()

print("Laporan Klasifikasi: Random Forest")
print(classification_report(y_test, y_pred_rf, target_names=gilang_tes.target_names))

"""- Membuat Model DecisionTreeClassifier"""

dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("\nModel: DecisionTreeClassifier")
print(f"Akurasi: {accuracy_dt * 100:.2f}%")

cm_dt = confusion_matrix(y_test, y_pred_dt)
plt.figure(figsize=(8, 5))
sns.heatmap(cm_dt, annot=True, fmt="d", cmap="Blues",
            xticklabels=gilang_tes.target_names, yticklabels=gilang_tes.target_names)
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.title("Confusion Matrix - DecisionTreeClassifier")
plt.show()

print("Laporan Klasifikasi: DecisionTreeClassifier")
print(classification_report(y_test, y_pred_dt, target_names=gilang_tes.target_names))

"""- Dari 4 Algoritmya yang digunakan Naive bayes mencapai acurrasy di 97%, Random Forest 97% sedangkan ke 2 algoritma lainnya mencapai 100%"""