import argparse
import sys
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class InvalidConfigError(Exception):
    pass

def generate_data(seed, years, stores, out_path):
    np.random.seed(seed)
    start_date=datetime(2023, 1, 1)
    days=365*years

    cities=['Минск', 'Гомель', 'Брест', 'Витебск', 'Гродно']
    categories=['Электроника', 'Одежда', 'Продукты']
    products={
        'Электроника': ['Смартфон', 'Ноутбук', 'Наушники'],
        'Одежда': ['Футболка', 'Джинсы', 'Куртка'],
        'Продукты': ['Хлеб', 'Молоко', 'Сыр']
    }

    data=[]

    for day in range(days):
        current_date=start_date+timedelta(days=day)
        is_weekend=current_date.weekday()>=5
        
        if current_date.month in [12, 1, 2]:
            season=1.5
        elif current_date.month in [6, 7, 8]:
            season=0.7
        else:
            season=1.0

        for store_id in range(1, stores+1):
            city_index=(store_id-1)%len(cities)
            city=cities[city_index]

            for category in categories:
                for product in products[category]:
                    
                    qty=np.random.randint(5, 20)

                    if is_weekend:
                        qty=int(qty*1.3)
                    
                    qty=int(qty*season)

                    if category=='Электроника':
                        trend=1.0
                    elif category=='Одежда':
                        trend=0.5
                    else:
                        trend=-0.2
                        
                    years_passed=day/365.0
                    qty=int(qty*(1+trend*years_passed*0.1))

                    promo=0
                    price=np.random.uniform(100, 1000)
                    
                    if np.random.rand()<0.1:
                        promo=1
                        qty=int(qty*1.5)
                        price=price*0.9

                    if np.random.rand()<0.01:
                        qty=qty*10

                    cost=price*0.7
                    payment=np.random.choice(['наличные', 'карта', 'онлайн'])

                    if np.random.rand()<0.005:
                        payment=np.nan
                        
                    if np.random.rand()<0.005:
                        price=np.nan

                    data.append({
                        'date': current_date.strftime('%Y-%m-%d'),
                        'store_id': store_id,
                        'city': city,
                        'category': category,
                        'product': product,
                        'qty': qty,
                        'price': price,
                        'cost': cost,
                        'promo': promo,
                        'payment_method': payment
                    })

    df=pd.DataFrame(data)
    df.to_csv(out_path, index=False)
    print(f"Сгенерировано {len(df)} строк. Сохранено в {out_path}")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--years', type=int, default=1)
    parser.add_argument('--stores', type=int, default=5)
    parser.add_argument('--out', type=str, default='part3_synthetic_data/data/sales.csv')
    
    args=parser.parse_args()

    try:
        if args.years<=0:
            raise InvalidConfigError("Лет должно быть больше нуля")
        if args.stores<=0:
            raise InvalidConfigError("Магазинов должно быть больше нуля")
        
        generate_data(args.seed, args.years, args.stores, args.out)
        
    except InvalidConfigError as e:
        print("Ошибка в параметрах:", e)
        sys.exit(1)
    except Exception as e:
        print("Что-то пошло не так:", e)
        sys.exit(1)

if __name__=='__main__':
    main()