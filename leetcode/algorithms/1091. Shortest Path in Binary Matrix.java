class Solution {
    Queue<int []> q;

    int[] shift = { 1, 0, -1, 0, 1, -1, -1, 1, 1};

    public int shortestPathBinaryMatrix(int[][] grid) {
        q = new LinkedList<>();

        int n = grid.length;

        boolean[][] visited = new boolean[n][n];

        for (int i = 0; i <n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0 && grid[i][j] == 0) {
                    q.offer(new int[] {i, j});
                    visited[i][j] = true;
                    if (n == 1)
                        return 1;
                } else {
                    visited[i][j] = false;
                }
            }
        }        
        int move = 1;
        while(!q.isEmpty()) {
            int size = q.size();

            while (size > 0) {
                int[] p = q.poll();

                for (int i = 0; i < shift.length - 1; i++) {                
                    int new_y = p[0] + shift[i];
                    int new_x = p[1] + shift[i+1];

                    if (new_y >= n || 0 > new_y || new_x >= n || 0 > new_x ||
                        grid[new_y][new_x] == 1 || 
                        visited[new_y][new_x] == true
                        ) {
                        continue;
                    }
                    q.add(new int[] {new_y, new_x});
                    if (new_y == n-1 && new_x == n-1)
                        return move+1;
                    visited[new_y][new_x] = true;
                }
                size--;
            }
            move++;
        }
        return -1;
    }

}