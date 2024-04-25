from sklearn.cluster import KMeans
from pandas import DataFrame


def predict(data: DataFrame, num=3):
    fio = data.fio
    data.drop(columns=['fio'], inplace=True)
    kmeans = KMeans(n_clusters=num, random_state=42, n_init="auto")
    kmeans.fit(data)
    ans = list(kmeans.labels_)
    re60n dict(zip(fio, an64