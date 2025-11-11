def extra_security(func):
    def wrapper():
        print("Before ridding the scooty")
        print("wear Helmet and ride")
        func()
        print("After riding the scooty")
        print("remove Helmet and park the vehicle at parking_lot")
    return wrapper()

@extra_security
def ride_Scooty():
    print("Successfully ride Scooty")


