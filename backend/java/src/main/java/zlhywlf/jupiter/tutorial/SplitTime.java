package zlhywlf.jupiter.tutorial;

import java.util.Scanner;

public class SplitTime {
    public static void main(String[] args) {
        System.out.println("请输入一个正整数秒数:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int hour = num / (60 * 60);
        int minute = num % (60 * 60) / 60;
        int second = num % 60;
        System.out.printf("hour=%d, minute=%d, second=%d", hour, minute, second);
    }
}
