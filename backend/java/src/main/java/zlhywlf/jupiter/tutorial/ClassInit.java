package zlhywlf.jupiter.tutorial;

public class ClassInit {
    {
        System.out.println("2 构造块");
    }

    static {
        System.out.println("1 静态代码块");
    }

    ClassInit() {
        System.out.println("3 构造方法");
    }

    public static void main(String[] args) {
        new ClassInit();
    }
}
