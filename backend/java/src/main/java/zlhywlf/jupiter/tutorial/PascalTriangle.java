package zlhywlf.jupiter.tutorial;

import java.util.Arrays;

public class PascalTriangle {
    public static void main(String[] args) {
        int row = 10;
        int[][] arr = new int[row][];
        for (int i = 0; i < row; i++) {
            arr[i] = new int[i + 1];
            for (int j = 0; j <= i; j++) {
                if (0 == j || i == j) {
                    arr[i][j] = 1;
                    continue;
                }
                arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1];
            }
            System.out.println(Arrays.toString(arr[i]));
        }
    }
}
