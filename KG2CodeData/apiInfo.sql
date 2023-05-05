/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1_3333
Source Server Version : 50737
Source Host           : 127.0.0.1:3333
Source Database       : apitest

Target Server Type    : MYSQL
Target Server Version : 50737
File Encoding         : 65001

Date: 2022-04-10 00:23:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for apiInfo
-- ----------------------------
DROP TABLE IF EXISTS `apiInfo`;
CREATE TABLE `apiInfo` (
  `apiId` int(11) NOT NULL AUTO_INCREMENT,
  `package` varchar(255) DEFAULT NULL,
  `class` varchar(255) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `begin` varchar(255) DEFAULT NULL,
  `end` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`apiId`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apiInfo
-- ----------------------------
INSERT INTO `apiInfo` VALUES ('1', 'java.nio', 'ByteBuffer', 'get', 'c-o', '1942', 'rewind()', 'get()');
INSERT INTO `apiInfo` VALUES ('2', 'javax.swing', 'StringTokenizer', 'nextToken', 's-c', '41176', 'hasMoreTokens()', 'nextToken()');
INSERT INTO `apiInfo` VALUES ('3', 'java.lang.String', 'Scanner', 'nextLine', 's-c', '2796', 'hasNextLine()', 'nextLine()');
INSERT INTO `apiInfo` VALUES ('4', ' ', 'ApplicationInfo', 'loadIcon', 'c-o', '400', 'getPackageManager()', 'loadIcon()');
INSERT INTO `apiInfo` VALUES ('5', ' ', 'BufferedReader', 'readLine', 'c-o', '31257', 'BufferedReader()', 'readLine()');
INSERT INTO `apiInfo` VALUES ('6', ' ', 'Bundle', 'putString', 'c-o', '10616', 'Bundle()', 'putString()');
INSERT INTO `apiInfo` VALUES ('7', ' ', 'ByteBuffer', 'get', 's-c', '191', 'hasRemaining()', 'get()');
INSERT INTO `apiInfo` VALUES ('8', ' ', 'Cipher', 'init', 'c-o', '1969', 'getInstance()', 'init()');
INSERT INTO `apiInfo` VALUES ('9', ' ', 'Cursor', 'getString', 'c-o', '10418', 'getString()', 'close()');
INSERT INTO `apiInfo` VALUES ('10', ' ', 'Cursor', 'moveToFirst', 'c-o', '6501', 'moveToFirst()', 'close()');
INSERT INTO `apiInfo` VALUES ('11', ' ', 'FileChannel', 'write', 'c-o', '768', 'getChannel()', 'write()');
INSERT INTO `apiInfo` VALUES ('12', ' ', 'FileChannel', 'write', 'c-o', '666', 'write()', 'close()');
INSERT INTO `apiInfo` VALUES ('13', ' ', 'HttpClient', 'execute', 'c-o', '2536', 'HttpGet()', 'execute()');
INSERT INTO `apiInfo` VALUES ('14', ' ', 'Intent', 'putExtra', 'c-o', '15583', 'Intent()', 'putExtra()');
INSERT INTO `apiInfo` VALUES ('15', ' ', 'Iterator', 'next', 's-c', '253733', 'hasNext()', 'next()');
INSERT INTO `apiInfo` VALUES ('16', ' ', 'Iterator', 'next', 'c-o', '219571', 'iterator()', 'next()');
INSERT INTO `apiInfo` VALUES ('17', ' ', 'JButton', 'addActionListener', 'c-o', '23556', 'JButton()', 'addActionListener()');
INSERT INTO `apiInfo` VALUES ('18', ' ', 'JFrame', 'getContentPane', 'c-o', '4923', 'JFrame()', 'getContentPane()');
INSERT INTO `apiInfo` VALUES ('19', ' ', 'JFrame', 'pack', 'c-o', '6650', 'pack()', 'setVisible()');
INSERT INTO `apiInfo` VALUES ('20', ' ', 'JFrame', 'pack', 'c-o', '4550', 'JFrame()', 'pack()');
INSERT INTO `apiInfo` VALUES ('21', ' ', 'JFrame', 'setDefaultCloseOperation', 'c-o', '6971', 'setDefaultCloseOperation()', 'setVisible()');
INSERT INTO `apiInfo` VALUES ('22', ' ', 'JFrame', 'setDefaultCloseOperation', 'c-o', '5164', 'JFrame()', 'setDefaultCloseOperation()');
INSERT INTO `apiInfo` VALUES ('23', ' ', 'JFrame', 'setPreferredSize', 'c-o', '467', 'Dimension()', 'setPreferredSize()');
INSERT INTO `apiInfo` VALUES ('24', ' ', 'JFrame', 'setPreferredSize', 'c-o', '394', 'setPreferredSize()', 'pack()');
INSERT INTO `apiInfo` VALUES ('25', ' ', 'JFrame', 'setPreferredSize', 'c-o', '390', 'setPreferredSize()', 'setVisible()');
INSERT INTO `apiInfo` VALUES ('26', ' ', 'JFrame', 'setPreferredSize', 'c-o', '273', 'JFrame()', 'setPreferredSize()');
INSERT INTO `apiInfo` VALUES ('27', ' ', 'JFrame', 'setVisible', 'c-o', '7441', 'JFrame()', 'setVisible()');
INSERT INTO `apiInfo` VALUES ('28', ' ', 'JPanel', 'add', 'c-o', '17651', 'JPanel()', 'add()');
INSERT INTO `apiInfo` VALUES ('29', ' ', 'JsonElement', 'getAsString', 's-c', '51', 'isJsonPrimitive()', 'getAsString()');
INSERT INTO `apiInfo` VALUES ('30', ' ', 'JSONObject', 'getJSONArray', 'c-o', '3662', 'getJSONArray()', 'getJSONObject()');
INSERT INTO `apiInfo` VALUES ('31', ' ', 'Jsoup', 'connect', 'c-o', '376', 'connect()', 'get()');
INSERT INTO `apiInfo` VALUES ('32', ' ', 'KeyStore', 'load', 'c-o', '5246', 'getInstance()', 'load()');
INSERT INTO `apiInfo` VALUES ('33', ' ', 'LayoutInflater', 'from', 'c-o', '8251', 'from()', 'inflate()');
INSERT INTO `apiInfo` VALUES ('34', ' ', 'LinearLayout', 'addView', 'c-o', '1685', 'TextView()', 'addView()');
INSERT INTO `apiInfo` VALUES ('35', ' ', 'LinearLayout', 'addView', 'c-o', '1324', 'LinearLayout()', 'addView()');
INSERT INTO `apiInfo` VALUES ('36', ' ', 'Matcher', 'find', 'c-o', '5851', 'matcher()', 'find()');
INSERT INTO `apiInfo` VALUES ('37', ' ', 'Matcher', 'group', 'c-o', '31511', 'matcher()', 'group()');
INSERT INTO `apiInfo` VALUES ('38', ' ', 'Matcher', 'group', 's-c', '16446', 'find()', 'group()');
INSERT INTO `apiInfo` VALUES ('39', ' ', 'MessageDigest', 'digest', 'c-o', '7047', 'getInstance()', 'digest()');
INSERT INTO `apiInfo` VALUES ('40', ' ', 'Pattern', 'compile', 'c-o', '24889', 'compile()', 'matcher()');
INSERT INTO `apiInfo` VALUES ('41', ' ', 'PreparedStatement', 'setString', 'c-o', '25953', 'prepareStatement()', 'setString()');
INSERT INTO `apiInfo` VALUES ('42', ' ', 'PreparedStatement', 'setString', 'c-o', '11359', 'setString()', 'close()');
INSERT INTO `apiInfo` VALUES ('43', ' ', 'PrintWriter', 'write', 'c-o', '2472', 'write()', 'close()');
INSERT INTO `apiInfo` VALUES ('44', ' ', 'ProcessBuilder', 'start', 'c-o', '2255', 'start()', 'getInputStream()');
INSERT INTO `apiInfo` VALUES ('45', ' ', 'RandomAccessFile', 'write', 'c-o', '1407', 'write()', 'close()');
INSERT INTO `apiInfo` VALUES ('46', ' ', 'ResultSet', 'getString', 's-c', '18933', 'next()', 'getString()');
INSERT INTO `apiInfo` VALUES ('47', ' ', 'Scanner', 'nextInt', 'c-o', '3212', 'Scanner()', 'nextInt()');
INSERT INTO `apiInfo` VALUES ('48', ' ', 'Scanner', 'nextLine', 's-c', '2510', 'hasNextLine()', 'nextLine()');
INSERT INTO `apiInfo` VALUES ('49', ' ', 'Scanner', 'nextLine', 'c-o', '2300', 'Scanner()', 'nextLine()');
INSERT INTO `apiInfo` VALUES ('50', ' ', 'SharedPreferences', 'edit', 'c-o', '9650', 'edit()', 'commit()');
INSERT INTO `apiInfo` VALUES ('51', ' ', 'SimpleDateFormat', 'format', 'c-o', '18976', 'SimpleDateFormat()', 'format()');
INSERT INTO `apiInfo` VALUES ('52', ' ', 'SimpleDateFormat', 'parse', 'c-o', '9783', 'SimpleDateFormat()', 'parse()');
INSERT INTO `apiInfo` VALUES ('53', ' ', 'SimpleDateFormat', 'SimpleDateFormat', 'c-o', '18976', 'SimpleDateFormat()', 'format()');
INSERT INTO `apiInfo` VALUES ('54', ' ', 'SimpleDateFormat', 'SimpleDateFormat', 'c-o', '9783', 'SimpleDateFormat()', 'parse()');
INSERT INTO `apiInfo` VALUES ('55', ' ', 'SQLiteDatabase', 'query', 'c-o', '5563', 'query()', 'close()');
INSERT INTO `apiInfo` VALUES ('56', ' ', 'StringBuilder', 'append', 'c-o', '237169', 'StringBuilder()', 'append()');
INSERT INTO `apiInfo` VALUES ('57', ' ', 'Toast', 'makeText', 'c-o', '23649', 'makeText()', 'show()');
INSERT INTO `apiInfo` VALUES ('58', ' ', 'TypedArray', 'getString', 'c-o', '2125', 'getString()', 'recycle()');
INSERT INTO `apiInfo` VALUES ('59', ' ', 'URL', 'openConnection', 'c-o', '19056', 'URL()', 'openConnection()');
INSERT INTO `apiInfo` VALUES ('60', ' ', 'URL', 'openConnection', 'c-o', '16125', 'openConnection()', 'getInputStream()');
INSERT INTO `apiInfo` VALUES ('61', null, 'Environment', 'getExternalStorageState', 'trigger', '2324', 'getExternalStorageState()', 'getExternalStorageState()');
INSERT INTO `apiInfo` VALUES ('62', 'java.awt', 'Toolkit', 'getAWTEventListeners', 'd-c', '4333', 'getAWTEventListeners()', 'getAWTEventListeners()');
INSERT INTO `apiInfo` VALUES ('63', 'java.net', 'URLConnection', 'getHeaderField', 'd-c', '3455', 'getHeaderField()', 'getHeaderField()');
INSERT INTO `apiInfo` VALUES ('64', 'javax.sound.midi.Sequencer', 'SyncMode', '', 'sy-c', '12237', 'SyncMode', 'SyncMode');
INSERT INTO `apiInfo` VALUES ('65', 'javax.swing.table', 'DefaultTableModel', 'insertRow', 'trigger', '4589', 'insertRow()', 'insertRow()');
INSERT INTO `apiInfo` VALUES ('66', 'java.util', 'Map', null, 'sy-c', '435256', 'Map', 'Map');
