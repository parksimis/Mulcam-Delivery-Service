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
    '''
    각 업종별 테이블의 데이터를 모두 조회하는 method
    :param table: 원하는 테이블
        테이블 목록 = [bunsik, cafe, chicken, etc, fastfood, hansik, ilsik, jimtang, jokbal, jungsik, yasik]
    :return: 원하는 테이블 쿼리 결과
    '''
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
    '''
    테이블의 결과의 시간 컬럼을 연-월-일로 컬럼을 붙여주는 메소드
    :param df: 테이블 조회 결과(DataFrame)
    :return: 테이블에 연-월-일 컬럼이 추가된 결과
    '''
    df['시간'] = pd.to_datetime(df['시간'])

    df['year'] = df['시간'].dt.year
    df['month'] = df['시간'].dt.month
    df['day'] = df['시간'].dt.day

    return df


def preprocessing_df(df, formula=None):
    '''
    조회 결과를 받아 원하는 형식으로 전처리하는 메소드
    :param df: 전처리할 dataFrame
    :param formula: 1) 일자별 - 일자별로 groupby해 평균 계산(일자별 평균 주문건수)
                    2) 시간대별 - 시간대별로 groupby해 평균 계산(시간대별 주문건수)
    :return: 전처리된 DataFrame
    '''
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
    '''
    서울과 경기도로 데이터프레임을 나누는 메소드
    :param df: 처리할 dataFrame
    :param cut_column: 서울 or 경기도 선택
    :return: cut_column으로 나눠진 dataframe
    '''
    tmp = df.loc[df['광역시도명'] == cut_column].reset_index(drop=True)
    tmp.drop('광역시도명', axis=1, inplace=True)

    return tmp


def divide_df(df):
    '''
    시간과 주문건수로 나누어주는 메소드
    :param df: 나눌 데이터프레임
    :return: 시간과 주문건수 list
    '''
    table1 = df['시간'].values
    table2 = df['주문건수'].values

    return table1.tolist(), table2.tolist()


def execute_all(table, formula):
    '''
    위의 모든 과정을 한꺼번에 실행해서 결과를 반환
    :param table: 원하는 테이블
            테이블 목록 = [bunsik, cafe, chicken, etc, fastfood, hansik, ilsik, jimtang, jokbal, jungsik, yasik]
    :param formula: 1) 일자별 - 일자별로 groupby해 평균 계산(일자별 평균 주문건수)
                    2) 시간대별 - 시간대별로 groupby해 평균 계산(시간대별 주문건수)
    :return:
    '''
    table = select_all(table)

    add_column_tbl = add_datetime_column(table)
    daily_tbl = preprocessing_df(add_column_tbl, formula='일자별')
    hour_tbl = preprocessing_df(add_column_tbl, formula='시간대별')

    sl_daily_tbl = cutting_area(daily_tbl, '서울')
    gg_daily_tbl = cutting_area(daily_tbl, '경기도')

    sl_hour_tbl = cutting_area(hour_tbl, '서울')
    gg_hour_tbl = cutting_area(hour_tbl, '경기도')

    if formula == '일자별':
        sl_daily_lbl, sl_daily_val = divide_df(sl_daily_tbl)
        gg_daily_lbl, gg_daily_val = divide_df(gg_daily_tbl)
        return sl_daily_lbl, sl_daily_val, gg_daily_lbl, gg_daily_val

    elif formula == '시간대별':
        sl_hour_lbl, sl_hour_val = divide_df(sl_hour_tbl)
        gg_hour_lbl, gg_hour_val = divide_df(gg_hour_tbl)
        return sl_hour_lbl, sl_hour_val, gg_hour_lbl, gg_hour_val


def main_line_data():
    '''
    메인 화면의 전체 배달 주문건수에 대한 데이터를 얻기위한 메소드
    :return: 모든 테이블에 대한 일별 합계 데이터
    '''
    model_list = ['chicken', 'ilsik', 'bunsik', 'yasik', 'jokbal',
                  'jungsik', 'jimtang', 'cafe', 'fastfood', 'hansik', 'etc']

    result = pd.DataFrame(columns=['광역시도명', '시간', '주문건수', '업종명'])

    for model in model_list:
        model_result = select_all(model).reset_index(drop=True)

        result = pd.concat([result, model_result], axis=0)

    add_result = add_datetime_column(result)

    main_result = add_result.loc[(add_result['year'] == max(add_result['year'])) & (
                add_result['month'] == max(add_result['month']))].reset_index(drop=True)

    main_result['주문건수'] = main_result['주문건수'].astype('int')

    line_result = main_result.groupby(['year', 'month', 'day']).sum().reset_index()
    line_result[['year', 'month', 'day']] = line_result[['year', 'month', 'day']].astype('str')
    line_result['시간'] = line_result['year'] + '-' + line_result['month'] + '-' + line_result['day']
    line_result['시간'] = pd.to_datetime(line_result['시간']).dt.strftime('%Y-%m-%d')
    line_result.drop(['year', 'month', 'day'], axis=1, inplace=True)
    line_result = line_result[['시간', '주문건수']]
    line_result['주문건수'] = line_result['주문건수'].astype('int')

    line_lbl, line_val = divide_df(line_result)

    return line_lbl, line_val


def main_pie_data():
    '''
    메인 화면의 파이 그래프에 들어갈 데이터를 전처리해주는 메소드
    파이그래프 - 월별 주문비율
    :return: 각 테이블 별 월별 주문 비율 리스트
    '''
    model_list = ['chicken', 'ilsik', 'bunsik', 'yasik', 'jokbal',
                  'jungsik', 'jimtang', 'cafe', 'fastfood', 'hansik', 'etc']

    result = pd.DataFrame(columns=['광역시도명', '시간', '주문건수', '업종명'])

    for model in model_list:
        model_result = select_all(model).reset_index(drop=True)

        result = pd.concat([result, model_result], axis=0)

    add_result = add_datetime_column(result)

    main_result = add_result.loc[(add_result['year'] == max(add_result['year'])) & (
                add_result['month'] == max(add_result['month']))].reset_index(drop=True)

    main_result['주문건수'] = main_result['주문건수'].astype('int')

    pie_result = main_result.groupby(['업종명']).agg({'주문건수': sum}).sort_values(by='주문건수', ascending=False)

    pie_data = (pie_result / pie_result.sum() * 100)

    pie_data = np.round(pie_data, 2)

    return pie_data.index.tolist(), pie_data.values.reshape(1, -1)


