class Solution {
    boolean[] visited;
    LinkedList<String> q;

    public int minMutation(String startGene, String endGene, String[] bank) {            
        int n = bank.length;        
        visited = new boolean[n]; 
        q = new LinkedList<>();

        for(int i = 0; i < bank.length; i++) {
            if (isOneMutation(startGene, bank[i]) == true) {
                visited[i] = true;
                q.offer(bank[i]);

                if (bank[i].equals(endGene))
                    return 1;
            }
        }
        //q.forEach(s -> System.out.print(" " + s));
        int move = 2;

        while(!q.isEmpty()) {
            int size = q.size();
            while (size > 0) {
                String gene = q.poll();
                for(int i = 0; i < bank.length; i++) {
                    if (visited[i] == false && isOneMutation(gene, bank[i]) == true) {
                        visited[i] = true;
                        q.offer(bank[i]);
                        if (bank[i].equals(endGene))
                            return move;
                    }
                }
                size -= 1;
            }
            move += 1;
        }
        return -1;
    }

    public boolean isOneMutation(String word1, String word2) {
        int diff = 0;
        for(int i = 0; i < word1.length(); i++) {
            if(word1.charAt(i) != word2.charAt(i)) {
                diff++;
                if (diff > 1)
                    break;
            }     
        }
        return (diff == 1);
    }
}