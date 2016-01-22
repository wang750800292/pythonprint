### 提升mysql性能
### 数据库设计
#### 标准化
* 1) 所有的“对象”都在它自己的table中，没有冗余。
* 2) 数据库通常由E-R图生成。
* 3) 简洁，更新属性通常只需要更新很少的记录。
* 4) Join操作比较耗时。
* 5) Select，sort优化措施比较少。
* 6) 适用于OLTP应用。

#### 数据类型
* 选择合适的数据类型，数字、字符串、文本
* 用尽量小得数据类型
* 尽量使用not null
* 变长（varchar，text，blob）、定长合理选择

#### 创建索引
* 合理有选择性的使用索引，使用频率低，使用不到的字段不建立索引
* 避免重复索引
* 索引越短越好，最好用integer
* 查询时使用到索引，使用匹配数据库定义的类型查询数据
* 相近的比随机的好，auto increment比uuid要好
* 使用mysql内部缓存功能
* select一个字段代替*
* 使用join时，字段类型保持一致
* 数据库读写分离，垂直分割，水平分割
* myisam表锁，innodb是行锁，并且支持事务

### 服务端设置优化
* --character-set：如果是单一语言使用简单的character set例如latin1。尽量少用Utf-8，utf-8占用空间较多。
* --memlock：锁定MySQL只能运行在内存中，避免swapping，但是如果内存不够时有可能出现错误。
* --max_allowed_packet：要足够大，以适应比较大的SQL查询，对性能没有太大影响，主要是避免出现packet错误。
* --max_connections：server允许的最大连接。太大的话会出现out of memory。
* --table_cache：MySQL在同一时间保持打开的table的数量。打开table开销比较大。一般设置为512。
* --query_cache_size： 用于缓存查询的内存大小。
* --datadir：mysql存放数据的根目录，和安装文件分开在不同的磁盘可以提高一点性能。

### 存储引擎优化
#### myisam
* MyISAM管理非事务表。它提供高速存储和检索，以及全文搜索能力
* 不支持事务，宕机会破坏表
* 使用较小的内存和磁盘空间
* 基于表的锁，并发更新数据会出现严重性能问题
* MySQL只缓存Index，数据由OS缓存

#### innodb
* 支持事务，ACID，外键。
* Row level locks。 
* 支持不同的隔离级别。
* 和MyISAM相比需要较多的内存和磁盘空间。
* 没有键压缩。
* 数据和索引都缓存在内存hash表中。


