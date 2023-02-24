import unittest
from Data_analysis import DataAnalyticsUtils

class TestDataAnalyticsUtils(unittest.TestCase):
    def test_year_range(self):
        path_to_datafile = 'Project_File.xlsx' # Specify path to project_file
        year_range = [1978, 1987] # Specify the assigned year range
        included_countries = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
                                ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
                                ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
                                ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE '] # Specify the countries in the region that are contained in the project_file

        DA = DataAnalyticsUtils(path_to_datafile, year_range, included_countries)
        self.assertEqual(DA.get_year_range()[0], 1978)    # Check if year_start is right
        self.assertEqual(DA.get_year_range()[1], 1987)    # Check if year_end is right

if __name__ == '__main__':
    unittest.main()