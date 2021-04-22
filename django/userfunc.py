import sqlite3
import pandas as pd
import numpy as np


def select_main_table():
    '''
    index 화면에 들어갈 각 시도별/업종별 최신 배달 주문건수를 조회하는 테이블
    '''
    model_list = ['chicken', 'ilsik', 'bunsik', 'yasik', 'jokbal', 'jungsik', 'jimtang', 'cafe', 'fastfood', 'hansik', 'etc']

    result = pd.DataFrame(columns=['광역시도명', '시간', '주문건수', '업종명'])

    with sqlite3.connect('./db.sqlite3') as conn:
        cur = conn.cursor()
        i = 0

        for model in model_list:

            query = "SELECT * FROM main_" + str(model) + " ORDER BY time DESC LIMIT 2;"
            cur.execute(query)
            rows = cur.fetchall()

            for row in rows:
                result.loc[i] = row[1:]
                i += 1

        cur.close()
    conn.close()

    result = result.sort_values(by='주문건수', ascending=False).reset_index(drop=True)

    result = result[['시간', '광역시도명', '업종명', '주문건수']]
    return result.to_dict('records')


def select_all(table=None):
    conn = sqlite3.connect('./db.sqlite3')
    cur = conn.cursor()

    query = "SELECT * FROM main_" + str(table)

    cur.execute(query)

    rows = cur.fetchall()

    cur.close()
    conn.close()
    result = pd.DataFrame(rows, columns=['index', '광역시도명', '시간', '주문건수', '업종명']).sort_values(by='시간', ascending=False)
    result = result.iloc[:, 1:]

    return result


def add_datetime_column(df):
    df['시간'] = pd.to_datetime(df['시간'])

    df['year'] = df['시간'].dt.year
    df['month'] = df['시간'].dt.month
    df['day'] = df['시간'].dt.day

    return df


def preprocessing_df(df, formula=None):
    if formula == '일자별':

        tmp_df = df.loc[(df['year'] == max(df['year'])) & (df['month'] == max(df['month']))].reset_index(drop=True)

        groupby_df = np.round(tmp_df.groupby(['광역시도명', 'year', 'month', 'day']).mean(), 0)
        groupby_df['주문건수'] = groupby_df['주문건수'].astype('int')

        result = groupby_df.reset_index()

        result[['year', 'month', 'day']] = result[['year', 'month', 'day']].astype('str')

        result['시간'] = result['year'] + '-' + result['month'] + '-' + result['day']

        result['시간'] = pd.to_datetime(result['시간']).dt.strftime('%Y-%m-%d')
        result.drop(['year', 'month', 'day'], axis=1, inplace=True)

        result = result[['광역시도명', '시간', '주문건수']]

    elif formula == '시간대별':

        tmp_df = df.sort_values('시간', ascending=False)[:48]

        result = tmp_df.groupby(['광역시도명', '시간']).agg({'주문건수': sum}).reset_index()

        result['시간'] = pd.to_datetime(result['시간']).dt.strftime('%Y-%m-%d-%H') + '시'

    return result


def cutting_area(df, cut_column):
    tmp = df.loc[df['광역시도명'] == cut_column].reset_index(drop=True)
    tmp.drop('광역시도명', axis=1, inplace=True)

    return tmp


def divide_df(df):
    table1 = df['시간'].values
    table2 = df['주문건수'].values

    return table1.tolist(), table2.tolist()