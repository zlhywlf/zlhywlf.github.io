# SQL

## DCL(data control language)

[Reference](https://dev.mysql.com/doc/refman/8.4/en/account-management-statements.html)

### 创建用户

```sql
CREATE USER 'foo'@'localhost' IDENTIFIED BY 'password';
```

### 授予用户权限

```sql
GRANT ALL ON db.* TO 'foo'@'localhost';
```

### 回收用户权限

```sql
REVOKE ALL ON db_name.* FROM 'foo'@'localhost';
```

## DDL(data definition language)

[Reference](https://dev.mysql.com/doc/refman/8.4/en/sql-data-definition-statements.html)

[course](./course.md)

## DML(data manipulation language)

[Reference](https://dev.mysql.com/doc/refman/8.4/en/sql-data-manipulation-statements.html)

[course](./course.md)
