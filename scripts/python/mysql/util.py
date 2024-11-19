from typing import Any

from sqlalchemy import Column, Dialect
from sqlalchemy.sql.ddl import CreateTable, DropTable
from sqlmodel import SQLModel


def common_table_args(cls: type) -> type:
    """公共表参数."""
    if hasattr(cls, "__table__"):
        cls.__table__.comment = cls.__doc__.replace(".", "")
    return cls


def get_sql(dialect: Dialect | None = None, *, origin_style: bool = False) -> str:
    """获取建表 SQL."""
    res = []
    for table in SQLModel.metadata.tables.values():
        res.append(DropTable(table, if_exists=True).compile(dialect=dialect).__str__())
        res.append(CreateTable(table, if_not_exists=True).compile(dialect=dialect).__str__().replace(
            "" if origin_style else "\n", ""))
    res.append("")
    return ";".join(res)


def column(col_type: Any, comment: str | None = None, default: Any = "", *, nullable: bool = False,  # noqa: ANN401
           **kwargs: Any) -> dict[str, Column]:
    """返回列对象."""
    return {"sa_column": Column(col_type, server_default=default, nullable=nullable, comment=comment, **kwargs)}
