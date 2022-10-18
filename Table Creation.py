import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database="samplevideo_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS `user_details` (`user_id` int(11) NOT NULL AUTO_INCREMENT,`username` varchar(255) DEFAULT NULL,`first_name` varchar(50) DEFAULT NULL,`last_name` varchar(50) DEFAULT NULL,`gender` varchar(10) DEFAULT NULL,`password` varchar(50) DEFAULT NULL,`status` tinyint(10) DEFAULT NULL,PRIMARY KEY (`user_id`)) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
