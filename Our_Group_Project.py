import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt


class DataAnalysis:
    def __init__(self, path_to_datafile, year_range, included_countries):
        self.df = pd.read_excel(path_to_datafile)
        self.year_range = year_range
        self.included_countries = included_countries

    def parse_data(self):
        # Step 1: (Parse data) Split year-month column to year and month separately
        df = self.df.copy()
        df = df.rename(columns={df.columns[0]: 'year_month'})
        # Remove whitespace from `year_month` and split into year and month
        df['year'] = df['year_month'].apply(lambda row: row.strip().split(' ')[0]).astype(int)
        df['month'] = df['year_month'].apply(lambda row: row.strip().split(' ')[1])

        # Step 2: replace na values
        df = df.replace([None, ' na '], 0)

        # Step 3: Identify data for computation
        # S/No=1 : 1978 - 1987
        # Filter data to contain only rows from 1978-1987
        start_year = int(self.year_range[0])
        end_year = int(self.year_range[1])
        df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

        # Filter data to contain only rows from Asia Region / Remove irrelevant countries
        df = df[self.included_countries]
        self.df = df
        return self.df

    def display_processed_data(self):
        print(self.df)

    def get_top_3_countries(self):
        countries_total = {}
        for country in self.included_countries:
            if country not in countries_total:
                countries_total[country] = self.df[country].sum()

        top_3 = OrderedDict(sorted(countries_total.items(), key=lambda kv: kv[1], reverse=True)[:3])
        return top_3

    def display_total_visitors(self):
        top_3 = self.get_top_3_countries()
        fig = plt.figure(figsize=(10, 5))
        plt.bar(top_3.keys(), top_3.values())
        plt.title(f'Top 3 countries with most visitors between years {self.year_range[0]} and {self.year_range[1]}')
        plt.ylabel('Total International Visitors (In millions)')
        plt.xlabel('Countries')
        plt.show()


def TestCase():
    # Test Case:
    path_to_datafile = 'C:/Users/gmdhu/PycharmProjects/PY_Project/Project_File.xlsx'  # Specify path to project_file
    year_range = [1978, 1987]  # Specify the assigned year range
    included_countries = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
                          ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
                          ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
                          ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']  # Specify the countries in the region that

    da = DataAnalysis(path_to_datafile, year_range, included_countries)
    da.parse_data()
    da.display_processed_data()
    da.display_total_visitors()


if __name__ == '__main__':
    TestCase()

