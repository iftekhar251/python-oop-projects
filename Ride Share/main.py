from ride import RideSharing,Ride,RideRequest,RideMatching
from users import Rider,Driver
from vehicle import Car,Bike

niye_jao=RideSharing("Niye jao")
rahim=Rider("Rahim uddin","rahim2@gamil.com",1245,"banani",500)
niye_jao.add_rider(rahim)
karim=Driver("karim uddin","karim22@gamil.com",145245,"gulshan")
niye_jao.add_driver(karim)
rahim.request_ride(niye_jao,"uttara","car")
rahim.show_current_ride()
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
#print(niye_jao)