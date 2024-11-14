package zlhywlf.jupiter.tutorial;

import java.util.Scanner;

public class ArrayCount {
    public static void main(String[] args) {
        System.out.println("请输入一个整数:");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int[] arr = new int[10];
        while (a != 0) {
            arr[a % 10]++;
            a = a / 10;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%d 出现了 %d 次\n", i, arr[i]);
        }
    }
}
