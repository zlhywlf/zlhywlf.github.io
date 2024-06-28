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

  class {
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
