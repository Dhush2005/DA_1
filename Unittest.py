import unittest
from Data_analysis import DataAnalysis


class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.path_to_datafile = 'C:/Users/gmdhu/PycharmProjects/PY_Project/Project_File.xlsx'
        self.year_range = [1978, 1987]
        self.included_countries = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
                          ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
                          ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
                          ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
        self.da = DataAnalysis(self.path_to_datafile, self.year_range, self.included_countries)
        self.df = self.da.parse_data()

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

    def test_get_top_3_countries(self):
        top_3 = self.da.get_top_3_countries()
        self.assertEqual(len(top_3), 3)
        self.assertTrue(all(country in self.included_countries for country in top_3.keys()))

    def test_display_total_visitors(self):
        # Test if the function produces a plot
        self.assertIsNone(self.da.display_total_visitors())


if __name__ == '__main__':
    unittest.main()