import sys

import commmons
import common_details
import pandas as pd
class testcases:
    def test_case1():
        df = commmons.dataframe.primary_person_use(common_details.path)
        df_female = df[df['PRSN_GNDR_ID']=='FEMALE']
        df_female_killed = df_female[df_female['PRSN_INJRY_SEV_ID']=='KILLED']
        number =  df_female_killed.shape[0]
        return "Number of females killed are : {0}".format(number)

    def test_case2():
        df = commmons.dataframe.units_use(common_details.path)
        df_2_v = df[df['VEH_BODY_STYL_ID']=='MOTORCYCLE']

        number =  df_2_v.shape[0]
        return "Number of two wheelers are booked for crashes : {0}".format(number)

    def test_case3():
        df = commmons.dataframe.primary_person_use(common_details.path)
        df_female = df[df['PRSN_GNDR_ID']=='FEMALE']
        # df_final = df_female.groupby(['DRVR_LIC_STATE_ID'])['CRASH_ID'].count()
        # df_final = df_final.to_frame(name = ['state','count'])
        df2 = df_female.groupby(['DRVR_LIC_STATE_ID'])['CRASH_ID'].agg('count').reset_index()
        # number =  df_2_v.shape[0]
        df2 = df2.sort_values(by=['CRASH_ID'], ascending=False)
        return "The state with highest number accidents where females " \
               "were involved is {0} and the count is {1}".format(df2.iloc[0][0],df2.iloc[0][1])

    def test_case4():
        df1 = commmons.dataframe.primary_person_use(common_details.path)
        df2 = commmons.dataframe.units_use(common_details.path)

        df_temp = pd.merge(df1,df2[['CRASH_ID','VEH_MAKE_ID']], how = 'inner')
        df_temp_2 = df_temp.groupby(['VEH_MAKE_ID'])['CRASH_ID'].agg('count').reset_index()
        df_temp_2 = df_temp_2.sort_values(by=['CRASH_ID'], ascending=False)
        df_temp_2 = df_temp_2.iloc[5:16]
        return df_temp_2
    def test_case5():
        df1 = commmons.dataframe.primary_person_use(common_details.path)
        df2 = commmons.dataframe.units_use(common_details.path)

        df_temp = pd.merge(df1,df2[['CRASH_ID','VEH_BODY_STYL_ID']], how = 'inner')
        df_temp_2 = df_temp.groupby(['VEH_BODY_STYL_ID','PRSN_ETHNICITY_ID'])['CRASH_ID'].agg('count').reset_index()
        df_temp_2 = df_temp_2.sort_values(by=['CRASH_ID'], ascending=False)
        df_temp_2["rank"] = df_temp_2.groupby("VEH_BODY_STYL_ID")["CRASH_ID"].rank(method="dense", ascending=False)
        ranked = [1,2,3,4,5]
        df_temp_2['rank'] = df_temp_2['rank'].astype('int')
        df_temp_2 = df_temp_2[df_temp_2['rank'].isin(ranked)]
        return df_temp_2

    def test_case6():
        df1 = commmons.dataframe.primary_person_use(common_details.path)
        df2 = commmons.dataframe.units_use(common_details.path)
        df2 = df2.fillna('')
        df2['concated_contribution'] = df2['CONTRIB_FACTR_1_ID'] +df2['CONTRIB_FACTR_2_ID'] +df2['CONTRIB_FACTR_P1_ID']
        #
        df_temp = pd.merge(df1,df2[['CRASH_ID','concated_contribution']], how = 'inner')
        df_temp = df_temp[['concated_contribution','DRVR_ZIP']]
        df_temp = df_temp.loc[df_temp['concated_contribution'].str.contains("alcohol", case=False)]

        df_temp_2 = df_temp.groupby(['DRVR_ZIP'])['concated_contribution'].agg('count').reset_index()
        df_temp_2 = df_temp_2.sort_values(by=['concated_contribution'], ascending=False)
        return df_temp_2.head(1)

if __name__ == '__main__':
    input_str = sys.argv[1]
    if input_str == 'test_case_1':
        testcases.test_case1()
    elif input_str == 'test_case_2':
        testcases.test_case2()
    elif input_str == 'test_case_3':
        testcases.test_case3()
    elif input_str == 'test_case_4':
        testcases.test_case4()
    elif input_str == 'test_case_5':
        testcases.test_case5()
    elif input_str == 'test_case_6':
        testcases.test_case6()
    else:
        pass