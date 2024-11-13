package zlhywlf.jupiter.tutorial;

import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
    public static void main(String[] args) {
        Random random = new Random();
        int answer = random.nextInt(100) + 1;
        int count = 0;
        Scanner sc = new Scanner(System.in);
        for (; ; ) {
            System.out.println("请输入 1 ~ 100 之间的整数:");
            int num = sc.nextInt();
            count++;
            if (num > answer) {
                System.out.println("猜大了");
            } else if (num < answer) {
                System.out.println("猜小了");
            } else {
                System.out.println("猜对了");
                break;
            }
        }
        System.out.printf("猜了%d次结束游戏", count);
    }
}
