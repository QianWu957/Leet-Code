class Main {
 public static void main(String[] args) {
        int[][] forest = {{1,2,3},{2,1,2},{3,1,1}};
        int number = 3;
  System.out.println(forestPlanteed(forest, number));
 }

    public static int[][] preSum;
    public static int forestPlanteed(int[][] forest, int number) {
        int mod = (int)Math.pow(10,9) + 7;
        int row = forest.length;
        int col = forest[0].length;
        preSum = new int[row][col];

        if (forest[0][0] == 2) preSum[0][0] = 1;
        for (int i = 1; i < row; i++) {
            if (forest[i][0] == 2) {
                preSum[i][0] = preSum[i - 1][0] + 1;
            } else {
                preSum[i][0] = preSum[i - 1][0];
            }
        }
        for (int i = 1; i < col; i++) {
            if (forest[0][i] == 2) {
                preSum[0][i] = preSum[0][i - 1] + 1;
            } else {
                preSum[0][i] = preSum[0][i - 1];
            }
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (forest[i][j] == 2) {
                    preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + 1;
                } else {
                    preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1];
                }
            }
        }
        if (preSum[row - 1][col - 1] == 0) return 0;

        int[][][] dp = new int[row][col][number + 1];
        dp[0][0][1] = 1;

        for (int k = 2; k <= number; k++) {
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    if (dp[i][j][k - 1] == 0) continue;

                    for (int y = i + 1; y < row; y++) {
                        if (hasTree(i ,j ,y-1,col-1) && hasTree(y,j,row-1,col-1)) {
                            dp[y][j][k] += dp[i][j][k - 1];
                            dp[y][j][k] %= mod;
                        }
                    }

                    for (int y = j + 1; y < col; y++) {
                        if (hasTree(i,j,row-1,y-1) && hasTree(i,y,row-1,col-1)) {
                            dp[i][y][k] += dp[i][j][k - 1];
                            dp[i][y][k] %= mod;
                        }
                    }
                }
            }
        }

        int res = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0;  j < col; j++) {
                res += dp[i][j][number];
                res %= mod;
            }
        }

        return res;
    }

    public static boolean hasTree(int sr, int sc, int er, int ec) {
        int sum1, sum2, sum3;
        if (sr != 0 && sc != 0) sum1 = preSum[sr - 1][sc - 1];
        else sum1 = 0;
        if (sr != 0) sum2 = preSum[sr - 1][ec];
        else sum2 = 0;
        if (sc != 0) sum3 = preSum[er][sc - 1];
        else sum3 = 0;
        
        return preSum[er][ec] - sum2 - sum3 + sum1 > 0;
    }
}