"""
Connect to autopilot via serial ocmmunication
"""

from pymavlink import mavutil
import time
import sys

master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
master.reboot_autopilot()
master.wait_heartbeat()

message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'].decode("utf-8"), message['param_value']))

'''
master.mav.param_request_list_send(
	master.target_system, master.target_component
)
while True:
	msg = master.recv_match()
	if not msg:
		continue
	if msg.get_type() == 'HEARTBEAT':
		print("\n\n*****Got message: %s*****" % msg.get_type())
		print("Message: %s" % msg)

	if msg.get_type() == 'GPS_RAW':
		print("\n\n*****Got message: %s*****" % msg.get_type())
		print("Message: %s" % msg)
		#print("\nAs dictionary: %s" % msg.to_dict())
		# Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
		#print("\nSystem status: %s" % msg.system_status)
'''