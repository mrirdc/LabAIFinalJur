from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
iris=load_iris()

x=iris.data
y=iris.target

#1

print("Forma setului de date:", x.shape)

print("\nDenumirile atributelor:")
print(iris.feature_names)

print("nClasele:")
print(iris.target_names)

#2
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print(x)
print(y)

#3
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Înainte de scalare:")
print(X_train[:3])

print("\nDupă scalare:")
print(X_train_scaled[:3])

# 4.1
knn = KNeighborsClassifier(n_neighbors=3)

# 4.2
knn.fit(X_train_scaled, y_train)

# 4.3
acuratete = knn.score(X_test_scaled, y_test)
print("Acuratețea modelului KNN (k=3):", acuratete)



# 5.1 -
acurateti = []

for k in range(1, 16):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    acurateti.append(model.score(X_test_scaled, y_test))

# 5.2
plt.plot(range(1, 16), acurateti, marker='o')
plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratețe")
plt.title("Acuratețea KNN în funcție de k")
plt.xticks(range(1, 16))
plt.grid(True)
plt.show()

# 5.3
k_optim = acurateti.index(max(acurateti)) + 1
print(f"Valoarea optimă a lui k este: {k_optim} cu acuratețea: {max(acurateti)}")



# 6
y_pred = knn.predict(X_test_scaled)

# 6.1 - Matricea de confuzie
print("Matricea de confuzie:")
print(confusion_matrix(y_test, y_pred))

# 6.2 - Raport complet de clasificare
print("\nRaport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

#7.1.
plt.scatter(x[y==0, 2], x[y==0, 3], color='red', label='Setosa')
plt.scatter(x[y==1, 2], x[y==1, 3], color='blue', label='Versicolor')
plt.scatter(x[y==2, 2], x[y==2, 3], color='green', label='Virginicaa')
plt.xlabel("Lungime petală")
plt.ylabel("Lățime petală")
plt.title("Scatter plot în funcție de clasă")
plt.legend()
plt.show()

#7.2
print("Introduceți caracteristicile florii noi:")
sepal_length = float(input("Lungime sepală: "))
sepal_width = float(input("Lățime sepală: "))
petal_length = float(input("Lungime petală: "))
petal_width = float(input("Lățime petală: "))

floare_noua = [[sepal_length, sepal_width, petal_length, petal_width]]
floare_noua_scaled = scaler.transform(floare_noua)
predictie = knn.predict(floare_noua_scaled)
print("Floarea este:", iris.target_names[predictie[0]])