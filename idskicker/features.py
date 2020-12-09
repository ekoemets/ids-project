import pandas as pd

def add_date_as_features(df, date_column):
    """
    Adds year, month, day as features to the
    dataframe where argument dt_column will be
    the prefix for new columns.
    
    params:
        df: dataframe to which features are added
        dt_column: name of the column that will be used for datetime
    """
    date = pd.to_datetime(df[date_column])
    df[date_column + "_year"] = date.dt.year
    df[date_column + "_month"] = date.dt.month_name()
    df[date_column + "_day"] = date.dt.day_name()

def add_time_as_features(df, datetime_column):
    """
    Adds hour and minute as features to the dataframe
    where argument datetime_column will be the prefix for
    new columns.
    
    params:
        df: dataframe to which features are added
        dt_column: name of the column that will be used for datetime
    """
    datetime = pd.to_datetime(df[datetime_column])
    df[datetime_column + "_hour"] = datetime.dt.hour
    df[datetime_column + "_minute"] = datetime.dt.minute
    
    # TODO try to categorize into day parts, morning/noon/afternoon...
    # from the time provided by taking into account the timezone
    # that can be derived from country code
    

def add_text_as_features(df, text_column):
    """
    Generates different features from text column like the text length
    word count etc.
    
    params:
        df: dataframe to which features are added
        text_column: name of the text_column that features are generated from
    """
    df[text_column + "_length"] = df[text_column].str.len()
    df[text_column + "_words"] = df[text_column].str.findall(r'\w+').str.len()

def add_datediff_as_feature(df, start_date_column, end_date_column):
    """
    Calculates the difference in days between date1 and date2 by
    subtracting date1 from date2.

    params:
        df: dataframe to which feature is added
        date1: start date column name
        date2: end date column name
    """
    datetime1 = pd.to_datetime(df[start_date_column])
    datetime2 = pd.to_datetime(df[end_date_column])
    new_col_name = f"{start_date_column}_to_{end_date_column}_days"
    df[new_col_name] = (datetime2 - datetime1).dt.days
