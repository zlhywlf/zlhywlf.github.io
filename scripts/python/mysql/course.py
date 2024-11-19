from datetime import UTC, datetime, time
from typing import ClassVar

from faker import Faker
from sqlalchemy import Column, UniqueConstraint, create_engine, select
from sqlalchemy.dialects.mysql import (
    CHAR,
    DATETIME,
    DECIMAL,
    ENUM,
    INTEGER,
    MEDIUMINT,
    SMALLINT,
    TEXT,
    TIME,
    TIMESTAMP,
    TINYINT,
    VARCHAR,
    dialect,
)
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func
from sqlmodel import Field, SQLModel
from util import column, common_table_args

lang = "zh_CN"
schema = "course"
db = "mysql+pymysql://course:course@10.8.15.218:3306/course"
start_date_time = datetime(2020, 1, 1, tzinfo=UTC)
end_date_time = datetime(2021, 1, 1, tzinfo=UTC)
dialect = dialect()


@common_table_args
class Course(SQLModel, table=True):
    """课程."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    title: str = Field(..., **column(VARCHAR(20), "主标题"))
    title_desc: str = Field(..., **column(VARCHAR(50), "副标题"))
    type_id: str = Field(..., **column(SMALLINT(unsigned=True), "课程方向ID", "0"))
    class_id: str = Field(..., **column(SMALLINT(unsigned=True), "课程分类ID", "0"))
    level_id: str = Field(..., **column(SMALLINT(unsigned=True), "课程难度ID", "0"))
    online_time: str = Field(..., **column(DATETIME(), "上线时间", func.current_timestamp()))
    study_cnt: str = Field(..., **column(INTEGER(unsigned=True), "学习人数", "0"))
    course_time: str = Field(..., **column(TIME(), "课程时长", "00:00:00"))
    intro: str = Field(..., **column(VARCHAR(200), "课程简介"))
    info: str = Field(..., **column(VARCHAR(200), "学习需知"))
    harvest: str = Field(..., **column(VARCHAR(200), "课程收获"))
    user_id: str = Field(..., **column(INTEGER(unsigned=True), "讲师ID", "0"))
    main_pic: str = Field(..., **column(VARCHAR(200), "课程主图片"))
    content_score: str = Field(..., **column(DECIMAL(3, 1), "内容评分", "0.0"))
    level_score: str = Field(..., **column(DECIMAL(3, 1), "简单易懂", "0.0"))
    logic_score: str = Field(..., **column(DECIMAL(3, 1), "逻辑清晰", "0.0"))
    score: str = Field(..., **column(DECIMAL(3, 1), "综合评分", "0.0"))

    __table_args__ = (
        UniqueConstraint("title", name="udx_title"),
    )


@common_table_args
class Chapter(SQLModel, table=True):
    """章节."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    chapter_name: str = Field(..., **column(VARCHAR(50), "章节名称"))
    chapter_info: str = Field(..., **column(VARCHAR(200), "章节说明"))
    chapter_no: str = Field(..., **column(TINYINT(2, unsigned=True, zerofill=True), "章节编号", "00"))

    __table_args__ = (
        UniqueConstraint("course_id", "chapter_name", name="udx_couseid_chaptername"),
    )


@common_table_args
class Subsection(SQLModel, table=True):
    """小节."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    chapter_id: str = Field(..., **column(INTEGER(unsigned=True), "章节ID", "0"))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    sub_name: str = Field(..., **column(VARCHAR(50), "小节名称"))
    sub_url: str = Field(..., **column(VARCHAR(200), "小节链接"))
    video_type: str = Field(..., **column(ENUM("avi", "mp4", "mpeg"), "视频格式", "mp4"))
    sub_time: str = Field(..., **column(TIME(), "小节时长", "00:00:00"))
    sub_no: str = Field(..., **column(TINYINT(2, unsigned=True, zerofill=True), "小节编号", "00"))

    __table_args__ = (
        UniqueConstraint("course_id", "chapter_id", "sub_name", name="udx_courseid_chapterid_subname"),
    )


@common_table_args
class Classification(SQLModel, table=True):
    """分类."""
    id: int = Field(None, sa_column=Column(SMALLINT(unsigned=True), primary_key=True))
    class_name: str = Field(..., **column(VARCHAR(10), "课程分类名称"))
    add_time: str = Field(..., **column(TIMESTAMP(), "添加时间", func.current_timestamp()))


@common_table_args
class Level(SQLModel, table=True):
    """课程难度."""
    id: int = Field(None, sa_column=Column(SMALLINT(unsigned=True), primary_key=True))
    level_name: str = Field(..., **column(VARCHAR(10), "课程难度名称"))
    add_time: str = Field(..., **column(TIMESTAMP(), "添加时间", func.current_timestamp()))


@common_table_args
class Type(SQLModel, table=True):
    """课程方向."""
    id: int = Field(None, sa_column=Column(SMALLINT(unsigned=True), primary_key=True))
    type_name: str = Field(..., **column(VARCHAR(10), "课程方向名称"))
    add_time: str = Field(..., **column(TIMESTAMP(), "添加时间", func.current_timestamp()))


@common_table_args
class User(SQLModel, table=True):
    """用户."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    user_nick: str = Field(..., **column(VARCHAR(20), "用户昵称", "unknown"))
    user_pwd: str = Field(..., **column(CHAR(32), "密码"))
    sex: str = Field(..., **column(CHAR(2), "性别", "未知"))
    province: str = Field(..., **column(VARCHAR(20), "省"))
    city: str = Field(..., **column(VARCHAR(20), "市"))
    position: str = Field(..., **column(VARCHAR(10), "职位", "unknown"))
    mem: str = Field(..., **column(VARCHAR(100), "说明"))
    exp_cnt: str = Field(..., **column(MEDIUMINT(unsigned=True), "经验值", "0"))
    score: str = Field(..., **column(INTEGER(unsigned=True), "积分", "0"))
    follow_cnt: str = Field(..., **column(INTEGER(unsigned=True), "关注人数", "0"))
    fans_cnt: str = Field(..., **column(INTEGER(unsigned=True), "粉丝人数", "0"))
    is_teacher: str = Field(..., **column(TINYINT(unsigned=True), "讲师标识,0:普通用户,1:讲师用户", "0"))
    reg_time: str = Field(..., **column(DATETIME(), "注册时间", func.current_timestamp()))
    user_status: str = Field(..., **column(TINYINT(unsigned=True), "用户状态,1:正常 0:冻结", "1"))

    __table_args__ = (
        UniqueConstraint("user_nick", name="udx_usernick"),
    )


@common_table_args
class Question(SQLModel, table=True):
    """问答评论."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    user_id: str = Field(..., **column(INTEGER(unsigned=True), "用户ID", "0"))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    chapter_id: str = Field(..., **column(INTEGER(unsigned=True), "章节ID", "0"))
    sub_id: str = Field(..., **column(INTEGER(unsigned=True), "小节ID", "0"))
    reply_id: str = Field(..., **column(INTEGER(unsigned=True), "父评论ID", "0"))
    quest_title: str = Field(..., **column(VARCHAR(50), "评论标题"))
    quest_content: str = Field(..., **column(TEXT(), "评论内容", None, nullable=True))
    quest_type: str = Field(..., **column(ENUM("问答", "评论"), "评论类型", "评论"))
    view_cnt: str = Field(..., **column(INTEGER(unsigned=True), "浏览量", "0"))
    add_time: str = Field(..., **column(DATETIME(), "发布时间", func.current_timestamp()))


@common_table_args
class Note(SQLModel, table=True):
    """笔记."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    user_id: str = Field(..., **column(INTEGER(unsigned=True), "用户ID", "0"))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    chapter_id: str = Field(..., **column(INTEGER(unsigned=True), "章节ID", "0"))
    sub_id: str = Field(..., **column(INTEGER(unsigned=True), "小节ID", "0"))
    note_title: str = Field(..., **column(VARCHAR(50), "笔记标题"))
    note_content: str = Field(..., **column(TEXT(), "笔记内容", None, nullable=True))
    add_time: str = Field(..., **column(DATETIME(), "发布时间", func.current_timestamp()))


@common_table_args
class ClassValue(SQLModel, table=True):
    """课程评价."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    user_id: str = Field(..., **column(INTEGER(unsigned=True), "用户ID", "0"))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    content_score: str = Field(..., **column(DECIMAL(3, 1), "内容评分", "0.0"))
    level_score: str = Field(..., **column(DECIMAL(3, 1), "简单易懂", "0.0"))
    logic_score: str = Field(..., **column(DECIMAL(3, 1), "逻辑清晰", "0.0"))
    score: str = Field(..., **column(DECIMAL(3, 1), "综合评分", "0.0"))
    add_time: str = Field(..., **column(DATETIME(), "发布时间", func.current_timestamp()))

    __tablename__: ClassVar[str] = "class_value"


@common_table_args
class SelectCourse(SQLModel, table=True):
    """用户选课."""
    id: int = Field(None, sa_column=Column(INTEGER(unsigned=True), primary_key=True))
    user_id: str = Field(..., **column(INTEGER(unsigned=True), "用户ID", "0"))
    course_id: str = Field(..., **column(INTEGER(unsigned=True), "课程ID", "0"))
    select_time: str = Field(..., **column(DATETIME(), "选课时间", func.current_timestamp()))
    study_time: str = Field(..., **column(TIME(), "累积听课时间", "00:00:00"))

    __tablename__: ClassVar[str] = "select_course"


fake = Faker(lang)
engine = create_engine(db, echo=True)
session = Session(engine)
SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

types = [Type(
    type_name=fake.unique.word(),
    add_time=fake.date_time_between(start_date_time, end_date_time),
) for _ in range(5)]
session.add_all(types)
session.commit()
types = list(session.scalars(select(Type)))

classifications = [Classification(
    class_name=fake.unique.word(),
    add_time=fake.date_time_between(start_date_time, end_date_time),
) for _ in range(5)]
session.add_all(classifications)
session.commit()
classifications = list(session.scalars(select(Classification)))

levels = [Level(
    level_name=fake.unique.word(),
    add_time=fake.date_time_between(start_date_time, end_date_time),
) for _ in range(5)]
session.add_all(levels)
session.commit()
levels = list(session.scalars(select(Level)))

users = [User(
    user_nick=fake.unique.name(),
    user_pwd=fake.md5(),
    sex=fake.random_element(["男", "女", "未知"]),
    province=fake.province(),
    city=fake.city(),
    position=fake.job()[:10],
    mem=fake.text(fake.random_int(20, 100)),
    exp_cnt=fake.random_int(0, 9999),
    score=fake.random_int(0, 9999),
    follow_cnt=fake.random_int(0, 9999),
    fans_cnt=fake.random_int(0, 9999),
    is_teacher=fake.random_int(0, 1),
    reg_time=fake.date_time_between(start_date_time, end_date_time),
    user_status=1,
) for _ in range(7)]
session.add_all(users)
session.commit()
users = list(session.scalars(select(User)))
teachers = [_ for _ in users if _.is_teacher == 1]
students = [_ for _ in users if _.is_teacher == 0]

courses = [Course(
    title=fake.text(fake.random_int(5, 20)),
    title_desc=fake.text(fake.random_int(20, 50)),
    type_id=types[fake.random_int(0, len(types) - 1)].id,
    class_id=classifications[fake.random_int(0, len(classifications) - 1)].id,
    level_id=levels[fake.random_int(0, len(levels) - 1)].id,
    online_time=fake.date_time_between(start_date_time, end_date_time),
    study_cnt=fake.random_int(0),
    course_time=time.fromisoformat(fake.time()),
    intro=fake.text(fake.random_int(50, 200)),
    info=fake.text(fake.random_int(50, 200)),
    harvest=fake.text(fake.random_int(50, 200)),
    user_id=teachers[fake.random_int(0, len(teachers) - 1)].id,
    main_pic=fake.uri(),
    content_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
    level_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
    logic_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
    score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
) for _ in range(5)]
session.add_all(courses)
session.commit()
courses = list(session.scalars(select(Course)))

chapters = []
for course in courses:
    for no in range(fake.random_int(5, 23)):
        chapters.append(Chapter(
            course_id=course.id,
            chapter_name=fake.text(fake.random_int(5, 20)),
            chapter_info=fake.text(fake.random_int(20, 50)),
            chapter_no=no + 1,
        ))
session.add_all(chapters)
session.commit()
chapters = list(session.scalars(select(Chapter)))

subsections = []
for chapter in chapters:
    for no in range(fake.random_int(5, 23)):
        subsections.append(Subsection(
            chapter_id=chapter.id,
            course_id=chapter.course_id,
            sub_name=fake.text(fake.random_int(5, 20)),
            sub_url=fake.uri(),
            video_type=fake.random_element(["avi", "mp4", "mpeg"]),
            sub_time=time.fromisoformat(fake.time()),
            sub_no=no + 1,
        ))
session.add_all(subsections)
session.commit()
subsections = list(session.scalars(select(Subsection)))

index = 1
for student in students:
    for sub in subsections:
        reply_id = index
        for _ in range(fake.random_int(1, 5)):
            session.add(Question(
                user_id=student.id,
                course_id=sub.course_id,
                chapter_id=sub.chapter_id,
                sub_id=sub.id,
                reply_id=reply_id,
                quest_title=fake.text(fake.random_int(5, 20)),
                quest_content=fake.text(fake.random_int(50, 200)),
                quest_type=fake.random_element(["问答", "评论"]),
                view_cnt=fake.random_int(50, 200),
                add_time=fake.date_time_between(start_date_time, end_date_time),
            ))
            if _ >= 1:
                reply_id = index
            index += 1

    for sub in subsections:
        for _ in range(fake.random_int(1, 5)):
            session.add(Note(
                user_id=student.id,
                course_id=sub.course_id,
                chapter_id=sub.chapter_id,
                sub_id=sub.id,
                note_title=fake.text(fake.random_int(5, 20)),
                note_content=fake.text(fake.random_int(50, 200)),
                add_time=fake.date_time_between(start_date_time, end_date_time),
            ))

    for course in courses:
        session.add(ClassValue(
            user_id=student.id,
            course_id=course.id,
            content_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
            level_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
            logic_score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
            score=fake.pyfloat(min_value=0, max_value=10, right_digits=1),
            add_time=fake.date_time_between(start_date_time, end_date_time),
        ))

    for course in courses:
        session.add(SelectCourse(
            user_id=student.id,
            course_id=course.id,
            select_time=fake.date_time_between(start_date_time, end_date_time),
            study_time=time.fromisoformat(fake.time()),
        ))
    session.commit()

session.close()
