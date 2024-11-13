# 第一阶段 JavaSE

## 模块一 Java语言基础

### 任务一 初识计算机和Java语言

#### 计算机的基本概念

- 计算机(computer)俗称电脑, 是现代一种用于高级计算, 使用非常广泛的设备, 主要由计算机硬件和计算机软件两部分组成.
- 计算机硬件是客观存在的各种计算机相关设备, 而计算机软件是用于控制各种设备完成各种功能.

#### 常见的主要硬件

- 计算机硬件(computer hardware)主要包括: 中央处理器(CPU), 内存, 硬盘, 输入输出设备, 主板, 机箱和电源等辅助设备.

#### 主要硬件的详解

- CPU - 中央处理器(central processing unit).
    - 是计算机中最核心的部件, 类似人的大脑.
    - 是一台计算机运算核心和控制核心, 所有运算都由CPU完成.
    - 其功能主要是解释计算机指令以及处理计算机软件中的数据.
- 内存 - 是计算机中的储存部件, 内存(memory)也被称为内存储存器.
    - 用于暂时存放CPU中的运算数据, 以及与硬盘等外部存储器交换的数据.
    - CPU可以直接访问内存的数据, 而且效率比较高.
    - 容量小不能实现永久储存, 一旦断电会造成数据的丢失.
- 硬盘 - 是计算机中的存储部件.
    - 主要用于永久存放数据, 容量大且断电不丢失.
    - CPU不能直接访问硬盘中的数据, 若要访问则需要先加载到内存中.
- 输入输出设备.
    - 键盘叫标准输入设备, 显示器叫标准输出设备.

#### 常见的主要软件

- 计算机软件(computer software)可分为系统软件和应用软件, 系统软件就是操作系统, 是其他软件的基础.
- 主流操作系统: Windows/Unix/Linux/IOS/Android.

#### 计算机的体系结构

```mermaid
---
config:
    packet:
        showBits: false
        bitWidth: 12
---
packet-beta
0-31: "应用程序(application)"
32-63: "操作系统外壳 - GUI/命令(OS shell - KDE bash csh)"
64-95: "操作系统内核(OS kernel)"
96-127: "硬件(hardware)"
```

#### 计算机语言的发展

- 第一代语言: 机器语言 - 指令以二进制形式存在, 穿孔卡片等等
- 第二代语言: 汇编语言 - 使用助记符表示一条机器指令, ADD等等
- 第三代语言: 高级语言 - Java等等, [语言排行榜](https://www.tiobe.com/tiobe-index/)

#### Java语言的发展

##### 1991年(Java的诞生)

Java诞生于1991年5月，来源于名为"Oak"的项目，当时是由Sun公司的一个小工程师团队在设计和开发。该团队称自己为绿队(Green Term)
，团队成员有James Gosling、Mike Sheridan、 Patrick Naughton等人。James Gosling(詹姆斯高斯林)是项目负责人。Oak中文名是"橡树"
，橡树是力量和耐用性的象征。时间证明，这个名字是非常适合的，甚至是预言性的，尽管在1995年被迫改名为Java(
当时Oak已经被注册为另一个商标的一部分导致无法继续使用)。

##### 1995年

1995年当时在美国的硅谷有一个大会，号称是全球最顶尖的软件和硬件厂商都会在这个大会展示自家的产品，那么Sun公司的负责人James
Gosling也带着他的Oak项目去展示了。参会时一个偶然的机会让他发现他的项目名字早已被人注册商标了，没办法了只能重新给Oak取一个新的名字(
早在国外的时候人们对于版权看的非常重要)。James Gosling和他的团队经过讨论后最终决定重命名为Java(
爪哇，是印度尼西亚生产第一杯咖啡的一个岛屿名称。因为当时美国非常多的人喜欢喝咖啡)。同年Sun公司正式公开发布Java语言(
只是面世，还没有进行开发工具包JDK的发布，大家还无法使用)，并且第一次提出了"Write Once，Run Anywhere"(WORA,一次编写，到处运行)
的口号。《时代》杂志将Java评为了1995年十大最佳产品之一。

##### 1996年(JDK1.0)

1996年1月23日，Sun公司发布了Java1.0的第一个公开开发工具包，也就是JDK1.0，Java语言有了第一个正式版本的运行环境。JDK1.0提供了一个纯解释执行的Java虚拟机实现(
Sun Classic VM)
。JDK1.0版本的代表技术点有：Java虚拟机、Applet、AWT等。同年5月底，首届JavaOne大会在旧金山顺利举行，从此JavaOne成为了全世界数百万Java语言开发者一年一度的技术盛会。9月，已有大约8万网页应用采用了Java技术实现

##### 1997年(JDK1.1)

1997年2月19日，Sun公司发布了JDK1.1，Java里许多最基础的技术点(如JDBC等)
都是在JDK1.1版本中提出的，JDK1.1版本的技术代表有：JAR文件格式、JDBC、JavaBeans、RMI等。Java语言的语法也有了一定的增强，如内部类(
Inner Class)和反射(Reflection都是在这个版本出现的)。

- 内部类的概念
- Java Bean的概念
- JDBC
- RMI
- AWT事件模型被彻底重塑
- 反射仅支持Introspection，在运行时无法修改。（通过引入AccessibleObject类及其子类，如Field类，在J2SE 1.2中添加了反射性修改对象的能力。）
- Symantec公司为JavaSoft制作了Microsoft Windows平台上的 JIT（Just In Time）编译器
- 来自Taligent公司的国际化和Unicode支持

##### 1998年(JDK1.2)

1998年12月4日，JDK迎来了一个里程碑式的版本：工程代号为Playground的JDK1.2，Sun在这个版本中把Java技术体系拆分为三个方向，分别是面向桌面开发的J2SE、面向企业开发的J2EE、面向移动端开发的J2ME。在这个版本中出现了非常多的代表性技术，如EJB、Java
Plug-in、Java IDL、Swing等，并且这个版本中Java虚拟机第一次内置了JIT(Just In Time)即时编译器(JDK1.2中曾并存过三个虚拟机：Classic
VM、HotSpot VM和Exact VM, 其中Exact VM只在Solaris平台出现过；其余两款虚拟机都是内置了JIT即时编译器的，而之前版本所带的Classic
VM只能以外挂的形式实用即时编译器)。在语言和API层面上，Java添加了一系列Collections集合类等。

- Java plug-in(Java applet)
- Java IDL，一种用于CORBA互操作性的IDL实现
- Collections集合框架
- Swing图形API已集成到核心类中
- Sun的JVM首次配备了JIT编译器
- strictfp关键字
- 1999年(HotSpot)
- 1999年，HotSpot虚拟机诞生。

##### 2000年(JDK1.3)

2000年5月8日，JDK1.3版本发布。从此Sun公司维持着稳定的研发节奏： 大约每隔两年发布一个JDK的主版本，以动物命名，期间发布的各个修正版本则以昆虫作为工程代号。

- 包括了HotSpot JVM（HotSpot JVM于1999年4月首次发布，用于J2SE 1.2 JVM）
- 修改了RMI以支持与CORBA的可选兼容性
- Java Naming and Directory Interface (JNDI) 包含在核心库中（以前作为扩展提供）
- Java Platform Debugger Architecture (JPDA)
- JavaSound API
- Synthetic proxy classes

##### 2002年(JDK1.4)

2002年2月13日，JDK1.4发布，该版本是标志着Java真正走向成熟的一个版本。带来了非常多技术新特性，如正则表达式、异常链、NIO、日志类、XML解析器、XSLT转换器等。

- assert关键字
- 以Perl正则为模型的正则表达式支持
- Exception chaining，允许一个异常封装低级别的原始异常
- IPv6支持
- Non-blocking I/O (NIO)
- 日志接口(Logging API)
- 用于读取和写入JPEG和PNG等格式的图像I/O API
- 集成了XML解析器和XSLT处理器 (JAXP)
- 集成了安全和加密扩展（JCE、JSSE、JAAS）
- 包括了Java Web Start（Java Web Start 于2001年3月首次发布，适用于J2SE 1.3）

##### 2004年(JDK5)

2004年9月30日，JDK5发布， Sun公司从这个版本开始将产品版本号格式修改成了"JDK x"
，该版本在Java语法易用性上做了非常大的改进。如：自动装箱拆箱、泛型、动态注解、枚举、可变长参数、循环遍历(foreach)
等语法特性。这个版本改进了Java的内存模型(Java Memory Model，JMM)，提供了重要的JUC包(java.util.concurrent并发编程包)。

- 引入了泛型：避免了手动类型转换，使用类型擦除实现，在编译时删除泛型信息并使用Object替换，在实际使用时强转会原始类型
- 引入了注解，也叫原数据(metadata)，允许在类或方法等数据结构上做附加数据标记
- 原始类型的自动拆装箱
- 引入了枚举
- 可变长参数，允许方法的最后一个参数是可变长度
- for each 循环，用于迭代数组或Iterable集合
- 改进了Java多线程语义，增加了JUC(java.util.concurrent)包，增加了多个多线程工具，新的Java内存模型解决了先前规范的复杂性、有效性和性能问题
- 增加了静态import语法(import static)
- 自动为RMI（远程方法调用）对象生成方法stub
- Swing：新的look and fell，称为 synth
- 用于解析来自各种输入流和缓冲区的数据的扫描器类(Scanner class)
- 版本命名变更，1.5.0 表示开发者内部版本，JDK 5表示产品版本

##### 2006年(JDK6)

2006年12月11日，JDK6发布，在这个版本中，Sun公司终结了J2EE、J2SE、J2ME的产品线命名方式，启用JavaEE、JavaSE、JavaME的新命名格式来代替。JDK6应该是Java史上使用寿命最长的一个版本，主要原因是中间经历了代码复杂性增加、世界经济危机、Oracle对Sun进行收购。同年的JavaOne大会上，Sun公司宣布计划要把Java源代码开源，随后陆续的将JDK的各个部分在GPLv2(
GNU General Public Lcensev2)协议下公开了源码，并建立了OpenJDK组织对这些源代码进行独立管理。

- 脚本语言支持：用于与脚本语言紧密集成的通用API，以及内置的 Mozilla JavaScript Rhino 集成。
- Swing 的显着性能改进
- 通过JAX-WS改进了Web服务支持
- JDBC 4.0
- Java Compiler API：一种允许Java程序以编程方式选择和调用Java编译器的API
- JAXB升级到2.0版：包括集成 StAX 解析器
- 支持可插入注解（在编译期对代码中的注解进行处理，从而影响前端编译器的工作过程，常见时间是lombok）
- 许多GUI接口的改进
- JVM 改进包括：同步和编译器性能优化、新算法和对现有垃圾收集算法的升级以及应用程序启动性能

##### 2009年(JDK7)

2009年2月19日，JDK7的第一个里程碑版本发布。按JDK7最初的功能规划，一共会设置十个里程碑。从JDK7最原始的功能清单来看，它本应是一个包含许多重要改进的JDK版本，但现实不如人愿，由于Sun公司在商业上遇到了问题，没有精力去推动JDK7的研发工资，因此以下功能没能全在JDK7中完成实现：

- Lambda项目:支持Lambda表达式，支持函数式编程。(JDK 8)
- Jigsaw项目:虚拟机层面的模块化支持。(JDK 9)
- 动态语言支持:Java是静态语言，为其他运行在Java虛拟机上的动态语言提供支持。
- Garbage-First收集器。（JDK 8）
- Coin项目: Java语法细节进化。(部分JDK 8)

从JDK7 Update4开始， JavaSE的核心功能正式开始为MacOS X操作系统提供支持，并在JDK7 Update6中达到所有功能与MacOS
X完全兼容的程度；同时，JDK7 Update6还对ARM指令集架构提供了支持。至此，Sun官方提供的JDK可以运行于Windows(不含Windows 9x)
、Linux、Solaris和MacOS X操作系统上，支持ARM、x86\x86-64和SPARC指令集架构，JDK7也是可以支持Windows XP操作系统的最后一个版本。
2009年4月20日，Oracle公司以74亿美元的价格收购了市值曾超过2000亿美元的Sun公司。一年后詹姆斯高斯林宣布离职

- 动态语言支持，使用新的invokedynamic字节码，遵循当前在多语言虚拟机上完成的原型设计工作
- 压缩的 64 位指针（在Java 6中可用 -XX:+UseCompressedOops开启）
- Coin项目：
- switch语句中使用String
- 自动管理资源的try-with-resources
- 改进了实例创建时的类型推断菱形运算符<>
- 简化了可变参语法
- 二进制的数字表示 byte aByte = (byte)0b00100001;
- 允许在数字中使用下划线
- 使用改进的类型检查捕获多种异常类型并重新抛出异常
- JDBC4.1
- jcmd工具，用来代替jps
- fork/join框架
- 并发实用工具
- 新的文件I/O库增加了对多个文件系统、文件元数据和符号链接的支持。新包是java.nio.file、java.nio.file.attribute 和
  java.nio.file.spi
- Java Mission Control
- 使用Timsort替代集合和数组中的归并排序
- 对椭圆曲线密码学的库级支持
- 用于Java 2D的XRender管道，可改进对现代GPU特定功能的处理
- 实现6u10中不受支持的图形API
- 增强了对新网络协议的库级支持，包括SCTP和Sockets Direct Protocol
- XML和Unicode的上游更新
- Java deployment rule sets

##### 2014年(JDK8)

2014年3月18日，JDK8发布，提供了Lambda表达式支持、内置Nashorn JavaScript引擎支持、新的时间日期API、彻底移除HotSpot永久代。

- Lambda表达式
- stream操作
- HashMap改进
- Nashorn项目，允许开发人员在应用程序中嵌入JavaScript代码
- 重复注解
- 类型注解
- 无符号整型
- 新的日期和时间API
- 静态链接的JNI库
- 启动JavaFX应用程序（直接启动JavaFX应用程序JAR）
- 删除永久代

2017年(JDK9) 2017年9月21日，JDK9发布，带来了Jigsaw虚拟机模块化支持技术。从此每六个JDK大版本划出一个三年支持的LTS版本(Long
Term Support)，普通版本只有六个月生命周期。JDK8和JDK11是LTS版本。下一个就是要在2021年发布的JDK17了。

- Jigsaw项目下JDK的模块化（Java 平台模块系统）
- G1成为了默认的垃圾回收器
- 统一了 JVM/GC 日志
- HTTP/2 Client
- 更方便的集合工厂方法，以前大多使用Guava类库
- docker方便的支持
- 货币API
- 实现了响应式流
- 新的Flow类
- 并发工具的更新
- 更加紧凑的字符串
- HiDPI graphics：自动缩放和调整大小
- 变量句柄(Variable handles)：用来代替java.util.concurrent.atomic和sun.misc.Unsafe操作的等价物
- Coin语法改进项目继续进行
- jshell：Java Shell：JShell 是Java语言的REPL（读取-执行-打印循环）命令行界面
- XML目录
- jlink：Java 链接器：创建一个工具，可以将一组模块及其依赖项组装和优化为自定义运行时映像。它有效地允许生成一个完全可用的可执行文件，包括运行它的
  JVM。
- 提前编译：GraalVM 提供的提前编译。

2018年(JDK10、JDK11)
2018年3月20日，JDK10发布，该版本主要是内部重构。同年，Oracle公司宣告JavaEE成为历史名词。同年，JavaOne大会成为最后一届。

- 局部变量类型推断 var 关键字
- GC接口：通过引入干净的垃圾收集器 (GC) 接口来改进不同垃圾收集器的源代码隔离
- G1并行full GC
- CDS：为了改善启动和占用空间，扩展现有的类数据共享 (“CDS”) 功能以允许将应用程序类放置在共享存档中
- 线程的本地握手：一种无需执行全局VM安全点即可在线程上执行回调的方法。使停止单个线程而不只是所有线程或不停止所有线程成为可能且成本低廉
- 移除了javah工具，被JDK 8中添加的javac高级功能取代
- 额外的 Unicode 语言标签扩展
- 替代内存设备上的堆分配：启用HotSpot VM以在用户指定的备用内存设备（例如 NV-DIMM）上分配Java对象堆
- 实验性基于 Java 的 JIT 编译器
- 基于时间的发布版本控制：针对当前和未来基于时间的发布模型，修订 Java SE 平台和 JDK 的版本字符串方案以及相关版本控制信息

2018年9月25日，LTS版本的JDK11发布，ZGC出现。同时Oracle公司调整了JDK授权许可证。OpenJDK免费版只有半年支持。OracleJDK在生产环境必须付费，但有三年支持。迫使商业用户要么不断升级JDK版本，要么去购买商业支持。

- 嵌套访问控制，在java 11之前嵌套类的访问，是编译器通过生成匿名的public桥接方法实现嵌套类之间的访问私有成员控制，这种在使用反射时无法生成桥接方法而导致不能直接访问嵌套类私有成员。java
  11中通过虚拟机指令级别的支持，运行嵌套类之间直接访问私有成员。Class类新增了getNestHost，getNestMembers方法
- 增加了一个新的常量池类型：CONSTANT_Dynamic，解决java 7中引入的invokeddynamic协议中俩个复杂的常量池及引导时的校验这种麻烦的场景，改善程序性能和简化编译器逻辑
- 引入了一个消极的垃圾回收器Epsilon，分配有限的资源，不进行垃圾回收操作，可用于性能测试和短生命周期任务
- 移除了Java EE 和 CORBA 模块
- Java 11 对 Java 9 中引入并在 Java 10 中进行了更新的 Http Client API 进行了标准化，在前两个版本中进行孵化的同时，Http
  Client 几乎被完全重写，并且现在完全支持异步非阻塞
- var关键字可以在Lambda表达式中使用
- 引入了新的秘钥协议方案 Curve25519 和 Curve448
- 支持Unicode 10
- 开源了之前是商业版的飞行记录仪
- 实现 RFC 7539的ChaCha20 and ChaCha20-Poly1305加密算法
- 可以直接运行单个源码文件，而无需编译。简化了小程序的运行流程
- 通过JVMTI的SampledObjectAlloc回调提供了一个开销低的heap分析方式
- 支持TLS 1.3
- 提供了实验性的ZGC垃圾收集器
- 废除Nashorn javascript引擎，在后续版本准备移除掉，有需要的可以考虑使用GraalVM
- 废除了pack200以及unpack200工具以及java.util.jar中的Pack200
  API。Pack200主要是用来压缩jar包的工具，不过由于网络下载速度的提升以及java9引入模块化系统之后不再依赖Pack200，因此这个版本将其移除掉

> 接下来的JDK12、JDK13、JDK14、JDK15、JDK16、JDK18、JDK19都是过渡产品，不太受开发者待见。

##### 2019年(JDK12、JDK13)

2019年，JDK12发布，引入了Shenandoah垃圾收集器，作为首个非Oracle公司开发的垃圾收集器，由于目标与Oracle在JDK11引入的ZGC几乎一致，存在竞争关系。OracleJDK
12把相关代码通过条件编译强行踢出，使其无法在OracleJDK中使用。

- 提供了实验性的Shenandoah垃圾收集器
- 在 JDK 源代码中添加一套基本的微基准测试，让开发人员可以轻松地运行现有微基准测试并创建新的微基准测试
- 扩展了switch语句，使之可以合并多个分支，或用于返回语句。处于试验阶段
- 引入 API 来对关键类文件和运行时工件的名义描述建模，特别是可从常量池加载的常量
- 之前JDK有两个关于aarch64的实现，现在只保留一个
- 在 64 位平台上编译JDK时生成一份默认的 CDS 存档文件方便大家使用
- JDK 12之前G1进行回收时一旦确定了CSet，就不会停止。这是STW的时间可能会超出预期停顿时间。JDK
  12使用混合回收，当选择了一个比较大的CSet时将其分为强制部分和可选部分，当回收完强制部分还有剩余时间时。才回收可选部分。随着预测进行，可选部分会越来越小。如果预测变得不准确，集合将会再次分为两部分
- 增强 G1 垃圾收集器在空闲时自动将 Java 堆内存返还给操作系统。G1目前只有在full GC或者concurrent
  cycle的时候才会归还内存，由于这两个场景都是G1极力避免发生的。这时在付费的容器环境中极为不利。G1
  将在应用程序不活动期间，定期尝试继续或触发并发循环，以确定总体 Java 堆使用情况。这将导致它自动将 Java
  堆中未使用的部分返回给操作系统。或者，在用户控制下，可以执行full GC 以最大化返回的内存量

2019年9月，JDK13发布，动态CDS归档；ZGC：取消提交未使用存储器；重新实现旧版Socket API；Switch表达式(预览阶段)

- 之前需要用户手动的创建CDS，然后使用CDS运行应用。JDK 13中可以在应用第一次运行期间自动生成CDS 存档
- 增强 ZGC 将未使用的堆内存返回给操作系统
- 重新实现了传统的Socket API。将java.net.Socket和java.net.ServerSocketAPI使用的底层实现替换为更简单、更现代、易于维护和调试的实现
- 增强的switch表达式，第二次预览阶段
- 引入了文本块语法，预览阶段

##### 2020年(JDK14、JDK15)

2020年3月，JDK14发布，主要包含16个功能改进和漏洞修复。

- 增强了instanceof功能，简化了使用。预览阶段
- 增加了一个java的应用打包工具，可以打包成各平台的应用格式。孵化阶段
- 实现了G1垃圾收集器的NUMA-aware内存分配，以提升在大型机器上的性能
- JDK11引入了JFR，使用的时候先dump到磁盘上然后再分析；而在JDK14则支持stream方式来订阅JFR事件进行持续性的监控
- 支持MappedByteBuffer访问non-volatile memory (NVM)
- 增加了空指针异常的提示信息，便于定位空指针位置及原因，需要通过-XX:+ShowCodeDetailsInExceptionMessages开启
- 引入了新的数据载体类型 record，简化了用于存储数据的类代码，通过编译器实现，编译后的代码其实是继承了java.lang.Record
- 增强的switch表达式不再是预览阶段了，进入了正式版本
- 弃用 Solaris/SPARC、Solaris/x64 和 Linux/SPARC 端口，在未来的发行版中删除它们
- 移除了并发标记清除 (CMS) 垃圾收集器
- ZGC支持了macOS系统
- ZGC支持了Windows系统
- 弃用 Parallel Scavenge 和 Serial Old 垃圾收集算法的组合
- 删除pack200和unpack200工具，以及Pack200在APIjava.util.jar包。这些工具和 API在 Java SE 11中已被弃用
- 文本块语法进入二次预览阶段
- 引入 API 以允许 Java 程序安全有效地访问 Java 堆之外的外部内存。孵化阶段

2020年9月，JDK15发布，主要是安全更新和bug修复。

- 使用爱德华兹曲线数字签名算法 (EdDSA) 实现加密签名
- 引入了两个关键字sealed和permits。实现了密封类继承语法。处于预览阶段。在过去的java语法中，类可以被自由的继承。在新的语法中，可以用sealed密封一个类，然后使用permits限制可以继承这个类的子类
- JDK15引入了隐藏类，同时废弃了非标准的sun.misc.Unsafe::defineAnonymousClass使用Lookup::
  defineHiddenClass，目标是为框架提供在运行时生成内部的class
- 删除 Nashorn JavaScript 脚本引擎和 API 以及该jjs 工具。引擎、API 和工具在 Java 11中已被弃用
- 该特性使用更简单及更现代的方式重新实现了java.net.DatagramSocket及java.net.MulticastSocket以方便更好的维护及debug，新的实现将会更容易支持虚拟线程
- 禁用和弃用了偏向锁。随着JUC包的引入，Synchronized关键字的使用场景减少，偏向锁的收益不再明显。偏向锁定在同步子系统中引入了大量复杂的代码，并且对其他
  HotSpot 组件也有侵入性。这种复杂性是理解代码各个部分的障碍，也是在同步子系统内进行重大设计更改的障碍。为此，我们希望禁用、弃用并最终删除对偏向锁定的支持
- 增强的instanceof进入二次预览阶段
- ZGC现可被引入生产环境
- 文本块语法结束了预览阶段，进入了正式版本
- Shenandoah现可用于生产环境
- Solaris and SPARC 移植内容在JDK14被标记为废弃，在JDK15版本正式移除
- 外部内存访问API进入二次孵化阶段
- record类型进入二次预览阶段
- JDK15废弃了RMI Activation，后续将被移除

##### 2021年(JDK16、JDK17)

2021年3月，JDK16发布，主要包含17个更新。

- 提供了一套新的向量计算API，并且向量计算运行时可以尽量编译到硬件支持的最佳指令上
- 允许在 JDK C++ 源代码中使用 C++14 语言特性，并给出关于哪些特性可以在 HotSpot 代码中使用的具体指导
- 将 OpenJDK 社区的源代码存储库从 Mercurial (hg) 迁移到 Git
- 在GitHub上托管OpenJDK 社区的 Git 存储库。与JEP 357（从 Mercurial 迁移到 Git）一致，这会将所有单存储库 OpenJDK 项目迁移到
  GitHub，包括版本 11 及更高版本的JDK 功能版本和JDK 更新版本
- 将 ZGC 线程堆栈处理从安全点移动到并发阶段
- 将 Unix 域 ( AF_UNIX) 套接字支持添加到包中的套接字通道和服务器套接字通道API java.nio.channels。扩展继承的通道机制以支持
  Unix 域套接字通道和服务器套接字通道
- 将 JDK 移植到 Alpine Linux
- 更及时地将未使用的 HotSpot 类元数据（即元空间）内存返还给操作系统，减少元空间占用空间，并简化元空间代码以降低维护成本
- 将 JDK 移植到 Windows/AArch64
- 从 Java 1.1 开始，Java 就支持通过Java 本地接口 (JNI)调用本地方法，但这条路径一直是艰难而脆弱的。外部链接器
  API（孵化阶段）提供对本机代码的静态类型、纯 Java 访问。此 API 与外部内存 API ( JEP 393 )一起，将大大简化绑定到本机库的其他容易出错的过程
- 当对原始值类型及其包装类型使用synchronize时发出警告
- 提供jpackage用于打包自包含 Java 应用程序的工具。该jpackage工具是由JEP 343在 JDK 14 中作为孵化工具引入的
- 外部内存访问API进入三次孵化阶段
- 增强的instanceof进入了正式版本
- record类型进入了正式版本
- 默认情况下，强封装 JDK 的所有内部元素，除了关键的内部 API，如sun.misc.Unsafe. 允许最终用户选择自 JDK 9 以来一直默认的宽松强封装
- sealed进入第二次预览阶段

2021年9月，LTS版本的JDK17发布，主要包含14个更新。

- 浮点运算始终严格，而不是同时具有严格的浮点语义 ( strictfp)和略有不同的默认浮点语义。这将恢复语言和 VM 的原始浮点语义，匹配
  Java SE 1.2 中引入严格和默认浮点模式之前的语义
- 增强型伪随机数生成器
- 使用 Apple Metal API 为 macOS 实现 Java 2D 内部渲染管道，作为现有管道的替代方案，现有管道使用已弃用的 Apple OpenGL API
- 将 JDK 移植到 macOS/AArch64
- 弃用 Applet API 以进行删除。它基本上无关紧要，因为所有 Web 浏览器供应商都已取消对 Java 浏览器插件的支持或宣布了这样做的计划
- 强烈封装 JDK 的所有内部元素，除了关键的内部 API，如sun.misc.Unsafe. 不再可能通过单个命令行选项来放松内部元素的强封装，就像在
  JDK 9 到 JDK 16 中那样
- 将switch表达式与增强的instanceof进行结合，可以一起使用删除远程方法调用 (RMI) 激活机制，同时保留 RMI 的其余部分
- sealed进入正式版本
- 删除实验性的基于 Java 的提前 (AOT)和即时 (JIT) 编译器。该编译器自推出以来几乎没有什么用处，维护它所需的工作量很大。保留实验性的
  Java 级 JVM 编译器接口 (JVMCI)，以便开发人员可以继续使用外部构建的编译器版本进行 JIT 编译
- 提供外部函数和内存 API（孵化阶段），Java 程序可以通过该 API 与 Java 运行时之外的代码和数据进行互操作。通过有效调用外部函数（即
  JVM 之外的代码），以及安全地访问外部内存（即不由 JVM 管理的内存），API 使 Java 程序能够调用本地库和处理本地数据，而不需要通过JNI
- 向量计算API进入二次孵化阶段
- 特定于上下文的反序列化过滤器

##### 2022年(JDK18、JDK19)

2022年3月22日，JDK18发布。

- 将UTF-8指定为标准Java API的默认字符集
- 简单Web服务器
- Java API文档中支持Snippets代码片段
- 重新实现反射核心机制(Method Handles)
- 矢量API(三次孵化中)
- 定义全新的互联网地址解析SPI
- 外部函数和内存API(二次孵化中)
- Switch模式匹配(二次预览中)
- 弃用Finalization

2022年9月20日，JDK19发布。

- 记录模式(一次预览中)
- Switch模式匹配(三次预览中)
- 外部函数和内存API(一次预览中)
- 矢量API(四次孵化中)
- Linux/RISC-V端口
- 虚拟线程(一次预览中)
- 结构化并发(一次孵化中)

#### Java语言的主要版本

- java SE (Java platform, standard edition)
    - 称为 `Java平台标准版`, 是Java平台的基础.
    - java SE 包含了运行Java应用所需要的基础环境和核心类库.
    - java SE 还定义了基于桌面应用的基础类库.
- java EE (Java platform, enterprise edition)
    - 称为 `Java平台企业版`.
    - java EE 构建在 java SE 基础之上, 用于构建企业级应用.
- java ME (Java platform, micro edition)
    - 为机顶盒, 移动电话和PDA等嵌入式消费电子设备提供的Java解决方案.
    - 已淘汰.

#### 开发工具的下载和安装

see [环境准备](./index#环境准备)

#### 相关概念

- JDK - Java开发工具包(java development kit)
    - jdk 目录
        - bin - 工具命令
        - conf - 配置文件
        - include - 平台头文件
        - jmods - 模块
        - legal - 模块授权文档
        - lib - 补充jar包和源代码
- JRE - java运行时环境(java runtime environment)

#### 编写Java程序的流程

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/HelloWorld.java

#### 常用的快捷键和注释

略(计算机快捷键与java注释)

#### 环境变量的配置

see [环境准备](./index#环境准备)

#### 跨平台原理

Java字节码可以通过JVM翻译为具体平台能够执行的机器指令. 由于定义了JVM规范, 而且不同操作系统大多提供了JVM实现,
才使得相同的字节码文件可以在不同的操作系统上运行.

### 任务二 变量和数据类型

#### 变量的基本概念

- 当需要在程序中记录单个数据内容时, 则声明一个变量, 而声明变量的本质就是在内存申请一个存储单元, 由于该储存单元中的数据内容可以改变,
  因此称为 `变量`.
- 由于存放的数据内容大小不一样, 导致所需存储单元的大小不一样, 在java语言中使用数据类型加以描述, 为了便于下次访问还需要给该变量指定一个名字,
  用于记录该变量对应的存储单元.

#### 变量的声明和使用

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/Variable.java

#### 变量使用的注意事项

- 使用变量之前需要声明并作了初始化
- 类中成员变量会作默认初始化
- 变量不能重复声明

#### 标识符的命名法则

- 由数字, 字母, 下划线以及$等组成, 不能以数字开头.
- 不能使用Java语言关键字.
- 变量区分大小写,无长度限制.
- 见名知意.

#### 变量输入输出的案例实现

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/InputAndOutput.java

#### 变量输入输出案例的优化和手册介绍

略

#### 数据类型的分类

- 基本数据类型
    - byte
    - short
    - int
    - long
    - float
    - double
    - boolean
    - char
- 引用数据类型
    - 数组
    - 类
    - 接口
    - 枚举
    - 注解
    - 记录

#### 常用的进制

- 十进制
- 二进制
- 八进制
- 十六进制

#### 正十进制转换为二进制的方式

- 除2取余法
  ```plantuml
  45 / 2 = 22 ---- 1
  22 / 2 = 11 ---- 0
  11 / 2 = 5  ---- 1
  5  / 2 = 2  ---- 1
  2  / 2 = 1  ---- 0
  1  / 2 = 0  ---- 1
  
  45 ==> 101101
  ```
- 拆分法, 将十进制整数拆分为若干个二进制权重的和
  ```plantuml
  45 = 1 x 2^5 + 0 x 2^4 + 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 1 x 2^0
     = 32      + 0       + 8       + 4       + 0       + 1
  
  45 ==> 101101
  ```

#### 正二进制转化十进制的方式

- 加权法, 使用二进制中的每个数字乘以当前位的权重再累加起来
  ```plantuml
  101101 ==> 1 x 2^5 + 0 x 2^4 + 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 1 x 2^0
         ==> 32      + 0       + 8       + 4       + 0       + 1
         ==> 45
  ```

#### 负十进制转换为二进制的方式

- 先将十进制的绝对值转换为二进制, 然后进行按位取反再加一
  ```plantuml
   45 ==> 101101 ==> 010010 ==> 010011
  
  -45 ==> 010011
  ```

#### 负二进制转换为十进制的方式

- 先减去一, 再按位取反, 转为十进制数后添加负号
  ```plantuml
  010011 ==> 010010 ==> 101101 ==> 45
  
  010011 ==> -45
  ```

#### 单个字节所能表示的整数范围

- 在计算机中单个字节表示八位二进制位, 其中最高位(最左边)代表符号位, 使用0代表非负数, 使用1代表负数
    - 0111 1111 ==> 127
    - 1111 1111 ==> -128

#### 整数类型的概念

- byte: 1 个字节
- short: 2 个字节
- int: 4 个字节
- long: 8 个字节

#### 整数类型的编程使用

- 整数字面量默认为 int 类型, 赋值 long 类型需要在数字末尾添加 `l` 或者 `L`

#### 整数类型的笔试考点

- 大整数类型转为小整数类型

#### 浮点类型的概念

- float: 4个字节, 7位有效数字
- double: 8个字节, 15位有效数字

#### 浮点类型的编程使用

- 浮点字面量默认为 double 类型, 赋值 float 类型需要在数字末尾添加 `f` 或者 `F`

#### 布尔类型的概念和编程使用

- boolean: 值只有 `true` 与 `false`

#### 字符类型的概念

- char: 2个字节, 无符号位, 描述单个字符, 'A'

#### 字符类型和编码的使用

[ASCII码](https://www.asciim.cn/)

#### Unicode字符集的概念和使用

[Unicode 符号表](https://symbl.cc/cn/unicode-table/)

#### 转义字符的概念和使用

- \" ==> "
- \' ==> '
- \t ==> 制表符
- \n ==> 换行符

#### 自动类型转换的概念和使用

- 小类型到大类型

#### 强制类型转换的概念后使用

- 大类型到小类型

### 任务三 运算符

#### 算数运算符的概念和使用

- \+: 加法 ==> 1+1 ==> 2
- \-: 减法 ==> 1-1 ==> 0
- \*: 乘法 ==> 2*2 ==> 4
- /: 除法 ==> 9/3 ==> 3
- %: 取模/取余 ==> 3%2 ==> 1

#### 算数运算符的注意事项

- 两个整数相除, 结果只保留整数部分, 例如: 5/2 ==> 2
- 0 不能作除数

#### 算数运算符实现时间拆分

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/SplitTime.java

#### 字符串连接符的概念和使用

- \+: 只要该符号两边有一个是字符串类型时, 拼接字符 ==> "A"+"B" ==> "AB"

#### 关系(比较)运算符的概念和使用

- \>: 是否大于 ==> 1>1 ==> false
- <: 是否小于 ==> 1<1 ==> false
- ==: 是否等于 ==> 1==1 ==> true
- <=: 是否小于或等于 ==> 1<=1 ==> true
- \>=: 是否大于或等于 ==> 1>=1 ==> true
- !=: 是否不等于 ==> 1!=1 ==> false

#### 关系运算符实现负数判断

- 判断输入数字是否小于0

#### 自增/自减运算符的概念和使用

- ++: 自身数值加1 int a=1 ==> a++ 或者 ++a ==> 2
- \--: 自身数值减1 int a=1 ==> a-- 或者 --a ==> 0

#### 前后自增/自减的区别

- a++: 先使用值 1, 在自增 int a=1 ==> 1 + a++ ==> 2
- ++a: 先自增, 再使用值, 即 2 int a=1 ==> 1 + ++a ==> 3
- a--: 先使用值 1, 在自减 int a=1 ==> 1 + a-- ==> 2
- --a: 先自减, 再使用值, 即 0 int a=1 ==> 1 + --a ==> 1

#### 自增/自减运算符的笔试考点

- 前后自增/自减的区别
- 只能用于变量, 不能用于字面量

#### 逻辑运算符的概念和使用

- &&: 同真为真, 一假为假
- ||: 一真为真, 同假为假
- ! : 真为假, 假为真

#### 逻辑运算符的短路特性

- &&: 若第一个表达式为假则跳过第二个表达式
- ||: 若第一个表达式为真则跳过第二个表达式

#### 逻辑原算符判断三位数

- 判断输入的数字是否在 100 与 999 之间
- 逻辑运算符主要用于连接多个关系运算符作为最终运算的表达式

#### 三目运算符的概念和使用

- 条件表达式 ? 表达式1 : 表达式2

#### 三目运算符查找最大值

- 输入的两个数字中取最大值
- max = a > b ? a : b

#### 赋值运算符的概念和使用

- =: 将右边的数据赋值给左边的变量, 表达式的结果即右边的值, 即 `a=5` 表达式的结果为 `5`
- +=: a+=1 等价于 a = a + 1 以此类推到其他算数运算符

#### 赋值运算符的考点

- a == 2 推荐写成 2 == a

#### 移位运算符

- <<: 左移运算符, 将数据的二进制位向左移动, 右边使用0补充
- \>>: 右移运算符, 将数据的二进制位向右移动, 左边使用符号位补充
- \>>>: 逻辑右移运算符, 将数据的二进制位向右移动, 左边使用0补充

#### 移位运算符的使用

略

#### 位运算符的概念

- &: 按位与, 同1为1, 有0为0
- |: 按位或, 有1为1, 同0为0
- ~: 按位取反, 1为0, 0为1
- ^: 按位异或, 相同为0, 不同为1

#### 位运算符的使用

略

#### 运算符的优先级

| Operators            | Precedence                              |
|----------------------|-----------------------------------------|
| postfix              | expr++ expr--                           |
| unary                | ++expr --expr +expr -expr ~ !           |
| multiplicative       | * / %                                   |
| additive             | + -                                     |
| shift                | << >> >>>                               |
| relational           | < > <= >= instanceof                    |
| equality             | == !=                                   |
| bitwise AND          | &                                       |
| bitwise exclusive OR | ^                                       |
| bitwise inclusive OR | \|                                      |
| logical AND          | &&                                      |
| logical OR           | \|\|                                    |
| ternary              | ? :                                     |
| assignment           | = += -= *= /= %= &= ^= \|= <<= >>= >>>= |

### 流程控制语句

#### 分支结构的概念

- 当需要进行条件判断并做出先择的时候,使用分支结构

#### if分支结构的概念和使用

```plantuml
if(条件表达式){
条件成立执行语句;
}
```

#### if分支结构查找最大值的方式

略

#### if else分支结构的概念和使用

```plantuml
if(条件表达式){
条件成立执行语句;
}else{
条件不成立执行语句;
}
```

#### if else分支结构判断负数和非负数

略

#### if else if else分支结构的概念和使用

```plantuml
if(条件表达式1){
条件1成立执行语句;
}else if(条件表达式2){
条件2成立执行语句;
}else{
条件都不成立执行语句;
}
```

#### 个人所得税的计算方式

略

#### 出租车计费系统的实现

略

#### if分支结构实现等级判断

略

#### switch case分支结构的概念

```plantuml
switch(变量/表达式){
case 字面量1: 语句; break;
case 字面量2 -> {语句;}
...
default: 语句;
}
```

#### switch case分支结构实现等级判断

略

#### switch case实现字符界面

略

#### 循环结构的概念

- 希望重复执行一段代码, 就需要使用循环结构

#### for循环的概念和使用

```plantuml
for(初始化表达式;条件表达式;修改初始值表达式){
循环体;
}
```

#### for循环打印奇数

略

#### for循环实现累加和

略

#### for循环实现水仙花数的打印

略

#### continue关键字

结束本次循环, 开始下一次循环

#### break关键字模拟聊天的框架实现

跳出当前循环

#### break关键字模拟聊天的完整实现

略

#### 猜数字游戏的框架实现

略

#### 猜数字游戏的完整实现

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/GuessNumber.java

#### 双重for循环的由来

略

#### 双重for循环的执行流程和特点

- 外层循环用于控制打印的行数, 内存循环用于控制打印的列数
- 若需要打印多行多列时, 使用双重循环

#### 各种星星图案的打印

略

#### 九九乘法表的打印

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/MultiplicationTable.java

#### 素数打印的实现

略

#### 素数打印的优化

略

#### while循环的概念和使用

```plantuml
while(条件表达式){
循环体;
}
```

#### while循环实现调和数列的累加和

略

#### while循环和for循环的比较

- while循环和for循环可以互换, 推荐使用for循环
- while循环适合明确循环条件但不明确循环次数的场景中
- for循环适合明确循环次数或范围的场景中

#### while循环实现反向输出

略

#### do-while循环的概念和使用

- do-while循环主要使用于至少执行一次循环体的场景中

```plantuml
do{
循环体;
}while(条件表达式)
```

#### do-while循环模拟任务检查

略

#### 循环的笔试考点

略
