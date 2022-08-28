/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : nzoly

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 24/08/2022 18:08:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for event_stage
-- ----------------------------
DROP TABLE IF EXISTS `event_stage`;
CREATE TABLE `event_stage`  (
  `StageID` int(0) NOT NULL AUTO_INCREMENT,
  `StageName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `EventID` int(0) NOT NULL,
  `Location` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `StageDate` date NOT NULL,
  `Qualifying` tinyint(1) NOT NULL,
  `PointsToQualify` float NULL DEFAULT NULL,
  PRIMARY KEY (`StageID`) USING BTREE,
  INDEX `EventID`(`EventID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 382 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of event_stage
-- ----------------------------
INSERT INTO `event_stage` VALUES (356, 'Heat 1', 3, 'Shougang', '2022-02-14', 1, 127.5);
INSERT INTO `event_stage` VALUES (357, 'Final', 3, 'Shougang', '2022-02-15', 0, NULL);
INSERT INTO `event_stage` VALUES (377, 'Heat 1', 1, 'Genting Snow Park', '2022-02-05', 1, NULL);
INSERT INTO `event_stage` VALUES (379, 'Final', 1, 'Genting Snow Park', '2022-02-06', 0, NULL);
INSERT INTO `event_stage` VALUES (281, 'Qualification', 7, 'Genting Snow Park', '2022-02-14', 1, 63.5);
INSERT INTO `event_stage` VALUES (289, 'Qualification', 11, 'Genting Snow Park', '2022-02-17', 1, 70);
INSERT INTO `event_stage` VALUES (290, 'Final', 11, 'Genting Snow Park', '2022-02-19', 0, NULL);

-- ----------------------------
-- Table structure for event_stage_results
-- ----------------------------
DROP TABLE IF EXISTS `event_stage_results`;
CREATE TABLE `event_stage_results`  (
  `ResultID` int(0) NOT NULL AUTO_INCREMENT,
  `StageID` int(0) NOT NULL,
  `MemberID` int(0) NOT NULL,
  `PointsScored` float NOT NULL,
  `Position` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ResultID`) USING BTREE,
  INDEX `StageID`(`StageID`) USING BTREE,
  INDEX `MemberID`(`MemberID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 579 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of event_stage_results
-- ----------------------------
INSERT INTO `event_stage_results` VALUES (467, 356, 5634, 176.5, NULL);
INSERT INTO `event_stage_results` VALUES (538, 357, 5634, 177, 2);
INSERT INTO `event_stage_results` VALUES (567, 377, 5634, 86.75, NULL);
INSERT INTO `event_stage_results` VALUES (577, 379, 5634, 92.88, 1);
INSERT INTO `event_stage_results` VALUES (265, 281, 5632, 54.93, NULL);
INSERT INTO `event_stage_results` VALUES (222, 289, 5633, 90.5, NULL);
INSERT INTO `event_stage_results` VALUES (223, 290, 5633, 94, 1);
INSERT INTO `event_stage_results` VALUES (224, 356, 5629, 172.5, NULL);

-- ----------------------------
-- Table structure for events
-- ----------------------------
DROP TABLE IF EXISTS `events`;
CREATE TABLE `events`  (
  `EventID` int(0) NOT NULL AUTO_INCREMENT,
  `EventName` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Sport` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `NZTeam` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`EventID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of events
-- ----------------------------
INSERT INTO `events` VALUES (1, 'Slopestyle', 'Snowboarding', 101);
INSERT INTO `events` VALUES (3, 'Big Air', 'Snowboarding', 101);
INSERT INTO `events` VALUES (5, 'Men\'s Halfpipe', 'Freestyle Skiing', 103);
INSERT INTO `events` VALUES (6, 'Men\'s 20 km individual biathlon', 'Biathlon', 123);
INSERT INTO `events` VALUES (7, 'Women\'s slopestyle', 'Freestyle Skiing', 103);
INSERT INTO `events` VALUES (11, 'Men\'s Halfpipe', 'Snowboarding', 101);
INSERT INTO `events` VALUES (13, 'aaa1', 'bbb2', 103);

-- ----------------------------
-- Table structure for members
-- ----------------------------
DROP TABLE IF EXISTS `members`;
CREATE TABLE `members`  (
  `MemberID` int(0) NOT NULL AUTO_INCREMENT,
  `TeamID` int(0) UNSIGNED NOT NULL,
  `FirstName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `LastName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `City` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `Birthdate` date NOT NULL,
  `Type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'user',
  PRIMARY KEY (`MemberID`) USING BTREE,
  INDEX `TeamID`(`TeamID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 5641 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of members
-- ----------------------------
INSERT INTO `members` VALUES (5629, 101, 'Ben', 'Barclay', 'Auckland', '2002-02-04', 'user');
INSERT INTO `members` VALUES (5630, 103, 'Anja', 'Barugh', 'Morrinsville', '1999-05-21', 'user');
INSERT INTO `members` VALUES (5631, 103, 'Finn', 'Bilous', 'Wanaka', '1999-09-22', 'user');
INSERT INTO `members` VALUES (5632, 103, 'Margaux', 'Hackett', 'Wanaka', '1999-06-02', 'user');
INSERT INTO `members` VALUES (5633, 103, 'Nico', 'Porteous', 'Hamilton', '2001-11-23', 'user');
INSERT INTO `members` VALUES (5634, 101, 'Zoi', 'Sadowski-Synnott', 'Wanaka', '2001-03-06', 'user');
INSERT INTO `members` VALUES (5635, 101, 'Tiarn', 'Collins', 'Queenstown', '1999-11-09', 'user');
INSERT INTO `members` VALUES (5636, 125, 'Peter', 'Michael', 'Wellington', '1989-05-09', 'user');
INSERT INTO `members` VALUES (5637, 123, 'Campbell', 'Wright', 'Rotorua', '2002-05-25', 'user');
INSERT INTO `members` VALUES (5638, 0, '', 'admin', 'Wanaka', '2022-08-10', 'admin');

-- ----------------------------
-- Table structure for teams
-- ----------------------------
DROP TABLE IF EXISTS `teams`;
CREATE TABLE `teams`  (
  `TeamID` int(0) NOT NULL AUTO_INCREMENT,
  `TeamName` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`TeamID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 127 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teams
-- ----------------------------
INSERT INTO `teams` VALUES (101, 'Snowboard');
INSERT INTO `teams` VALUES (103, 'Freestyle Skiing');
INSERT INTO `teams` VALUES (123, 'Biathlon');
INSERT INTO `teams` VALUES (102, 'Alpine Skiing');
INSERT INTO `teams` VALUES (125, 'Speed Skating');

-- ----------------------------
-- View structure for event_stage_results_view
-- ----------------------------
DROP VIEW IF EXISTS `event_stage_results_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `event_stage_results_view` AS select `event_stage_results`.`ResultID` AS `ResultID`,`event_stage_results`.`MemberID` AS `MemberID`,`event_stage_results`.`PointsScored` AS `PointsScored`,`event_stage`.`StageName` AS `StageName`,`event_stage`.`StageDate` AS `StageDate`,`events`.`EventName` AS `EventName`,`event_stage`.`Qualifying` AS `Qualifying`,`event_stage`.`PointsToQualify` AS `PointsToQualify`,`event_stage`.`Location` AS `Location`,`event_stage_results`.`Position` AS `Position`,`event_stage_results`.`StageID` AS `StageID`,`events`.`Sport` AS `Sport`,`events`.`NZTeam` AS `NZTeam`,`event_stage`.`EventID` AS `EventID`,concat(`members`.`FirstName`,' ',`members`.`LastName`) AS `Name`,`teams`.`TeamName` AS `TeamName`,`members`.`TeamID` AS `TeamID` from ((((`event_stage_results` left join `event_stage` on((`event_stage_results`.`StageID` = `event_stage`.`StageID`))) join `events` on((`event_stage`.`EventID` = `events`.`EventID`))) join `members` on((`event_stage_results`.`MemberID` = `members`.`MemberID`))) join `teams` on((`members`.`TeamID` = `teams`.`TeamID`)));

-- ----------------------------
-- Records of teams
-- ----------------------------
INSERT INTO `teams` VALUES (467, 5634, 176.5, 'Heat 1', '2022-02-14', 'Big Air', 1, 127.5, 'Shougang', NULL, 356, 'Snowboarding', 101, 3, 'Zoi Sadowski-Synnott', 'Snowboard', 101);
INSERT INTO `teams` VALUES (538, 5634, 177, 'Final', '2022-02-15', 'Big Air', 0, NULL, 'Shougang', 2, 357, 'Snowboarding', 101, 3, 'Zoi Sadowski-Synnott', 'Snowboard', 101);
INSERT INTO `teams` VALUES (567, 5634, 86.75, 'Heat 1', '2022-02-05', 'Slopestyle', 1, NULL, 'Genting Snow Park', NULL, 377, 'Snowboarding', 101, 1, 'Zoi Sadowski-Synnott', 'Snowboard', 101);
INSERT INTO `teams` VALUES (577, 5634, 92.88, 'Final', '2022-02-06', 'Slopestyle', 0, NULL, 'Genting Snow Park', 1, 379, 'Snowboarding', 101, 1, 'Zoi Sadowski-Synnott', 'Snowboard', 101);
INSERT INTO `teams` VALUES (265, 5632, 54.93, 'Qualification', '2022-02-14', 'Women\'s slopestyle', 1, 63.5, 'Genting Snow Park', NULL, 281, 'Freestyle Skiing', 103, 7, 'Margaux Hackett', 'Freestyle Skiing', 103);
INSERT INTO `teams` VALUES (222, 5633, 90.5, 'Qualification', '2022-02-17', 'Men\'s Halfpipe', 1, 70, 'Genting Snow Park', NULL, 289, 'Snowboarding', 101, 11, 'Nico Porteous', 'Freestyle Skiing', 103);
INSERT INTO `teams` VALUES (223, 5633, 94, 'Final', '2022-02-19', 'Men\'s Halfpipe', 0, NULL, 'Genting Snow Park', 1, 290, 'Snowboarding', 101, 11, 'Nico Porteous', 'Freestyle Skiing', 103);
INSERT INTO `teams` VALUES (224, 5629, 172.5, 'Heat 1', '2022-02-14', 'Big Air', 1, 127.5, 'Shougang', NULL, 356, 'Snowboarding', 101, 3, 'Ben Barclay', 'Snowboard', 101);

-- ----------------------------
-- View structure for event_stage_view
-- ----------------------------
DROP VIEW IF EXISTS `event_stage_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `event_stage_view` AS select `event_stage`.`StageID` AS `StageID`,`event_stage`.`StageName` AS `StageName`,`event_stage`.`EventID` AS `EventID`,`event_stage`.`Location` AS `Location`,`event_stage`.`StageDate` AS `StageDate`,`event_stage`.`Qualifying` AS `Qualifying`,`event_stage`.`PointsToQualify` AS `PointsToQualify`,`events`.`EventName` AS `EventName`,`events`.`Sport` AS `Sport`,`events`.`NZTeam` AS `NZTeam`,`teams`.`TeamName` AS `TeamName` from ((`event_stage` join `events` on((`event_stage`.`EventID` = `events`.`EventID`))) join `teams` on((`events`.`NZTeam` = `teams`.`TeamID`)));

-- ----------------------------
-- Records of teams
-- ----------------------------
INSERT INTO `teams` VALUES (356, 'Heat 1', 3, 'Shougang', '2022-02-14', 1, 127.5, 'Big Air', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (357, 'Final', 3, 'Shougang', '2022-02-15', 0, NULL, 'Big Air', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (377, 'Heat 1', 1, 'Genting Snow Park', '2022-02-05', 1, NULL, 'Slopestyle', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (379, 'Final', 1, 'Genting Snow Park', '2022-02-06', 0, NULL, 'Slopestyle', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (281, 'Qualification', 7, 'Genting Snow Park', '2022-02-14', 1, 63.5, 'Women\'s slopestyle', 'Freestyle Skiing', 103, 'Freestyle Skiing');
INSERT INTO `teams` VALUES (289, 'Qualification', 11, 'Genting Snow Park', '2022-02-17', 1, 70, 'Men\'s Halfpipe', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (290, 'Final', 11, 'Genting Snow Park', '2022-02-19', 0, NULL, 'Men\'s Halfpipe', 'Snowboarding', 101, 'Snowboard');

-- ----------------------------
-- View structure for events_view
-- ----------------------------
DROP VIEW IF EXISTS `events_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `events_view` AS select `events`.`EventID` AS `EventID`,`events`.`EventName` AS `EventName`,`events`.`Sport` AS `Sport`,`events`.`NZTeam` AS `NZTeam`,`teams`.`TeamName` AS `TeamName` from (`events` join `teams` on((`events`.`NZTeam` = `teams`.`TeamID`)));

-- ----------------------------
-- Records of teams
-- ----------------------------
INSERT INTO `teams` VALUES (1, 'Slopestyle', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (3, 'Big Air', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (5, 'Men\'s Halfpipe', 'Freestyle Skiing', 103, 'Freestyle Skiing');
INSERT INTO `teams` VALUES (6, 'Men\'s 20 km individual biathlon', 'Biathlon', 123, 'Biathlon');
INSERT INTO `teams` VALUES (7, 'Women\'s slopestyle', 'Freestyle Skiing', 103, 'Freestyle Skiing');
INSERT INTO `teams` VALUES (11, 'Men\'s Halfpipe', 'Snowboarding', 101, 'Snowboard');
INSERT INTO `teams` VALUES (13, 'aaa1', 'bbb2', 103, 'Freestyle Skiing');

SET FOREIGN_KEY_CHECKS = 1;
