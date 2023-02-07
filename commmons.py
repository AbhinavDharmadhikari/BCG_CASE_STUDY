import pandas as pd
import common_details
class dataframe:
    """
    Provide all the csv as a dataframe by reading the csv through pandas
    """
    def charges_use(path):
        path = path + "\{0}".format(common_details.charges_use_name)
        df = pd.read_csv(path)
        return df
    def damages_use(path):
        path = path + "\{0}".format(common_details.damages_use_name)
        df = pd.read_csv(path)
        return df

    def endorse_use(path):
        path = path + "\{0}".format(common_details.endorse_use_name)
        df = pd.read_csv(path)
        return df
    def primary_person_use(path):
        path = path + "\{0}".format(common_details.primary_person_use_name)
        df = pd.read_csv(path)
        return df
    def restrict_use(path):
        path = path + "\{0}".format(common_details.restrict_use_name)
        df = pd.read_csv(path)
        return df
    def units_use(path):
        path = path + "\{0}".format(common_details.units_use_name)
        df = pd.read_csv(path,low_memory=False)
        return df
