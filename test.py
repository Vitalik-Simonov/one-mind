import pandas as pd

from ml import predict


df = pd.DataFrame([
[1, 1, 1],
[2, 2, 1],
[1, 1, 1],
[1, 2, 2],
[1, 3, 3],
[3, 3, 1],
[1, 1, 1]
])
df['fio'] = [str(i) for i in range(7)]
print(df)

print(predict(df))