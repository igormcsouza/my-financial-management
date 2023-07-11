from typing import Dict, List, Tuple

import pandas as pd
import numpy as np

from data_translation import Headers, Methods, Categories, TransactionType


class QueryError(Exception):
    ...

# General Transformations

def calculate_days_in_interval(initial: np.datetime64, final: np.datetime64) -> int:
    return int((final - initial) / np.timedelta64(1, 'D'))

def query_rows_by_column_values(data: pd.DataFrame, columns: str, values: List[str]) -> pd.DataFrame:
    return data.loc[data[columns].isin(values), :]

def query_rows_beside_columns_values(data: pd.DataFrame, columns: str, values: List[str]) -> pd.DataFrame:
    return data.loc[~data[columns].isin(values), :]

def rename_header(data: pd.DataFrame, new_headers: Dict[str, str]) -> pd.DataFrame:
    return data.rename(columns=new_headers)

def filter_by_date_range(data: pd.DataFrame, initial: np.datetime64, final: np.datetime64) -> pd.DataFrame:
    return data[data[Headers.DATE].between(initial, final)]

# More specific transformations

def total_cash_by_main_categories_in_range(data: pd.DataFrame, date_range: Tuple[np.datetime64, np.datetime64]) -> pd.DataFrame:
    return_data = dict()
    
    data = filter_by_date_range(data, *date_range)
    data = query_rows_by_column_values(data, Headers.METHOD, [Methods.DEBIT])

    return_data['labels'] = ('food', 'fixed', 'rest')
    
    food = sum(
        query_rows_by_column_values(data, Headers.CATEGORY, [Categories.FOOD,
            Categories.CLOTHING, Categories.ANIMALS, Categories.HEALTH, Categories.PLAY,
            Categories.TRANSPORTATION, Categories.OTHERS])[Headers.AMOUNT]
    )
    fixed = sum(
        query_rows_by_column_values(data, Headers.CATEGORY, [Categories.THITHING, 
            Categories.BILLS])[Headers.AMOUNT]
    )
    rest = sum(query_rows_by_column_values(data, Headers.CATEGORY, [Categories.SALARY])[Headers.AMOUNT]) - food - fixed
    
    return_data['values'] = (food, fixed, rest)

    return pd.DataFrame(return_data)

def balance_in_range(data: pd.DataFrame, date_range: Tuple[np.datetime64, np.datetime64]) -> pd.DataFrame:
    return_data = dict()
    
    data = filter_by_date_range(data, *date_range)
    data = query_rows_by_column_values(data, Headers.METHOD, [Methods.DEBIT])

    return_data['types'] = ("incoming", "outgoing") 

    return_data['values'] = (
        sum(
            query_rows_by_column_values(data, Headers.TYPE, [TransactionType.INCOMING])[Headers.AMOUNT]
        ),
        sum(
            query_rows_by_column_values(data, Headers.TYPE, [TransactionType.OUTGOING])[Headers.AMOUNT]
        )
    )

    return pd.DataFrame(return_data)
