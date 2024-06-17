# calgary_dogs.py
# Aidan MacNichol
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd 
import numpy as np 

class DogBreedAnalyzer:
    
    def __init__(self, file_path = "CalgaryDogBreeds.xlsx"):
        self.df = pd.read_excel(file_path)
        # It looks like they are already uppercase but this is good practice regardless
        self.df['Breed'] = self.df['Breed'].str.upper()
        
    def get_breed_data(self, breed):
        # Standardize input
        breed = breed.upper()
        # Raise error if breed not found
        if breed not in self.df['Breed'].values:
            raise KeyError('Dog breed not found in the data. Please try again.')
        # Filter the dataframe for only breed values
        breed_data = self.df[self.df["Breed"] == breed]
        return breed_data
    
    
    def analyze_breed_data(self, breed):
        """
        Method to tie everything together and print statistics. See individual functions for explanation.

        Args:
            breed (str): Breed name.
        """
        # Load Breed data
        breed = breed.upper()
        breed_data = self.get_breed_data(breed)
        
        # 1. Get all the unique years breed is listed
        self.print_unique_years(breed, breed_data)

        # 2. Get total num of registrations for breed
        self.print_registration_total(breed, breed_data)
        
        # 3. Print yearly percentage stats
        self.print_year_registration_percentage(breed, breed_data)
        
        # 4. Print total percentage stat
        self.print_total_regestration_percentage(breed, breed_data)
        
        # 5. Find months with most registration. Print ties
        self.print_popular_months(breed, breed_data)
        
        
    def print_unique_years(self, breed, breed_data):
        """
        Prints the number of unique years the specified breed was listed in

        Args:
            breed (str): Breed name.
            breed_data (df): Associated data with specified breed.
        """
        # 1. Get all the unique years breed is listed
        years = breed_data["Year"].unique()
        # Print out years using fancy map to iterate through array of strings 
        print(f"The {breed} was found in the top breeds for years: {', '.join(map(str, years))}")
    
    
    def print_registration_total(self, breed, breed_data):
        """
        Print total number of registrations across all years

        Args:
            breed (str): Breed name.
            breed_data (df): Associated data with specified breed.
        """
        # 2. Get total num of registrations for breed by summing up relevant data
        reg_total = breed_data["Total"].sum()
        print(f"There have been {reg_total} {breed} dogs registered total.")
        
        
    def print_year_registration_percentage(self, breed, breed_data):
        """
        Prints what percentage of specified breed registration compared to the total 
        dataset for each year (2021, 2022, 2023).

        Args:
            breed (str): Breed name.
            breed_data (df): Associated data with specified breed.
        """
        # Repeat for each of the three years
        for year in [2021, 2022, 2023]:
            # Get year total for specified breed
            breed_total = breed_data[breed_data["Year"] == year]["Total"].sum()
            # Get all breeds total for specified year
            total = self.df[self.df["Year"] == year]["Total"].sum()
            # Calculate the percentage
            percentage = (breed_total / (total)) * 100
            # Print result (rounded to 6 decimal places) 
            print(f"The {breed} was {round(percentage, 6)}% of the top breeds in {year}.")
    
        
    def print_total_regestration_percentage(self, breed, breed_data):
        """
        Print what percentage of a specified breed compored to the total dataset over all years.

        Args:
            breed (str): Breed name.
            breed_data (df): Associated data with specified breed.
        """
        # Sum registration counts over breed dataset
        breed_total = breed_data["Total"].sum()
        # Sum registration counts over entire data set
        total = self.df["Total"].sum()
        # Calculate percentage
        percentage = (breed_total / total) * 100
        # Print result
        print(f"The {breed} was {round(percentage, 6)}% of the top breeds across all years.")


    def print_popular_months(self, breed, breed_data):
        # Get the number of times each month shows up for given breed data
        month_frequency = breed_data["Month"].value_counts() 
        # Get only the maximum value (will also get ties)
        popular_months = month_frequency[month_frequency == month_frequency.max()]
        # Get the month name and convert to a list
        popular_months = popular_months.index.tolist()
        # Print result
        print(f"Most popular month(s) for {breed} dogs: {' '.join(popular_months)}")
        
def main():
    print("ENSF 692 Dogs of Calgary")
    # Create object
    analyzer = DogBreedAnalyzer("CalgaryDogBreeds.xlsx")
    # Continually ask for user input
    while True:
        try:
            user_input = input("Please enter a dog breed: ")
            analyzer.analyze_breed_data(user_input)
            # End program upon succesful execution
            break
        # Where a invalid user input is caught
        except KeyError as e:
            print(e)
    

if __name__ == '__main__':
    main()
