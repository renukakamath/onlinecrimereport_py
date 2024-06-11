/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - online_crime_py
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_crime_py` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_crime_py`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`station_id`,`description`,`datetime`,`status`) values 
(1,1,3,'descriptions..........','2022-08-22','on going');

/*Table structure for table `crime_types` */

DROP TABLE IF EXISTS `crime_types`;

CREATE TABLE `crime_types` (
  `crime_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_type_name` varchar(100) DEFAULT NULL,
  `minimum_penalty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crime_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `crime_types` */

insert  into `crime_types`(`crime_type_id`,`crime_type_name`,`minimum_penalty`) values 
(4,'crime','500'),
(5,'sdfgh','dfghj');

/*Table structure for table `crimes` */

DROP TABLE IF EXISTS `crimes`;

CREATE TABLE `crimes` (
  `crime_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_type_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `crime_title` varchar(100) DEFAULT NULL,
  `crime_description` varchar(100) DEFAULT NULL,
  `date_time_occurred` varchar(100) DEFAULT NULL,
  `date_time_reported` varchar(100) DEFAULT NULL,
  `crime_status` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crime_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `crimes` */

insert  into `crimes`(`crime_id`,`crime_type_id`,`station_id`,`crime_title`,`crime_description`,`date_time_occurred`,`date_time_reported`,`crime_status`,`place`,`dob`,`district`,`image`) values 
(6,4,3,'aaaa','mmm','2022-08-11T15:24','2022-08-13T15:24','pending','karanakodam','2022-08-12','mumbai','static/images/cd44ac51-5734-4ed1-a32a-b31149e298852..jfif');

/*Table structure for table `criminals` */

DROP TABLE IF EXISTS `criminals`;

CREATE TABLE `criminals` (
  `criminal_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `genter` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `photo` varchar(1000) DEFAULT NULL,
  `thumb_impression` varchar(100) DEFAULT NULL,
  `identification_mark1` varchar(100) DEFAULT NULL,
  `identification_mark2` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`criminal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `criminals` */

insert  into `criminals`(`criminal_id`,`first_name`,`last_name`,`genter`,`dob`,`photo`,`thumb_impression`,`identification_mark1`,`identification_mark2`,`address`,`father_name`,`place`,`district`) values 
(2,'renuka','kamath','male','mumbai','static/images/f31a81b6-762e-45ff-b3f5-f10642cf480f5.jfif','static/images/3fd1a835-6494-4c81-8397-0f210e4bfd662..jfif','nbfdahfa dsffad','kjkehja djhfkja','hggdjwad','jwodjq','ernakaulam','mumbai'),
(3,'renuka','kamath','female','2022-08-04','static/images/d52ee8fe-a32e-41d4-95f8-7e988dda18733..jfif','static/images/f35a990d-e013-4881-9532-c126233e9a562..jfif','nbfdahfa dsffad','kjkehja djhfkja','hggdjwad','jwodjq','ernakaulam','mumbai');

/*Table structure for table `evidences` */

DROP TABLE IF EXISTS `evidences`;

CREATE TABLE `evidences` (
  `evidence_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint_id` int(11) DEFAULT NULL,
  `file_path` varchar(1000) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`evidence_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `evidences` */

insert  into `evidences`(`evidence_id`,`complaint_id`,`file_path`,`description`,`datetime`) values 
(1,1,'static/images/f520c5c1-0637-4d81-ab9c-41ce6fad51471.jfif','descriptions..........','2022-08-23'),
(2,1,'static/images/3d2a642f-7858-427a-9a10-8ca5c2cc59241.jfif','qwertyvb','2022-08-23');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `fee_description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`fee_description`,`reply`,`datetime`) values 
(1,1,'bad','ok','2022-08-22');

/*Table structure for table `foundreport` */

DROP TABLE IF EXISTS `foundreport`;

CREATE TABLE `foundreport` (
  `fount_id` int(11) NOT NULL AUTO_INCREMENT,
  `criminal_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fount_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `foundreport` */

insert  into `foundreport`(`fount_id`,`criminal_id`,`user_id`,`place`,`datetime`,`description`) values 
(1,2,1,'ernakulam','2022-09-02T15:03','descriptions..........'),
(2,2,1,'ernakulam','2022-08-12T15:04','descriptions..........');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'renuka','12345','user'),
(2,'renuka','12345','user'),
(3,'renuka1','12345','user'),
(4,'admin','admin','admin'),
(5,'police','police','police'),
(6,'police1','police1','police'),
(7,'admin','123456','police');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `message_description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`message_id`,`user_id`,`message_description`,`reply`,`datetime`) values 
(1,1,'hello','pending','2022-08-23'),
(2,1,'hai','ok','2022-08-23'),
(3,1,'hello','pending','2022-08-23');

/*Table structure for table `stations` */

DROP TABLE IF EXISTS `stations`;

CREATE TABLE `stations` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `station_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fax_no` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`station_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `stations` */

insert  into `stations`(`station_id`,`login_id`,`station_name`,`place`,`district`,`pincode`,`phone`,`email`,`fax_no`) values 
(3,7,'shop2','ernakulam','ernakulam','682032','1234567890','renukakamath@gmail.com','1234567');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`address`,`place`,`pincode`,`phone`,`email`) values 
(1,3,'renuka','kamath','address','12345','682032','1234567890','address');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
