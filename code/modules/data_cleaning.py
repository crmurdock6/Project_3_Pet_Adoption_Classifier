import re
import numpy as np


def convert_ages(column):
    """
    A function applied to a df column where, given an age column with months,
    days, weeks, or years, converts all ages to months

    INPUT:
    column - an age entry from a dataframe column

    OUTPUT:
    An age given in months
    """
    age_regex = re.compile(r'\d+')
    if 'months' in column or 'month' in column:
        age_initial = age_regex.search(column)
        return int(age_initial.group())
    elif 'years' in column or 'year' in column:
        age_initial = age_regex.search(column)
        return int(age_initial.group()) * 12
    elif 'day' in column or 'days' in column:
        age_initial = age_regex.search(column)
        return int(age_initial.group()) / 30
    elif 'week' in column or 'weeks' in column:
        age_initial = age_regex.search(column)
        return int(age_initial.group()) / 4
    else:
        print(column)


def group_colors(color):
    """
    A function applied to a df column that groups colors into a more reasonable
    subset

    INPUT:
    color - a color entry in a dataframe column

    OUTPUT:
    A color in a given subset of colors
    """
    if '/' in color:
        color = color.split('/')
        if color[0].lower() == color[1].lower():
            color = color[0]
        elif 'brindle' in color[0].lower() or 'brindle' in color[1].lower():
            color = 'Brindle'
        elif 'tick' in color[0].lower() or 'tick' in color[1].lower():
            color = 'Tick'
        elif 'merle' in color[0].lower() or 'merle' in color[1].lower():
            color = 'Merle'
        else:
            color = 'Twocolor'
    else:
        if 'brindle' in color.lower():
            color = 'Brindle'
        elif 'brown brindle' in color.lower():
            color = 'Brindle'
        elif 'tiger' in color.lower():
            color = 'Brindle'
        elif 'tick' in color.lower():
            color = 'Tick'
        elif 'merle' in color.lower():
            color = 'Merle'
        elif 'smoke' in color.lower() or 'cream' in color.lower():
            coat_color = color.split(' ')
            color = coat_color[0]
        else:
            color = color
    return color


def pit_bull_separation(breed):
    """
    A function applied to a df column of breeds that returns whether an animal
    is a pitbull or not

    INPUT:
    breed - a breed entry from a dataframe column

    OUTPUT:
    Either 'Pit Bull' or 'Not Pit Bull' as the new breed
    """
    if 'bull' in breed.lower():
        return 'Pit Bull'
    else:
        return 'Not Pit Bull'


def pure_vs_mix(breed):
    """
    A function applied to a df column of breeds that returns whether an animal
    is purebred or not

    INPUT:
    breed - a breed entry from a dataframe column

    OUTPUT:
    Either 'Purebred' or 'Not Purebred' as the new breed
    """
    if '/' in breed:
        return 'Mixed Breed'
    elif ' Mix' in breed:
        return 'Mixed Breed'
    else:
        return 'Purebred'


def encode_columns(df, le):
    """
    A function applied to a df that encodes the desired categorical colums and
    converts the time the animal has been in the shelter to days

    INPUT:
    df - the dataframe name
    le - a variable that has been assigned to LabelEncoder() from sklearn

    OUTPUT:
    The dataframe with categorical columns of interest encoded instead of as
    strings and times converted to days
    """

    columns_to_encode = ['OUTCOME_TYPE', 'SEX_ON_OUTCOME', 'BREED', 'COLOR',
                         'INTAKE_TYPE', 'INTAKE_CONDITION', 'SEX_ON_INTAKE']
    timediff_in_days = []

    for column in columns_to_encode:
        le.fit(list(df[column].values))
        # path = '/Users/murdock/Documents/metis/project3/pkl_files/'
        # pkl_filename = column + '.pkl'
        # model_pkl = open(path + pkl_filename, 'wb')
        # pickle.dump(le, model_pkl)
        # model_pkl.close()
        labels = le.transform(list(df[column].values))
        df[column] = labels
    for time in df['TIME_DIFF'].values:
        days = time.astype('timedelta64[D]')
        days / np.timedelta64(1, 'D')
        timediff_in_days.append(days.astype(int))
    df['TIME_DIFF'] = timediff_in_days
    return df


def convert_time_diff(df, le):
    """
    A function applied to a df that encodes the desired categorical colums and
    converts the time the animal has been in the shelter to days

    INPUT:
    df - the dataframe name
    le - a variable that has been assigned to LabelEncoder() from sklearn

    OUTPUT:
    The dataframe with categorical columns of interest encoded instead of as
    strings and times converted to days
    """
    timediff_in_days = []
    for time in df['TIME_DIFF'].values:
        days = time.astype('timedelta64[D]')
        days / np.timedelta64(1, 'D')
        timediff_in_days.append(days.astype(int))
    df['TIME_DIFF'] = timediff_in_days
    labels = le.fit_transform(list(df['OUTCOME_TYPE'].values))
    df['OUTCOME_TYPE'] = labels
    return df


def group_outcomes(outcome):
    """
    Given a dataframe column of outcomes, iterates through the column and
    determines whether the outcome should be adopted or not

    INPUT:
    outcome - an entry in the dataframe column where the function is applied

    OUTPUT:
    An outcome of either adopted or not adopted
    """
    if outcome == 'Adoption':
        return outcome
    else:
        return 'Not Adopted'
