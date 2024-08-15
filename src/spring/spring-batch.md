# spring-batch

## 概述

### domain model

![git-model](./imgs/spring-batch-domain-model.svg)

### relational model

```mermaid
classDiagram
    class BATCH_JOB_EXECUTION {
        bigint VERSION
        bigint JOB_INSTANCE_ID
        datetime(6) CREATE_TIME
        datetime(6) START_TIME
        datetime(6) END_TIME
        varchar(10) STATUS
        varchar(2500) EXIT_CODE
        varchar(2500) EXIT_MESSAGE
        datetime(6) LAST_UPDATED
        bigint JOB_EXECUTION_ID
    }
    class BATCH_JOB_EXECUTION_CONTEXT {
        varchar(2500) SHORT_CONTEXT
        text SERIALIZED_CONTEXT
        bigint JOB_EXECUTION_ID
    }
    class BATCH_JOB_EXECUTION_PARAMS {
        bigint JOB_EXECUTION_ID
        varchar(100) PARAMETER_NAME
        varchar(100) PARAMETER_TYPE
        varchar(2500) PARAMETER_VALUE
        char(1) IDENTIFYING
    }
    class BATCH_JOB_EXECUTION_SEQ {
        bigint ID
        char(1) UNIQUE_KEY
    }
    class BATCH_JOB_INSTANCE {
        bigint VERSION
        varchar(100) JOB_NAME
        varchar(32) JOB_KEY
        bigint JOB_INSTANCE_ID
    }
    class BATCH_JOB_SEQ {
        bigint ID
        char(1) UNIQUE_KEY
    }
    class BATCH_STEP_EXECUTION {
        bigint VERSION
        varchar(100) STEP_NAME
        bigint JOB_EXECUTION_ID
        datetime(6) CREATE_TIME
        datetime(6) START_TIME
        datetime(6) END_TIME
        varchar(10) STATUS
        bigint COMMIT_COUNT
        bigint READ_COUNT
        bigint FILTER_COUNT
        bigint WRITE_COUNT
        bigint READ_SKIP_COUNT
        bigint WRITE_SKIP_COUNT
        bigint PROCESS_SKIP_COUNT
        bigint ROLLBACK_COUNT
        varchar(2500) EXIT_CODE
        varchar(2500) EXIT_MESSAGE
        datetime(6) LAST_UPDATED
        bigint STEP_EXECUTION_ID
    }
    class BATCH_STEP_EXECUTION_CONTEXT {
        varchar(2500) SHORT_CONTEXT
        text SERIALIZED_CONTEXT
        bigint STEP_EXECUTION_ID
    }
    class BATCH_STEP_EXECUTION_SEQ {
        bigint ID
        char(1) UNIQUE_KEY
    }

    BATCH_JOB_EXECUTION --> BATCH_JOB_INSTANCE: JOB_INSTANCE_ID
    BATCH_JOB_EXECUTION_CONTEXT --> BATCH_JOB_EXECUTION: JOB_EXECUTION_ID
    BATCH_JOB_EXECUTION_PARAMS --> BATCH_JOB_EXECUTION: JOB_EXECUTION_ID
    BATCH_STEP_EXECUTION --> BATCH_JOB_EXECUTION: JOB_EXECUTION_ID
    BATCH_STEP_EXECUTION_CONTEXT --> BATCH_STEP_EXECUTION: STEP_EXECUTION_ID

```

## 搭建环境

- 确保数据库 `batch` 已存在
- `spring.batch.jdbc.initialize-schema=always`: 表不存在则创建表

```properties
spring.datasource.driverClassName=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/batch
spring.datasource.username=root
spring.datasource.password=root
spring.batch.jdbc.initialize-schema=always
```
