import pandas as pd
import datetime

important_disorders = {'Mood Disorder (Depression, Bipolar Disorder, etc)',
                       'Anxiety Disorder (Generalized, Social, Phobia, etc)',
                       'Attention Deficit Hyperactivity Disorder', 'Post-traumatic Stress Disorder',
                       'Obsessive-Compulsive Disorder', 'Stress Response Syndromes',
                       'Personality Disorder (Borderline, Antisocial, Paranoid, etc)', 'Substance Use Disorder',
                       'Addictive Disorder', 'Eating Disorder (Anorexia, Bulimia, etc)', 'Dissociative Disorder',
                       'Psychotic Disorder (Schizophrenia, Schizoaffective, etc)'}


def make_diagnosed_disorder_col(df):
    assert isinstance(df, pd.DataFrame)
    return [
        [x if (isinstance(x, str) and x in important_disorders) else 'Other' for x in disorders if isinstance(x, str)]
        for disorders in df.loc[:, 'Anxiety Disorder (Generalized, Social, Phobia, etc).2':'Other.2'].values.tolist()]


def make_believed_disorder_col(df):
    assert isinstance(df, pd.DataFrame)
    return [
        [x if (isinstance(x, str) and x in important_disorders) else 'Other' for x in disorders if isinstance(x, str)]
        for disorders in df.loc[:, 'Anxiety Disorder (Generalized, Social, Phobia, etc).1':'Other.1'].values.tolist()]


def gender_standardization(gender, male_list, female_list):
    """
    Standardizes genders to integer values based on the string lists
    provided in male_list and female_list. Returns 0 for male, 1 for female,
    2 for other, and -1 for null entries.
    """
    if isinstance(gender, int) and gender == -1:
        return -1

    assert isinstance(gender, str)

    if gender in male_list:
        return 0
    elif gender in female_list:
        return 1
    else:
        return 2


def standardize_disorders(disorders):
    """
    Standardizes the list of disorders
    from a string into a list of strings
    """
    if isinstance(disorders, int):
        return []
    assert isinstance(disorders, str)
    disorder_list = []
    in_parenthesis = False
    disorder = ""
    for char in disorders:
        if (char == "," or char == "|") and not in_parenthesis:
            if disorder.strip() in important_disorders:
                disorder_list.append(disorder.strip())
            disorder = ""
            in_parenthesis = False
        elif char == "(":
            in_parenthesis = True
            disorder += char
        elif char == ")":
            in_parenthesis = False
            disorder += char
        else:
            disorder += char
    if disorder.strip() in important_disorders:
        disorder_list.append(disorder.strip())
    return disorder_list


def to_1D(series):
    """
    Converts input to a panda compatible series so functions
    like value_counts works on lists
    """
    assert isinstance(pd.Series)
    return pd.Series([x for _list in series for x in _list])


def get_cleaned_df():
    data_2016 = pd.read_csv('data/OSMI 2016 Mental Health in Tech Survey Results.csv')
    data_2017 = pd.read_csv('data/OSMI 2017 Mental Health in Tech Survey Results.csv')
    data_2018 = pd.read_csv('data/OSMI 2018 Mental Health in Tech Survey Results.csv')
    data_2019 = pd.read_csv('data/OSMI 2019 Mental Health in Tech Survey Results.csv')
    data_2020 = pd.read_csv('data/OSMI 2020 Mental Health in Tech Survey Results.csv')

    valid_columns_2016 = ['Are you self-employed?',
                          'How many employees does your company or organization have?',
                          'Is your employer primarily a tech company/organization?',
                          'Is your primary role within your company related to tech/IT?',
                          'Does your employer provide mental health benefits as part of healthcare coverage?',
                          'Do you know the options for mental health care available under your employer-provided '
                          'coverage?',
                          'Has your employer ever formally discussed mental health (for example, as part of a '
                          'wellness campaign or other official communication)?',
                          'Does your employer offer resources to learn more about mental health concerns and options '
                          'for seeking help?',
                          'If a mental health issue prompted you to request a medical leave from work, asking for '
                          'that leave would be:',
                          'Would you feel comfortable discussing a mental health disorder with your direct '
                          'supervisor(s)?',
                          'Would you feel comfortable discussing a mental health disorder with your coworkers?',
                          'Do you currently have a mental health disorder?',
                          'If maybe, what condition(s) do you believe you have?',
                          'If yes, what condition(s) have you been diagnosed with?',
                          'What is your age?', 'What is your gender?',
                          'What country do you live in?',
                          'What US state or territory do you live in?',
                          'What country do you work in?',
                          'What US state or territory do you work in?']
    data_2016 = data_2016[valid_columns_2016]

    data_2017['believed_mh_disorder'] = make_believed_disorder_col(data_2017)
    data_2017['diagnosed_mh_disorder'] = make_diagnosed_disorder_col(data_2017)

    valid_columns_2017 = [
        'Are you self-employed?',
        'How many employees does your company or organization have?',
        'Is your employer primarily a tech company/organization?',
        'Is your primary role within your company related to tech/IT?',
        'Does your employer provide mental health benefits\xa0as part of healthcare coverage?',
        'Do you know the options for mental health care available under your employer-provided health coverage?',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or '
        'other official communication)?',
        'Does your employer offer resources to learn more about mental health disorders and options for seeking help?',
        'Overall, how much importance does your employer place on mental health?',
        'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it '
        'be to ask for that leave?',
        'Would you feel comfortable discussing a mental health issue with your coworkers?',
        'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?',
        'Do you currently have a mental health disorder?',
        'believed_mh_disorder',
        'diagnosed_mh_disorder',
        'What is your age?',
        'What is your gender?',
        'What country do you live in?',
        'What US state or territory do you live in?',
        'What country do you work in?',
        'What US state or territory do you work in?',
    ]

    data_2017.columns = data_2017.columns.str.replace('</strong>', '')
    data_2017.columns = data_2017.columns.str.replace('<strong>', '')
    data_2017 = data_2017[valid_columns_2017]

    data_2018['believed_mh_disorder'] = make_believed_disorder_col(data_2018)
    data_2018['diagnosed_mh_disorder'] = make_diagnosed_disorder_col(data_2018)

    valid_columns_2018 = ['<strong>Are you self-employed?</strong>',
                          'How many employees does your company or organization have?',
                          'Is your employer primarily a tech company/organization?',
                          'Is your primary role within your company related to tech/IT?',
                          'Does your employer provide mental health benefits as part of healthcare coverage?',
                          'Do you know the options for mental health care available under your employer-provided '
                          'health coverage?',
                          'Has your employer ever formally discussed mental health (for example, as part of a wellness '
                          'campaign or other official communication)?',
                          'Does your employer offer resources to learn more about mental health disorders and options '
                          'for seeking help?',
                          'If a mental health issue prompted you to request a medical leave from work, how easy or '
                          'difficult would it be to ask for that leave?',
                          'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?',
                          'Would you feel comfortable discussing a mental health issue with your coworkers?',
                          'Overall, how much importance does your employer place on mental health?',
                          'Do you currently have a mental health disorder?',
                          'believed_mh_disorder',
                          'diagnosed_mh_disorder',
                          'What is your age?', 'What is your gender?',
                          'What country do you <strong>live</strong> in?',
                          'What US state or territory do you <strong>live</strong> in?',
                          'What country do you <strong>work</strong> in?',
                          'What US state or territory do you <strong>work</strong> in?']
    data_2018 = data_2018[valid_columns_2018]

    valid_columns_2019 = ['*Are you self-employed?*',
                          'How many employees does your company or organization have?',
                          'Is your employer primarily a tech company/organization?',
                          'Is your primary role within your company related to tech/IT?',
                          'Does your employer provide mental health benefits as part of healthcare coverage?',
                          'Do you know the options for mental health care available under your employer-provided '
                          'health coverage?',
                          'Has your employer ever formally discussed mental health (for example, as part of a wellness '
                          'campaign or other official communication)?',
                          'Does your employer offer resources to learn more about mental health disorders and options '
                          'for seeking help?',
                          'If a mental health issue prompted you to request a medical leave from work, how easy or '
                          'difficult would it be to ask for that leave?',
                          'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?',
                          'Would you feel comfortable discussing a mental health issue with your coworkers?',
                          'Overall, how much importance does your employer place on mental health?',
                          'Do you *currently* have a mental health disorder?',
                          '*If possibly, what disorder(s) do you believe you have?*',
                          '*If so, what disorder(s) were you diagnosed with?*',
                          'What is your age?', 'What is your gender?',
                          'What country do you *live* in?',
                          'What US state or territory do you *live* in?',
                          'What country do you *work* in?',
                          'What US state or territory do you *work* in?']

    data_2019 = data_2019[valid_columns_2019]

    data_2020['believed_mh_disorder'] = make_believed_disorder_col(data_2020)
    data_2020['diagnosed_mh_disorder'] = make_diagnosed_disorder_col(data_2020)

    valid_columns = ['*Are you self-employed?*',
                     'How many employees does your company or organization have?',
                     'Is your employer primarily a tech company/organization?',
                     'Is your primary role within your company related to tech/IT?',
                     'Does your employer provide mental health benefits as part of healthcare coverage?',
                     'Do you know the options for mental health care available under your employer-provided health '
                     'coverage?',
                     'Has your employer ever formally discussed mental health (for example, as part of a wellness '
                     'campaign or other official communication)?',
                     'Does your employer offer resources to learn more about mental health disorders and options for '
                     'seeking help?',
                     'If a mental health issue prompted you to request a medical leave from work, how easy or '
                     'difficult would it be to ask for that leave?',
                     'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?',
                     'Would you feel comfortable discussing a mental health issue with your coworkers?',
                     'Overall, how much importance does your employer place on mental health?',
                     'Do you *currently* have a mental health disorder?',
                     'believed_mh_disorder',
                     'diagnosed_mh_disorder',
                     'What is your age?', 'What is your gender?',
                     'What country do you *live* in?',
                     'What US state or territory do you *live* in?',
                     'What country do you *work* in?',
                     'What US state or territory do you *work* in?']
    data_2020 = data_2020[valid_columns]

    employee_count_dict = {'1-5': 0, '6-25': 1, '26-100': 2, '100-500': 3, '500-1000': 4, 'More than 1000': 5}
    yes_no_mapping = {"Yes": 2, "I don't know": 1, "I am not sure": 1, "No": 0, "Not eligible for coverage / N/A": 0,
                      "Not eligible for coverage / NA": 0}
    difficulty_mapping = {'Very easy': 3, 'Somewhat easy': 3, 'Neither easy nor difficult': 2, "I don't know": 2,
                          'Somewhat difficult': 0, 'Difficult': 0, 'Very difficult': 0}
    yes_no_maybe_mapping = {'Yes': 2, 'Maybe': 1, 'No': 0}
    yes_no_possibly_mapping = {'Yes': 3, 'Maybe': 2, 'Possibly': 2, "Don't Know": 1, 'No': 0}

    column_name_mapping_2016 = {
        'Are you self-employed?': 'self_employed',
        'How many employees does your company or organization have?': 'employee_count',
        'Is your employer primarily a tech company/organization?': 'is_tech_company',
        'Is your primary role within your company related to tech/IT?': 'is_tech_role',
        'Does your employer provide mental health benefits as part of healthcare coverage?': 'provide_mh_benefits',
        'Do you know the options for mental health care available under your employer-provided coverage?': 'know_mh_coverage',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?': "formal_discuss_mh",
        'Does your employer offer resources to learn more about mental health concerns and options for seeking help?': "offer_mh_learning_resources",
        'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:': "mh_leave_difficult",
        'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?': "discuss_mh_with_supervisor",
        'Would you feel comfortable discussing a mental health disorder with your coworkers?': "discuss_mh_with_coworkers",
        'Do you currently have a mental health disorder?': "has_mh_disorder",
        'If maybe, what condition(s) do you believe you have?': "believed_mh_disorder",
        'If yes, what condition(s) have you been diagnosed with?': "diagnosed_mh_disorder",
        'What is your age?': "age",
        'What is your gender?': "gender",
        'What country do you live in?': "live_country",
        'What US state or territory do you live in?': "live_state",
        'What country do you work in?': "work_country",
        'What US state or territory do you work in?': "work_state"
    }
    data_2016 = data_2016.rename(columns=column_name_mapping_2016)

    column_name_mapping_2017 = {
        'Are you self-employed?': 'self_employed',
        'How many employees does your company or organization have?': 'employee_count',
        'Is your employer primarily a tech company/organization?': 'is_tech_company',
        'Is your primary role within your company related to tech/IT?': 'is_tech_role',
        'Does your employer provide mental health benefits\xa0as part of healthcare coverage?': 'provide_mh_benefits',
        'Do you know the options for mental health care available under your employer-provided health coverage?': 'know_mh_coverage',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?': "formal_discuss_mh",
        'Does your employer offer resources to learn more about mental health disorders and options for seeking help?': "offer_mh_learning_resources",
        'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?': "mh_leave_difficult",
        'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?': "discuss_mh_with_supervisor",
        'Would you feel comfortable discussing a mental health issue with your coworkers?': "discuss_mh_with_coworkers",
        'Overall, how much importance does your employer place on mental health?': "mh_importance",
        'Do you currently have a mental health disorder?': "has_mh_disorder",
        'What is your age?': "age",
        'What is your gender?': "gender",
        'What country do you live in?': "live_country",
        'What US state or territory do you live in?': "live_state",
        'What is your race?': "race",
        'What country do you work in?': "work_country",
        'What US state or territory do you work in?': "work_state"
    }
    data_2017 = data_2017.rename(columns=column_name_mapping_2017)

    column_name_mapping_2018 = {
        '<strong>Are you self-employed?</strong>': 'self_employed',
        'How many employees does your company or organization have?': 'employee_count',
        'Is your employer primarily a tech company/organization?': 'is_tech_company',
        'Is your primary role within your company related to tech/IT?': 'is_tech_role',
        'Does your employer provide mental health benefits as part of healthcare coverage?': 'provide_mh_benefits',
        'Do you know the options for mental health care available under your employer-provided health coverage?': 'know_mh_coverage',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?': "formal_discuss_mh",
        'Does your employer offer resources to learn more about mental health disorders and options for seeking help?': "offer_mh_learning_resources",
        'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?': "mh_leave_difficult",
        'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?': "discuss_mh_with_supervisor",
        'Would you feel comfortable discussing a mental health issue with your coworkers?': "discuss_mh_with_coworkers",
        'Overall, how much importance does your employer place on mental health?': "mh_importance",
        'Do you currently have a mental health disorder?': "has_mh_disorder",
        'What is your age?': "age",
        'What is your gender?': "gender",
        'What country do you <strong>live</strong> in?': "live_country",
        'What US state or territory do you <strong>live</strong> in?': "live_state",
        'What country do you <strong>work</strong> in?': "work_country",
        'What US state or territory do you <strong>work</strong> in?': "work_state"
    }
    data_2018 = data_2018.rename(columns=column_name_mapping_2018)

    column_name_mapping_2019 = {
        '*Are you self-employed?*': 'self_employed',
        'How many employees does your company or organization have?': 'employee_count',
        'Is your employer primarily a tech company/organization?': 'is_tech_company',
        'Is your primary role within your company related to tech/IT?': 'is_tech_role',
        'Does your employer provide mental health benefits as part of healthcare coverage?': 'provide_mh_benefits',
        'Do you know the options for mental health care available under your employer-provided health coverage?': 'know_mh_coverage',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?': "formal_discuss_mh",
        'Does your employer offer resources to learn more about mental health disorders and options for seeking help?': "offer_mh_learning_resources",
        'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?': "mh_leave_difficult",
        'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?': "discuss_mh_with_supervisor",
        'Would you feel comfortable discussing a mental health issue with your coworkers?': "discuss_mh_with_coworkers",
        'Overall, how much importance does your employer place on mental health?': "mh_importance",
        'Do you *currently* have a mental health disorder?': "has_mh_disorder",
        '*If possibly, what disorder(s) do you believe you have?*': "believed_mh_disorder",
        '*If so, what disorder(s) were you diagnosed with?*': "diagnosed_mh_disorder",
        'What is your age?': "age",
        'What is your gender?': "gender",
        'What country do you *live* in?': "live_country",
        'What US state or territory do you *live* in?': "live_state",
        'What country do you *work* in?': "work_country",
        'What US state or territory do you *work* in?': "work_state"
    }
    data_2019 = data_2019.rename(columns=column_name_mapping_2019)

    column_name_mapping_2020 = {
        '*Are you self-employed?*': 'self_employed',
        'How many employees does your company or organization have?': 'employee_count',
        'Is your employer primarily a tech company/organization?': 'is_tech_company',
        'Is your primary role within your company related to tech/IT?': 'is_tech_role',
        'Does your employer provide mental health benefits as part of healthcare coverage?': 'provide_mh_benefits',
        'Do you know the options for mental health care available under your employer-provided health coverage?': 'know_mh_coverage',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?': "formal_discuss_mh",
        'Does your employer offer resources to learn more about mental health disorders and options for seeking help?': "offer_mh_learning_resources",
        'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?': "mh_leave_difficult",
        'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?': "discuss_mh_with_supervisor",
        'Would you feel comfortable discussing a mental health issue with your coworkers?': "discuss_mh_with_coworkers",
        'Overall, how much importance does your employer place on mental health?': "mh_importance",
        'Do you *currently* have a mental health disorder?': "has_mh_disorder",
        'What is your age?': "age",
        'What is your gender?': "gender",
        'What country do you *live* in?': "live_country",
        'What US state or territory do you *live* in?': "live_state",
        'What country do you *work* in?': "work_country",
        'What US state or territory do you *work* in?': "work_state"
    }
    data_2020 = data_2020.rename(columns=column_name_mapping_2020)

    data_2016 = data_2016.fillna(-1)
    data_2017 = data_2017.fillna(-1)
    data_2018 = data_2018.fillna(-1)
    data_2019 = data_2019.fillna(-1)
    data_2020 = data_2020.fillna(-1)

    data_2016['self_employed'] = data_2016['self_employed'].astype("int32")
    data_2016['is_tech_company'] = data_2016['is_tech_company'].astype("int32")
    data_2016['is_tech_role'] = data_2016['is_tech_role'].astype("int32")
    data_2016['age'] = data_2016['age'].astype("int32")

    data_2016['employee_count'] = data_2016['employee_count'].replace(employee_count_dict)

    data_2016['provide_mh_benefits'] = data_2016['provide_mh_benefits'].replace(yes_no_mapping)
    data_2016['know_mh_coverage'] = data_2016['know_mh_coverage'].replace(yes_no_mapping)
    data_2016['formal_discuss_mh'] = data_2016['formal_discuss_mh'].replace(yes_no_mapping)
    data_2016['offer_mh_learning_resources'] = data_2016['offer_mh_learning_resources'].replace(yes_no_mapping)

    data_2016['mh_leave_difficult'] = data_2016['mh_leave_difficult'].replace(difficulty_mapping)

    data_2016['discuss_mh_with_supervisor'] = data_2016['discuss_mh_with_supervisor'].replace(yes_no_maybe_mapping)
    data_2016['discuss_mh_with_coworkers'] = data_2016['discuss_mh_with_coworkers'].replace(yes_no_maybe_mapping)

    data_2016['has_mh_disorder'] = data_2016['has_mh_disorder'].replace(yes_no_possibly_mapping)

    data_2016['believed_mh_disorder'] = data_2016['believed_mh_disorder'].apply(standardize_disorders)
    data_2016['diagnosed_mh_disorder'] = data_2016['diagnosed_mh_disorder'].apply(standardize_disorders)

    data_2016['believed_mh_disorder'] = data_2016['believed_mh_disorder'].apply(tuple)
    data_2016['diagnosed_mh_disorder'] = data_2016['diagnosed_mh_disorder'].apply(tuple)

    male_2016 = ['Male', 'male', 'Male ', 'M', 'm', 'man', 'Cis male',
            'Male.', 'Male (cis)', 'Man', 'Sex is male', 'Male (trans, FtM)',
            'cis male', 'Malr', 'Dude', 'Male/genderqueer',
            "I'm a man why didn't you make this a drop down question. You should of asked sex? And I would of "
            "answered yes please. Seriously how much text can this take? ",
            'mail', 'M|', 'male ', 'Cis Male', 'cisdude', 'cis man', 'MALE']

    female_2016 = ['Female', 'female', 'I identify as female.', 'female ', 'Female assigned at birth ',
              'F', 'Woman', 'fm', 'f', 'Cis female ', 'Transitioned, M2F', 'Genderfluid (born female)',
              'Female or Multi-Gender Femme',
              'Female ', 'woman', 'female/woman', 'Cisgender Female', 'fem',
              'Female (props for making this a freeform field, though)',
              ' Female', 'Cis-woman', 'Genderflux demi-girl', 'female-bodied; no feelings about gender',
              'Transgender woman', 'genderqueer woman']

    data_2016['gender'] = data_2016['gender'].apply(gender_standardization, args=(male_2016, female_2016))

    data_2017['self_employed'] = data_2017['self_employed'].astype("int32")
    data_2017['is_tech_company'] = data_2017['is_tech_company'].astype("int32")
    data_2017['is_tech_role'] = data_2017['is_tech_role'].astype("int32")
    data_2017['age'] = data_2017['age'].astype("int32")
    data_2017['mh_importance'] = data_2017['mh_importance'].astype("int32")

    data_2017['employee_count'] = data_2017['employee_count'].replace(employee_count_dict)

    data_2017['provide_mh_benefits'] = data_2017['provide_mh_benefits'].replace(yes_no_mapping)
    data_2017['know_mh_coverage'] = data_2017['know_mh_coverage'].replace(yes_no_mapping)
    data_2017['formal_discuss_mh'] = data_2017['formal_discuss_mh'].replace(yes_no_mapping)
    data_2017['offer_mh_learning_resources'] = data_2017['offer_mh_learning_resources'].replace(yes_no_mapping)

    data_2017['mh_leave_difficult'] = data_2017['mh_leave_difficult'].replace(difficulty_mapping)

    data_2017['discuss_mh_with_supervisor'] = data_2017['discuss_mh_with_supervisor'].replace(yes_no_maybe_mapping)
    data_2017['discuss_mh_with_coworkers'] = data_2017['discuss_mh_with_coworkers'].replace(yes_no_maybe_mapping)

    data_2017['has_mh_disorder'] = data_2017['has_mh_disorder'].replace(yes_no_possibly_mapping)

    data_2017['believed_mh_disorder'] = data_2017['believed_mh_disorder'].apply(tuple)
    data_2017['diagnosed_mh_disorder'] = data_2017['diagnosed_mh_disorder'].apply(tuple)

    male_2017 = ['male', 'Male', 'M', 'Man', 'cis-male', 'Mail', 'm', 'Male (cis)', 'Cis male', 'Male ', 'Cis-male',
            'Cis Male', 'dude']
    female_2017 = ['Female', 'F', 'female', 'f', 'Female', 'Woman', 'femalw', 'femail', 'female (cis)', 'woman',
              'female (cisgender)', 'Female (cis) ', 'cis-Female', 'cis female', 'F, cisgender']
    data_2017['gender'] = data_2017['gender'].apply(gender_standardization, args=(male_2017, female_2017))

    data_2018['self_employed'] = data_2018['self_employed'].astype("int32")
    data_2018['is_tech_company'] = data_2018['is_tech_company'].astype("int32")
    data_2018['is_tech_role'] = data_2018['is_tech_role'].astype("int32")
    data_2018['age'] = data_2018['age'].astype("int32")
    data_2018['mh_importance'] = data_2018['mh_importance'].astype("int32")

    data_2018['employee_count'] = data_2018['employee_count'].replace(employee_count_dict)

    data_2018['provide_mh_benefits'] = data_2018['provide_mh_benefits'].replace(yes_no_mapping)
    data_2018['know_mh_coverage'] = data_2018['know_mh_coverage'].replace(yes_no_mapping)
    data_2018['formal_discuss_mh'] = data_2018['formal_discuss_mh'].replace(yes_no_mapping)
    data_2018['offer_mh_learning_resources'] = data_2018['offer_mh_learning_resources'].replace(yes_no_mapping)

    data_2018['mh_leave_difficult'] = data_2018['mh_leave_difficult'].replace(difficulty_mapping)

    data_2018['discuss_mh_with_supervisor'] = data_2018['discuss_mh_with_supervisor'].replace(yes_no_maybe_mapping)
    data_2018['discuss_mh_with_coworkers'] = data_2018['discuss_mh_with_coworkers'].replace(yes_no_maybe_mapping)

    data_2018['has_mh_disorder'] = data_2018['has_mh_disorder'].replace(yes_no_possibly_mapping)

    data_2018['believed_mh_disorder'] = data_2018['believed_mh_disorder'].apply(tuple)
    data_2018['diagnosed_mh_disorder'] = data_2018['diagnosed_mh_disorder'].apply(tuple)

    male_2018 = ['male', 'Male', 'Ostensibly Male', 'male, born with xy chromosoms', 'Malel', 'M',
            'MALE', 'm', 'Male (or female, or both)', 'Trans man', 'Cis-male', 'Male ',
            'cis male', 'Cis Male', 'Man', 'Demiguy', 'Cisgender male']
    female_2018 = ['Female', 'female', 'Female ', 'Woman', 'woman', 'F', 'f',
              'I identify as female', '*shrug emoji* (F)',
              'Female/gender non-binary.', 'Cis woman',
              'Female (cisgender)', 'Cis-Female', 'Cisgendered woman',
              'Trans woman', 'Trans female',
              'She/her/they/them', 'Cis female ',
              'cisgender female', 'Nonbinary/femme',
              'gender non-conforming woman']

    data_2018['gender'] = data_2018['gender'].apply(gender_standardization, args=(male_2018, female_2018))

    data_2019['self_employed'] = data_2019['self_employed'].astype("int32")
    data_2019['is_tech_company'] = data_2019['is_tech_company'].astype("int32")
    data_2019['is_tech_role'] = data_2019['is_tech_role'].astype("int32")
    data_2019['age'] = data_2019['age'].astype("int32")
    data_2019['mh_importance'] = data_2019['mh_importance'].astype("int32")

    data_2019['employee_count'] = data_2019['employee_count'].replace(employee_count_dict)

    data_2019['provide_mh_benefits'] = data_2019['provide_mh_benefits'].replace(yes_no_mapping)
    data_2019['know_mh_coverage'] = data_2019['know_mh_coverage'].replace(yes_no_mapping)
    data_2019['formal_discuss_mh'] = data_2019['formal_discuss_mh'].replace(yes_no_mapping)
    data_2019['offer_mh_learning_resources'] = data_2019['offer_mh_learning_resources'].replace(yes_no_mapping)

    data_2019['mh_leave_difficult'] = data_2019['mh_leave_difficult'].replace(difficulty_mapping)

    data_2019['discuss_mh_with_supervisor'] = data_2019['discuss_mh_with_supervisor'].replace(yes_no_maybe_mapping)
    data_2019['discuss_mh_with_coworkers'] = data_2019['discuss_mh_with_coworkers'].replace(yes_no_maybe_mapping)

    data_2019['has_mh_disorder'] = data_2019['has_mh_disorder'].replace(yes_no_possibly_mapping)

    data_2019['believed_mh_disorder'] = data_2019['believed_mh_disorder'].apply(standardize_disorders)
    data_2019['diagnosed_mh_disorder'] = data_2019['diagnosed_mh_disorder'].apply(standardize_disorders)

    data_2019['believed_mh_disorder'] = data_2019['believed_mh_disorder'].apply(tuple)
    data_2019['diagnosed_mh_disorder'] = data_2019['diagnosed_mh_disorder'].apply(tuple)

    male_2019 = ['Male', 'male', 'm', 'M',
            'Let\'s keep it simple and say "male"', 'Identify as male',
            'Male ', 'Masculine', 'Cishet male',
            'Man', 'cis male', 'Cis Male', 'Trans man', 'man',
            'masculino', 'Make',
            'CIS Male']
    female_2019 = ['female', 'Female', 'F', 'f',
              'Woman', 'Female-identified', 'woman', 'cis woman',
              'Agender trans woman', 'Female ', 'femmina', 'Femile' 'Female (cis)']

    data_2019['gender'] = data_2019['gender'].apply(gender_standardization, args=(male_2019, female_2019))

    data_2020['self_employed'] = data_2020['self_employed'].astype("int32")
    data_2020['is_tech_company'] = data_2020['is_tech_company'].astype("int32")
    data_2020['is_tech_role'] = data_2020['is_tech_role'].astype("int32")
    data_2020['age'] = data_2020['age'].astype("int32")
    data_2020['mh_importance'] = data_2020['mh_importance'].astype("int32")

    data_2020['employee_count'] = data_2020['employee_count'].replace(employee_count_dict)

    data_2020['provide_mh_benefits'] = data_2020['provide_mh_benefits'].replace(yes_no_mapping)
    data_2020['know_mh_coverage'] = data_2020['know_mh_coverage'].replace(yes_no_mapping)
    data_2020['formal_discuss_mh'] = data_2020['formal_discuss_mh'].replace(yes_no_mapping)
    data_2020['offer_mh_learning_resources'] = data_2020['offer_mh_learning_resources'].replace(yes_no_mapping)

    data_2020['mh_leave_difficult'] = data_2020['mh_leave_difficult'].replace(difficulty_mapping)

    data_2020['discuss_mh_with_supervisor'] = data_2020['discuss_mh_with_supervisor'].replace(yes_no_maybe_mapping)
    data_2020['discuss_mh_with_coworkers'] = data_2020['discuss_mh_with_coworkers'].replace(yes_no_maybe_mapping)

    data_2020['has_mh_disorder'] = data_2020['has_mh_disorder'].replace(yes_no_possibly_mapping)
    data_2020['believed_mh_disorder'] = data_2020['believed_mh_disorder'].apply(tuple)
    data_2020['diagnosed_mh_disorder'] = data_2020['diagnosed_mh_disorder'].apply(tuple)

    male_2020 = ['Male', 'male', 'mail', 'M', 'm', 'mostly male', 'cisgender male', 'MAle']
    female_2020 = ['female', 'Female', 'F', 'f', 'Woman', 'FEMALE', 'female, she/her']

    data_2020['gender'] = data_2020['gender'].apply(gender_standardization, args=(male_2020, female_2020))

    data_2016['year'] = datetime.datetime(2016, 1, 1)
    data_2017['year'] = datetime.datetime(2017, 1, 1)
    data_2018['year'] = datetime.datetime(2018, 1, 1)
    data_2019['year'] = datetime.datetime(2019, 1, 1)
    data_2020['year'] = datetime.datetime(2020, 1, 1)

    merged_df = data_2016.merge(data_2017, how='outer')\
                         .merge(data_2018, how='outer')\
                         .merge(data_2019, how='outer')\
                         .merge(data_2020, how='outer')

    return merged_df
