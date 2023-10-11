# 실습 1 - 텐서플로우로 선형회귀 모델링
# 선형회귀모델을 만들고 ‘5’를 넣었을때 값을 예측해보세요.

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2,4,6,8,10])
y = np.array([20,24,37,40,50])

model = Sequential()

model.add(Dense(1, input_dim = 1, activation = 'linear'))  # 선형 회귀니까 활성화함수 linear

model.compile(loss = 'mse', optimizer = 'sgd', metrics = ['accuracy'])

model.summary()  # 내가 만든 모델 확인할 수 있음

model.fit(x, y, epochs = 10)  # fit 학습시키기, epochs 학습 반복 횟수

model.predict([5])  # 예측




# 실습 2

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([[2,0],[4,5],[6,3],[8,5],[10,7]])  # x값의 차원 : y값에 대응되는 x값의 개수
y = np.array([20,24,37,40,50])

model = Sequential()

model.add(Dense(1, input_dim = 2, activation = 'linear')) # Dense(입력층 노드 개수, 인풋 데이터 차원, 활성화함수)

model.compile(loss = 'mse', optimizer = 'sgd', metrics = ['accuracy'])

model.fit(x, y, epochs = 10)

model.predict([[5, 7]])



# 실습 3 - 텐서플로우로 로지스틱회귀 모델링
# 로지스틱회귀 : 출력값이 0 아니면 1인 회귀, 분류모델용

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2,4,6,8,10])
y = np.array([0,0,0,1,1])

model2 = Sequential()

model2.add(Dense(1, input_dim = 1, activation = 'sigmoid'))

model2.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
# binary_crossentropy 이항분류때 사용하는 손실함수

model2.fit(x, y, epochs = 50)

model2.predict([9])





# 실습4(붓꽃 데이터)
# 붓꽃 종을 예측하는 base line 모델을 먼저 만들고, 성능(acc 90%이상)향상 모델을 만들어보세요

# 데이터 불러오기
import seaborn as sns
iris = sns.load_dataset('iris')

# 무슨 종이 있는지 확인
iris.groupby('species').mean()

# 붓꽃 종 원핫인코딩
def check(species):
  if species == 'setosa':
    return [1, 0, 0]
  elif species == 'versicolor' :
    return [0, 1, 0]
  elif species == 'virginica' :
    return [0, 0, 1]
  
# x값 y값 정의
import numpy as np
iris_feature = iris.drop(labels = 'species', axis = 1)
iris_class = list(map(check, iris['species']))
iris_class = np.array(iris_class)

# 훈련데이터 학습데이터 랜덤 분할
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    iris_feature, iris_class, random_state=42)

# 모델 쌓기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model3 = Sequential()

model3.add(Dense(32, input_dim = 4, activation = 'relu'))
model3.add(Dense(3, activation = 'softmax'))

model3.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
# 손실함수 : 원핫인코딩으로 다항분류할때 씀

model3.summary()

# 모델 학습
model3.fit(train_input, train_target, epochs = 100, verbose = 1)

# 모델 예측
predict_result = model3.predict([[7.1,	3.0,	5.9,	2.1]])
print('setosa, versicolor, virginica :', predict_result)

# 모델 평가
results = model3.evaluate(test_input, test_target)
print('loss, acc :', results)
