import dronekit
import time

vehicle = dronekit.connect("/dev/ttyAMA0", baud=57600)
print("connecting to vehicle on %s" % vehicle)

print ("Get some vehicle attribute values:")
print ("GPS: %s" % vehicle.gps_0)
print ("Battery: %s" % vehicle.battery)
print ("Last heartbeat: %s" % vehicle.last_heartbeat)

while True:
  loc = vehicle.location.global_frame
  coords = (loc.lat, loc.lon)
  print(f"GPS: ({loc.lat}, {loc.lon})")
  time.sleep(1)

vehicle.close()
print("Complete")
