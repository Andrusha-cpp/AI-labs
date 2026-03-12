import pandas as pd
from faker import Faker

fake = Faker('en_US')
df = pd.read_csv("train.csv")
print(df.head())

empval = df.isnull() #*смотрим и подсчитываем пустые значения
print(f"Amount of empty values before:\n{empval.sum()}\n")

#*Находим моду и среднее значения 
HomePlanet_mode = df['HomePlanet'].mode()[0]
CryoSleep_mode = df['CryoSleep'].mode()[0]
Cabin_mode = df['Cabin'].mode()[0]
Destination_mode = df['Destination'].mode()[0]
Age_mean = df['Age'].mean()
VIP_mode = df['CryoSleep'].mode()[0]
RoomService_mean = df['RoomService'].mean()
FoodCourt_mean = df['FoodCourt'].mean()
ShoppingMall_mean = df['ShoppingMall'].mean()
Spa_mean = df['Spa'].mean()
VRDeck_mean = df['VRDeck'].mean()

#*Подсчет и генерация имен
empnames = df['Name'].isnull()
empnames_amount = empnames.sum()

#*Заполняем пустые строки
df['HomePlanet'] = df['HomePlanet'].fillna(HomePlanet_mode)
df['CryoSleep'] = df['CryoSleep'].fillna(CryoSleep_mode)
df['Cabin'] = df['Cabin'].fillna(Cabin_mode)
df['Destination'] = df['Destination'].fillna(Destination_mode)
df['Age'] = df['Age'].fillna(Age_mean)
df['VIP'] = df['VIP'].fillna(VIP_mode)
df['RoomService'] = df['RoomService'].fillna(RoomService_mean)
df['FoodCourt'] = df['FoodCourt'].fillna(FoodCourt_mean)
df['ShoppingMall'] = df['ShoppingMall'].fillna(ShoppingMall_mean)
df['Spa'] = df['Spa'].fillna(Spa_mean)
df['VRDeck'] = df['VRDeck'].fillna(VRDeck_mean)

#* Заполняем имена
df.loc[empnames, 'Name'] = [fake.name() for _ in range(empnames_amount)]

empval = df.isnull() #*смотрим и подсчитываем пустые значения
print(f"Amount of empty values after:\n{empval.sum()}\n")

