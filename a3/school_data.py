# school_data.py
# Aidan MacNichol
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# (year, school, grade)

class HighSchoolData():
    """
    One class to print and calculate any school statistics needed for this assignment.

    Variables:
        school_names (npArray): Array containing all school names in order of lowest to highest code
        school_codes (npArray): Array containing all school codes in order of lowest to highest code
        data_list (dict): Dictionary containing year as key and the data for that year as the value
    """

    # Array of school names - arranged in same order as schoolCodes (lowest to highest numerical value)
    school_names = np.array(["Centennial High School",
                            "Robert Thirsk School",
                            "Louise Dean School",
                            "Queen Elizabeth High School",
                            "Forest Lawn High School",
                            "Crescent Heights High School",
                            "Western Canada High School",
                            "Central Memorial High School",
                            "James Fowler High School",
                            "Ernest Manning High School",
                            "William Aberhart High School",
                            "National Sport School",
                            "Henry Wise Wood High School",
                            "Bowness High School",
                            "Lord Beaverbrook High School",
                            "Jack James High School",
                            "Sir Winston Churchill High School",
                            "Dr. E. P. Scarlett High School",
                            "John G Diefenbaker High School",
                            "Lester B. Pearson High School"])
    
    # School codes in ascending numerical order
    school_codes = np.array(["1224", "1679", "9626", "9806", "9813", "9815", 
                            "9816", "9823", "9825", "9826", "9829", "9830", 
                            "9836", "9847", "9850", "9856", "9857", "9858", "9860", "9865"])
    
    # List of data for each year
    data_list = {2013:year_2013, 2014:year_2014, 2015:year_2015, 2016:year_2016, 2017:year_2017, 2018:year_2018, 2019:year_2019, 2020:year_2020, 
                2021:year_2021, 2022:year_2022}

    def __init__(self):
        self.load_data()


    def load_data(self):
        """
        Loads highschool enrollment data into a 3D array with shape: (year, school, grade)
        """
        reshaped_data = []
        for year, data in self.data_list.items():
            reshaped_data.append(data.reshape(20,3))
        self.data = np.stack(reshaped_data, axis=0)


    def print_shape(self):
        """
        Prints the shape of the full data array. 

        Returns:
            npArray: shape of array.
        """
        return self.data.shape


    def get_dimensions(self):
        """
        Gets the number of dimensions of the full data array.

        Returns:
            int: Number of dimensions. 
        """
        return self.data.ndim
    

    def get_school_data(self, school_identifier):
        """
        Given a school code or name of school returns all of the enrollment data in the shape (year, grade)

        Args:
            school_identifier (int or string): Either a 4 digit school code or school name as a string

        Raises:
            ValueError: School code or name was not found

        Returns:
            npArray[int, int]: 2D array where the rows are the year and collumns are grade
        """
        # Make sure school code exists
        if school_identifier in self.school_codes:
            # get index of data array corresponding to the school code
            idx = np.where(self.school_codes == school_identifier)[0][0]
            # return all years and grades for given school index
            return self.data[:,idx,:]
        # Make sure school name exists if code not found
        elif school_identifier in self.school_names:
            # get index of array corresponding to school name
            idx = np.where(self.school_names == school_identifier)[0][0]
            return self.data[:,idx,:]
        else:
            raise ValueError("You must enter a valid school name or code.")
    
    def print_school_stats(self, school_identifier):
        """
        Given school data from "get_school_data()" calculates the following statistics:
        1. School name and code
        2. Mean enrollment for Grade 10 across all years
        3. Mean enrollment for Grade 11 across all years
        4. Mean enrollment for Grade 12 across all years
        5. Highest enrollment for a single grade within the entire time period
        6. Lowest enrollment for a single grade within the entire time period
        7. Total enrollment for each year from 2013 to 2022
	    8. Total ten year enrollment
	    9. Mean total yearly enrollment over 10 years
        10. Finds where enrollment numbers are over 500 and calculates the median value for the 500 enrollments

        Args:
            school_identifier (int or string) Either a 4 digit school code or school name as a string
        """
        # Get given school data
        data = self.get_school_data(school_identifier)
        # 1. Print school info (if given code get name and vice versa)
        if school_identifier in self.school_codes:
            name = self.school_names[np.where(self.school_codes == school_identifier)[0][0]]
            code = school_identifier
        elif school_identifier in self.school_names:
            code = self.school_codes[np.where(self.school_names == school_identifier)[0][0]]
            name = school_identifier
        # Should never get here but safe coding regardless :)
        else:
            raise ValueError("Invalid school identifier")

        print(f"School Name: {name}, School Code: {code}")
        # 2. Print mean enrollment for grade 10
        print(f"Total enrollment for Grade 10: {int(np.nanmean(data[:,0]))}")
        # 3. Print mean enrollment for grade 11
        print(f"Total enrollment for Grade 11: {int(np.nanmean(data[:,1]))}")
        # 4. Print mean enrollment for grade 12
        print(f"Total enrollment for Grade 12: {int(np.nanmean(data[:,2]))}")
        # 5. Print highest enrollment 
        print(f"Highest enrollment for a single grade: {int(np.nanmax(data))}")
        # 6. Print lowest enrollment
        print(f"Lowest enrollment for a single grade: {int(np.nanmin(data))}")
        # 7. Print total enrollment data
        idx = 0
        # Loop indexed weird so that it is easier to print
        for i in range(2013, 2023):
            print(f"Total enrollment for {i}: {int(np.nansum(data[idx, :]))}")
            idx += 1
        # 8. Print total ten year enrollment
        print(f"Total ten year enrollment: {int(np.nansum(data))}")
        # 9. Mean Total yearly enrollment over 10 years (sum all grades for each year than take mean over entire time period)
        sum = np.nansum(data, axis=1)
        print(f"Mean total enrollment over 10 years: {int(np.nanmean(sum))}")
        # 10. Median value of years where enrollment is over 500
        median = self.find_high_enrollment(data)
        # If not None       
        if median:
            print(f"For all enrollments over 500, the median value was: {int(self.find_high_enrollment(data))}")
        else:
            print(f"No enrollments over 500.")
    

    def find_high_enrollment(self, data):
        """
        Finds where enrollment is over 500 and calculates the median value for the 500 enrollments

        Args:
            data (npArray): Array of school enrollment numbers (year, grade)
        
        Returns:
            double: Median value. None if there are no values greater than 500
        """
        # use a mask to find values greater than 500
        mask = data > 500
        # return None if there is no enrollment above 500
        if data[mask].size == 0:
            return None
        else:
            return np.nanmedian(data[mask])
    

    def print_general_stats(self):
        """
        Prints overall statistics for the entire dataset.
        1. mean enrollment in 2013
        2. mean enrollment in 2022
        3. Total graduating class of 2022 across all schools
        4. Highest enrollment for a single grade (all schools entire time period)
        5. Lowest enrollment for a single grade (all schools entire time period)
        """
        # 1. mean enrollment in 2013
        print(f"Mean enrollment in 2013: {int(np.nanmean(self.data_list[2013]))}")
        # 2. mean enrollment in 2022
        print(f"Mean enrollment in 2022: {int(np.nanmean(self.data_list[2022]))}")
        # 3. total graduating class of 2022 across all schools
        year = self.data_list[2022].reshape(20,3)
        print(f"Total graduating class of 2022: {int(np.nansum(year[:, 2]))}")
        # 4. Highest enrollment for a single grade (all schools entire time period)
        # loop through dict of year statistics and find max
        print(f"Highest enrollment for a single grade: {int(np.nanmax([np.nanmax(data) for data in self.data_list.values()]))}")
        # 5. Lowest enrollment for a single grade (all schools entire time period)
        print(f"Highest enrollment for a single grade: {int(np.nanmin([np.nanmin(data) for data in self.data_list.values()]))}")


def main():
    print("ENSF 692 School Enrollment Statistics")
    # Print Stage 1 requirements here
    hsd = HighSchoolData()
    print(f"Shape of full data array: {hsd.print_shape()}")
    print(f"Dimensions of full data array: {hsd.get_dimensions()}")

    # Prompt for user input
    school_identifier = input("Please enter the high school name or school code: ")

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    hsd.print_school_stats(school_identifier)

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    hsd.print_general_stats()

if __name__ == '__main__':
    main()
