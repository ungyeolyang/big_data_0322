import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')

print(df.info())
print(df.head())
print(df.describe())
print(f"결측치확인 {df.isnull().sum()}")

# 결측치 처리: Age의 결측치를 평균값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Embarked의 결측치를 최빈값으로 대체
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 새로운 열 추가: 가족 수(FamilySize)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
survival_rate = df['Survived'].mean()
print(f"생존률: {survival_rate * 100:.2f}%")

survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
print(f"성별에 따른 생존자 비율 {survival_rate_by_gender}")

survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()
print(f"클래스에 따른 생존자 비율 {survival_rate_by_class}")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 필요한 열 선택 및 더미 변수화
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# 특성과 타겟 변수 정의
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'Sex_male', 'Embarked_Q', 'Embarked_S']]
y = df['Survived']

# 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 로지스틱 회귀 모델 훈련
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 정확도와 분류 보고서 출력
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

