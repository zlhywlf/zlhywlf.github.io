# course

## 结构设计

```mermaid
erDiagram
  course ||--o{ chapter: ""
  course ||--o{ question: ""
  course }o--|| class: ""
  course }o--|| level: ""
  course }o--|| type: ""
  course }o--|| user: ""
  chapter ||--o{ subsection: ""
  user ||--o{ note: ""
  user ||--o{ class_value: ""
  user ||--o{ select_course: ""

  course {
    int id PK "课程ID"
    varchar title UK "主标题"
    varchar title_desc "副标题"
    smallint type_id FK "课程方向ID"
    smallint class_id FK "课程分类ID"
    smallint level_id FK "课程难度ID"
    datetime online_time "上线时间"
    int study_cnt "学习人数"
    time course_time "课程时长"
    varchar intro "课程简介"
    varchar info "学习须知"
    varchar harvest "课程收获"
    int user_id FK "讲师ID"
    varchar main_pic "课程主图片"
    decimal content_score "内容评分"
    decimal level_score "简单易懂"
    decimal logic_score "逻辑清晰"
    decimal score "综合评分"
  }

  chapter {
    int id PK "章节ID"
    int course_id FK "课程ID"
    varchar chapter_name UK "章节名称"
    varchar chapter_info "章节说明"
    tinyint chapter_no "章节编号"
  }

  subsection {
    int id PK "小节ID"
    int chapter_id FK "章节ID"
    int course_id FK "课程ID"
    varchar sub_name UK "小节名称"
    varchar sub_url "小节链接"
    enum video_type "视频格式"
    time sub_time "小节时长"
    tinyint sub_no "小节编号"
  }

  classification {
    smallint id PK "课程分类ID"
    varchar class_name UK "课程分类名称"
    timestamp add_time "添加时间"
  }

  level {
    smallint id PK "课程难度ID"
    varchar level_name UK "课程难度名称"
    timestamp add_time "添加时间"
  }

  type {
    smallint id PK "课程方向ID"
    varchar type_name UK "课程方向名称"
    timestamp add_time "添加时间"
  }

  user {
    int id PK "用户ID"
    varchar user_nick UK "昵称"
    char user_pwd "密码"
    char sex "性别"
    varchar province "省"
    varchar city "市"
    varchar position "职位"
    varchar mem "说明"
    mediumint exp_cnt "经验值"
    int score "积分"
    int follow_cnt "关注人数"
    int fans_cnt "粉丝人数"
    tinyint is_teacher "讲师标识"
    datetime reg_time "注册时间"
    tinyint user_status "用户状态"
  }

  question {
    int id PK "评论ID"
    int user_id FK "用户ID"
    int course_id FK "课程ID"
    int chapter_id FK "章节ID"
    int sub_id FK "小节ID"
    int reply_id FK "父评论ID"
    varchar quest_title "评论标题"
    text quest_content "评论内容"
    enum quest_type "评论类型"
    int view_cnt "浏览量"
    datetime add_time "发布时间"
  }

  note {
    int id PK "笔记ID"
    int user_id FK "用户ID"
    int course_id FK "课程ID"
    int chapter_id FK "章节ID"
    int sub_id FK "小节ID"
    varchar note_title "笔记标题"
    text note_content "笔记内容"
    datetime add_time "发布时间"
  }

  class_value {
    int id PK "问答评论ID"
    int user_id FK "用户ID"
    int course_id FK "课程ID"
    decimal content_score "内容评分"
    decimal level_score "简单易懂"
    decimal logic_score "逻辑清晰"
    decimal score "综合评分"
    datetime add_time "发布时间"
  }

  select_course {
    int id PK "选课ID"
    int user_id FK "用户ID"
    int course_id FK "课程ID"
    datetime select_time "选课时间"
    time study_time "累计听课时间"
  }
```

## DDL {#DDL}

```sql
DROP
  DATABASE IF EXISTS `course`;
CREATE
  DATABASE `course`;
USE
  `course`;

DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`
(
  `id`            INT UNSIGNED      NOT NULL AUTO_INCREMENT COMMENT '课程ID',
  `title`         VARCHAR(20)       NOT NULL DEFAULT '' COMMENT '主标题',
  `title_desc`    VARCHAR(50)       NOT NULL DEFAULT '' COMMENT '副标题',
  `type_id`       SMALLINT UNSIGNED NOT NULL DEFAULT '0' COMMENT '课程方向ID',
  `class_id`      SMALLINT UNSIGNED NOT NULL DEFAULT '0' COMMENT '课程分类ID',
  `level_id`      SMALLINT UNSIGNED NOT NULL DEFAULT '0' COMMENT '课程难度ID',
  `online_time`   DATETIME          NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '上线时间',
  `study_cnt`     INT UNSIGNED      NOT NULL DEFAULT '0' COMMENT '学习人数',
  `course_time`   TIME              NOT NULL DEFAULT '00:00:00' COMMENT '课程时长',
  `intro`         VARCHAR(200)      NOT NULL DEFAULT '' COMMENT '课程简介',
  `info`          VARCHAR(200)      NOT NULL DEFAULT '' COMMENT '学习需知',
  `harvest`       VARCHAR(200)      NOT NULL DEFAULT '' COMMENT '课程收获',
  `user_id`       INT UNSIGNED      NOT NULL DEFAULT '0' COMMENT '讲师ID',
  `main_pic`      VARCHAR(200)      NOT NULL DEFAULT '' COMMENT '课程主图片',
  `content_score` DEC(3, 1)         NOT NULL DEFAULT '0.0' COMMENT '内容评分',
  `level_score`   DEC(3, 1)         NOT NULL DEFAULT '0.0' COMMENT '简单易懂',
  `logic_score`   DEC(3, 1)         NOT NULL DEFAULT '0.0' COMMENT '逻辑清晰',
  `score`         DEC(3, 1)         NOT NULL DEFAULT '0.0' COMMENT '综合评分',
  PRIMARY KEY (`id`),
  UNIQUE KEY `udx_title` (`title`)
) COMMENT ='课程';

DROP TABLE IF EXISTS `chapter`;
CREATE TABLE `chapter`
(
  `id`           INT UNSIGNED                 NOT NULL AUTO_INCREMENT COMMENT '章节ID',
  `course_id`    INT UNSIGNED                 NOT NULL DEFAULT '0' COMMENT '课程ID',
  `chapter_name` VARCHAR(50)                  NOT NULL DEFAULT '' COMMENT '章节名称',
  `chapter_info` VARCHAR(200)                 NOT NULL DEFAULT '' COMMENT '章节说明',
  `chapter_no`   TINYINT(2) UNSIGNED ZEROFILL NOT NULL DEFAULT '00' COMMENT '章节编号',
  PRIMARY KEY (`id`),
  UNIQUE KEY `udx_couseid_chaptername` (`course_id`, `chapter_name`)
) COMMENT ='章节';

DROP TABLE IF EXISTS `subsection`;
CREATE TABLE `subsection`
(
  `id`         INT UNSIGNED                 NOT NULL AUTO_INCREMENT COMMENT '小节ID',
  `chapter_id` INT UNSIGNED                 NOT NULL DEFAULT '0' COMMENT '章节ID',
  `course_id`  INT UNSIGNED                 NOT NULL DEFAULT '0' COMMENT '课程ID',
  `sub_name`   VARCHAR(50)                  NOT NULL DEFAULT '' COMMENT '小节名称',
  `sub_url`    VARCHAR(200)                 NOT NULL DEFAULT '' COMMENT '小节链接',
  `video_type` ENUM ('avi','mp4','mpeg')    NOT NULL DEFAULT 'mp4' COMMENT '视频格式',
  `sub_time`   TIME                         NOT NULL DEFAULT '00:00:00' COMMENT '小节时长',
  `sub_no`     TINYINT(2) UNSIGNED ZEROFILL NOT NULL DEFAULT '00' COMMENT '小节编号',
  PRIMARY KEY (`id`),
  UNIQUE KEY `udx_courseid_chapterid_subname` (`course_id`, `chapter_id`, `sub_name`)
) COMMENT ='小节';

DROP TABLE IF EXISTS `classification`;
CREATE TABLE `classification`
(
  `id`         SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程分类ID',
  `class_name` VARCHAR(10)       NOT NULL DEFAULT '' COMMENT '课程分类名称',
  `add_time`   TIMESTAMP         NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
  PRIMARY KEY (`id`)
) COMMENT ='分类';

DROP TABLE IF EXISTS `level`;
CREATE TABLE `level`
(
  `id`         SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程难度ID',
  `level_name` VARCHAR(10)       NOT NULL DEFAULT '' COMMENT '课程难度名称',
  `add_time`   TIMESTAMP         NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
  PRIMARY KEY (`id`)
) COMMENT ='课程难度';

DROP TABLE IF EXISTS `type`;
CREATE TABLE `type`
(
  `id`        SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程方向ID',
  `type_name` VARCHAR(10)       NOT NULL DEFAULT '' COMMENT '课程方向名称',
  `add_time`  TIMESTAMP         NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
  PRIMARY KEY (`id`)
) COMMENT ='课程方向';

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`
(
  `id`          INT UNSIGNED       NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `user_nick`   VARCHAR(20)        NOT NULL DEFAULT '慕课网' COMMENT '用户昵称',
  `user_pwd`    CHAR(32)           NOT NULL DEFAULT '' COMMENT '密码',
  `sex`         CHAR(2)            NOT NULL DEFAULT '未知' COMMENT '性别',
  `province`    VARCHAR(20)        NOT NULL DEFAULT '' COMMENT '省',
  `city`        VARCHAR(20)        NOT NULL DEFAULT '' COMMENT '市',
  `Position`    VARCHAR(10)        NOT NULL DEFAULT '未知' COMMENT '职位',
  `mem`         VARCHAR(100)       NOT NULL DEFAULT '' COMMENT '说明',
  `exp_cnt`     MEDIUMINT UNSIGNED NOT NULL DEFAULT '0' COMMENT '经验值',
  `score`       INT UNSIGNED       NOT NULL DEFAULT '0' COMMENT '积分',
  `follow_cnt`  INT UNSIGNED       NOT NULL DEFAULT '0' COMMENT '关注人数',
  `fans_cnt`    INT UNSIGNED       NOT NULL DEFAULT '0' COMMENT '粉丝人数',
  `is_teacher`  TINYINT UNSIGNED   NOT NULL DEFAULT '0' COMMENT '讲师标识,0:普通用户,1:讲师用户',
  `reg_time`    DATETIME           NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
  `user_status` TINYINT UNSIGNED   NOT NULL DEFAULT '1' COMMENT '用户状态,1:正常 0:冻结',
  PRIMARY KEY (`id`),
  UNIQUE KEY `udx_usernick` (`user_nick`)
) COMMENT ='用户';

DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`
(
  `id`            INT UNSIGNED         NOT NULL AUTO_INCREMENT COMMENT '评论ID',
  `user_id`       INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '用户ID',
  `course_id`     INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '课程ID',
  `chapter_id`    INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '章节ID',
  `sub_id`        INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '小节ID',
  `reply_id`      INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '父评论ID',
  `quest_title`   VARCHAR(50)          NOT NULL DEFAULT '' COMMENT '评论标题',
  `quest_content` TEXT COMMENT '评论内容',
  `quest_type`    ENUM ('问答','评论') NOT NULL DEFAULT '评论' COMMENT '评论类型',
  `view_cnt`      INT UNSIGNED         NOT NULL DEFAULT '0' COMMENT '浏览量',
  `add_time`      DATETIME             NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间',
  PRIMARY KEY (`id`)
) COMMENT ='问答评论';

DROP TABLE IF EXISTS `note`;
CREATE TABLE `note`
(
  `id`           INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '笔记ID',
  `user_id`      INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '用户ID',
  `course_id`    INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '课程ID',
  `chapter_id`   INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '章节ID',
  `sub_id`       INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '小节ID',
  `note_title`   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '笔记标题',
  `note_content` TEXT COMMENT '评论内容',
  `add_time`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间',
  PRIMARY KEY (`id`)
) COMMENT ='笔记';

DROP TABLE IF EXISTS `class_value`;
CREATE TABLE `class_value`
(
  `id`            INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT '问答评论ID',
  `user_id`       INT UNSIGNED  NOT NULL DEFAULT '0' COMMENT '用户ID',
  `course_id`     INT UNSIGNED  NOT NULL DEFAULT '0' COMMENT '课程ID',
  `content_score` DECIMAL(3, 1) NOT NULL DEFAULT '0.0' COMMENT '内容评分',
  `level_score`   DECIMAL(3, 1) NOT NULL DEFAULT '0.0' COMMENT '简单易懂',
  `logic_score`   DECIMAL(3, 1) NOT NULL DEFAULT '0.0' COMMENT '逻辑清晰',
  `score`         DECIMAL(3, 1) NOT NULL DEFAULT '0.0' COMMENT '综合评分',
  `add_time`      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间',
  PRIMARY KEY (`id`)
) COMMENT ='课程评价';

DROP TABLE IF EXISTS `select_course`;
CREATE TABLE `select_course`
(
  `id`          INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '选课ID',
  `user_id`     INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '用户ID',
  `course_id`   INT UNSIGNED NOT NULL DEFAULT '0' COMMENT '课程ID',
  `select_time` DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '选课时间',
  `study_time`  TIME         NOT NULL DEFAULT '00:00:00' COMMENT '累积听课时间',
  PRIMARY KEY (`id`)
) COMMENT ='用户选课';
```

## DML {#DML}
