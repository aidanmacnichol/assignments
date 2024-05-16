# input_processing.py
# Aidan MacNichol, ENSF 692 P24

# No global variables are permitted

class Sensor:

    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    def update_status(self):
        """
        Prompts user to select what type of status update to perform.

        Raises:
            ValueError: Invalid input, accepts only 0, 1, 2, 3 as ints

        Returns:
            int: integer corresponding to what type of status update to do. 
        """
        print("Are changes are detected in the vision input?")
        # wait indefinitly for user input
        while True:
            try:
                # Prompt user and get input
                option = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
                # Only accepts 0, 1, 2, 3 ints. 
                if option in [0, 1, 2, 3]:
                    return option
                # Invalid input raise an exception
                else:
                    raise ValueError
            except ValueError:
                print("You must select either 1, 2, 3 or 0.")
    

    def update_traffic_light(self):
        """
        Update traffic light status.

        Raises:
            ValueError: Invalid input, only accepts "green" "yellow" or "red"
        """
        # Wait indefinitly for input
        while True:
            try:
                # Prompt user and get input
                status = input("What change has been identified?: ")
                # Only accepts "green", "yellow", or "red"
                if status in ["green", "yellow", "red"]:
                    self.traffic_light = status
                    break
                # Invalid input raise an exception
                else:
                    raise ValueError
            except ValueError:
                print("Invalid vision change.")


    def update_pedestrian(self):
        """
        Update pedestrian status.

        Raises:
            ValueError: Invalid input, only accepts "yes" or "no"
        """
        # Wait indefinitly for input
        while True:
            try:
                # prompt user and get input
                status = input("What change has been identified?: ")
                # Only accepts "yes" or "no" option
                if status in ["yes", "no"]:
                    self.pedestrian = status
                    break
                # Invalid input raise an exception
                else:
                    raise ValueError
            except ValueError:
                print("Invalid vision change.")


    def update_vehicle(self):
        """
        Update vehicle status.

        Raises:
            ValueError: Invalid input, only accepts case sensitive "yes" or "no"
        """
        while True:
            try:
                # prompt user and get input
                status = input("What change has been identified?: ")
                # Only accepts "yes" or "no" option
                if status in ["yes", "no"]:
                    self.vehicle = status
                    break
                # Invalid input raise an exception
                else:
                    raise ValueError
            except ValueError:
                print("Invalid vision change.")


def print_message(sensor):
    """
    Checks current status of traffic light, pedestrian and vehicle and checks conditional logic to get
    a output message, either "Proceed", "Caution" or "STOP"

    Args:
        sensor (Sensor): Sensor object
    """
    # Condition for "Proceed"
    if sensor.traffic_light == "green" and sensor.pedestrian == "no" and sensor.pedestrian == "no":
        message = "Proceed"
    # Condition for "Caution"
    elif sensor.traffic_light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        message = "Caution"
    # All other conditions result in "STOP"
    else:
        message = "STOP"
    
    # Print out info formatted to specifications
    print(f"\n{message}\n")
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .\n")


def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Create sensor object
    sensor = Sensor()
    # Wait infinitly for input
    while True:
        option = sensor.update_status()
        # option 0: terminate the program
        if option == 0:
            break
        # option 1: update traffic light
        elif option == 1:
            sensor.update_traffic_light()
        # option 2: update pedestrian
        elif option == 2:
            sensor.update_pedestrian()
        # option 3: update vehicle
        elif option == 3:
            sensor.update_vehicle()
        
        # print out message
        print_message(sensor)

if __name__ == '__main__':
    main()

