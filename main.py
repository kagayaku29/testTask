import math

import pandas as pd

df = pd.read_table('sample_info.txt', delimiter='\t')

bacteria = df[
    ['comt_inhibitor', 'carbidopa_levodopa', 'anticholinergic', 'dopamine_agonist', 'amantadine', 'mao_b_inhibitor']]

# Case
for col in bacteria.columns:
    caseWithDisease = df[(df['case_control'].str.contains("Case")) & (df[col].str.contains("Y"))]
    caselWithoutDisease = df[(df['case_control'].str.contains("Case")) & (df[col].str.contains("N"))]
    caseNotApplicable = df[(df['case_control'].str.contains("Case")) & (df[col].str.contains("not applicable"))]
    caseMissing = df[(df['case_control'].str.contains("Case")) & (df[col].str.contains("Missing: Not provided"))]

    print(f"Case: Count with disease for {col}: {caseWithDisease['case_control'].count()}")
    print(f"Case: Count without disease for {col}: {caselWithoutDisease['case_control'].count()}")
    print(f"Case: Count not applicable for {col}: {caseNotApplicable['case_control'].count()}")
    print(f"Case: Count missing for {col}: {caseMissing['case_control'].count()}")

# Control
    controlWithDisease = df[(df['case_control'].str.contains("Control")) & (df[col].str.contains("Y"))]
    controlWithoutDisease = df[(df['case_control'].str.contains("Control")) & (df[col].str.contains("N"))]
    controlNotApplicable = df[(df['case_control'].str.contains("Control")) & (df[col].str.contains("not applicable"))]
    controlMissing = df[(df['case_control'].str.contains("Control")) & (df[col].str.contains("Missing: Not provided"))]

    print(f"Control: Count with disease for {col}: {controlWithDisease['case_control'].count()}")
    print(f"Control: Count without disease for {col}: {controlWithoutDisease['case_control'].count()}")
    print(f"Control: Count not applicable for {col}: {controlNotApplicable['case_control'].count()}")
    print(f"Control: Count missing for {col}: {controlMissing['case_control'].count()}")

# Alpha diversity (Shannon index)
columns_to_check = ['comt_inhibitor', 'carbidopa_levodopa', 'anticholinergic', 'dopamine_agonist', 'amantadine',
                    'mao_b_inhibitor']

missing_data_count = df[columns_to_check].apply(lambda col: col.str.contains("Missing: Not provided")).sum()
totalCount = df['case_control'].count()

print(f"Total Count: {totalCount}")
print(f"Missing Data Count: {missing_data_count}")
print(f"Count without missing data: {totalCount - missing_data_count}")

H = []

for cols in bacteria.columns:
    pi = caseWithDisease['case_control'].count() / df['case_control'].str.contains('Case').sum()
    ln_pi = math.log1p(caseWithDisease['case_control'].count() / df['case_control'].str.contains('Case').sum())
    print(f"pi {cols} { pi }")
    print(f"ln(pi) {cols} {ln_pi }")
    print(f"pi * ln(pi) { cols } { pi * ln_pi }")
    H.append((caseWithDisease['case_control'].count() / df['case_control'].str.contains('Case').sum()) * (math.log1p(caseWithDisease['case_control'].count() / df['case_control'].str.contains('Case').sum())))
print(f"H = {sum(H)}")