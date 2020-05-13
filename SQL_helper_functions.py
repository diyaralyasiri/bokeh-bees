#-Script with helper functions to store incoming broadcasts to Database

import sqlite3

# SQLite DB Name
DB_Name = "Bee_Telemetry_Database.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def read_db_record(self, query):
		self.cur.execute(query)
		self.conn.commit()

		result = self.cur.fetchall()

		return result

	def __del__(self):
		self.cur.close()
		self.conn.close()



#===============================================================
# Functions to push Sensor Data into Database

def Store_Telemetry_Data(data):
	
	#Parse Data
	Data_and_Time = data['Date']
	Temperature = str(data['Temperature'])
	Humidity = str(data['Humidity'])
	Wieght = str(data['Wieght'])

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Telemetry_Data_Table (Timestamp, Temperature, Wieght, Humidity) values (?,?,?,?)",[Data_and_Time, Temperature, Wieght, Humidity])
	del dbObj
	print ("Inserted Telemetry Data into Database.")
	# print ("")

# # Function to save Temperature to DB Table
# def DHT11_Temp_Data_Handler(data):

# 	#Parse Data
# 	SensorID = data['Sensor_ID']
# 	Data_and_Time = data['Date']
# 	Temperature = str(data['Temperature'])
# 	# print('Sensor ID type ' + str(type(SensorID)))
# 	# print('d&t type ' + str(type(Data_and_Time)))
# 	# print('Temp type ' + str(type(Temperature)))

# 	#Push into DB Table
# 	dbObj = DatabaseManager()
# 	dbObj.add_del_update_db_record("insert into DHT11_Temperature_Data (SensorID, Date_n_Time, Temperature) values (?,?,?)",[SensorID, Data_and_Time, Temperature])
# 	del dbObj
# 	print ("Inserted Temperature Data into Database.")
# 	print ("")

# # Function to save Humidity to DB Table
# def DHT11_Humidity_Data_Handler(data):
# 	#Parse Data
# 	SensorID = data['Sensor_ID']
# 	Data_and_Time = data['Date']
# 	Humidity = str(data['Humidity'])
# 	# print('Sensor ID type ' + str(type(SensorID)))
# 	# print('d&t type ' + str(type(Data_and_Time)))
# 	# print('Humidty type ' + str(type(Humidity)))

# 	#Push into DB Table
# 	dbObj = DatabaseManager()
# 	dbObj.add_del_update_db_record("insert into DHT11_Humidity_Data (SensorID, Date_n_Time, Humidity) values (?,?,?)",[SensorID, Data_and_Time, Humidity])
# 	del dbObj
# 	print ("Inserted Humidity Data into Database.")
# 	print ("")

#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic
# def sensor_Data_Handler(Topic, data):
# 	#print('Entered Data handler master')

# 	if Topic == "Diyar/Bee/DHT11/Temperature":
# 		DHT11_Temp_Data_Handler(data)
# 	elif Topic == "Diyar/Bee/DHT11/Humidity":
# 		DHT11_Humidity_Data_Handler(data)
	
	
#===============================================================

