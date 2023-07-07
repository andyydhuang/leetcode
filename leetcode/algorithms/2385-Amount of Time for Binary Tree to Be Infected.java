/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode start_node;
    int start_val;
    Map<TreeNode, TreeNode> parents;
    
    public int amountOfTime(TreeNode root, int start) {
        parents = new HashMap<>();
        start_val = start;
        start_node = null;

        build_parents(root, null);

        LinkedList<TreeNode> q = new LinkedList<>();
        q.offer(start_node);

        Set<TreeNode> visited = new HashSet<>();
        visited.add(start_node);
        int move = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            
            while (size > 0) {
                TreeNode n = q.poll();
                if (n.left != null && !visited.contains(n.left)) { 
                    q.offer(n.left);
                    visited.add(n.left);
                }
                if (n.right != null && !visited.contains(n.right)) {
                    q.offer(n.right);
                    visited.add(n.right);
                }

                TreeNode p = parents.get(n);
                if (p != null && !visited.contains(p)) { 
                    q.offer(p);
                    visited.add(p);
                }
                size--;
            }
            move++;
        }
        return move-1;
    }

    public void build_parents(TreeNode node, TreeNode parent) {
        if (node != null) {
            if (node.val == start_val) start_node = node; 
            parents.put(node, parent);
            if (node.left != null) build_parents(node.left, node);
            if (node.right != null) build_parents(node.right, node);
        }
    }

}