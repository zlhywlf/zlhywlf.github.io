package zlhywlf.jupiter.tutorial;

import java.util.Scanner;

public class InputAndOutput {
    public static void main(String[] args) {
        // 1 声明变量记录姓名与年龄
        String name;
        int age;

        // 2 提示用户输入
        System.out.println("请输入姓名与年龄:");

        // 3 获取键盘输入(System.in)
        Scanner sc = new Scanner(System.in);

        // 4 利用用户的输入的值初始化变量
        name = sc.next();
        age = sc.nextInt();

        // 5 打印
        System.out.printf("name=%s, age=%s", name, age);
    }
}
