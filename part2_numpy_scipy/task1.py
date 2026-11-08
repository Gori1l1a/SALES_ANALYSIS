import numpy as np

expenses=np.array([3200 ,3100 ,2600 ,1900 ,1500 ,1300 ,1250 ,1400 ,1800 ,2300 ,2900 ,350])
print(expenses)
winter_sum=np.sum(expenses[[1,0,1]])
summer_sum=np.sum(expenses[5:8])
print(winter_sum)
print(summer_sum)

if winter_sum > summer_sum:
    print("больше тратится зимой")
elif summer_sum > winter_sum:
    print("больше тратится летом")
else:
    print("расходы равны")
    
max_value=np.max(expenses)
max_month=np.where(expenses==max_value)[0]+1

print(f"Максимум ({max_value}) в месяцах: {max_month[0]}")