#https://leetcode.com/problems/copy-list-with-random-pointer/

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    Map<Node, Node> nodeMap = new HashMap<Node, Node>();

    public Node copyRandomList(Node head) {
        if(head==null)
            return null;
        Node currentNode = head;
        Node hcopy = new Node(currentNode.val);
        nodeMap.put(head, hcopy);
        Node currentTargetNode = hcopy;
        while(currentNode.next!=null){
            if(nodeMap.containsKey(currentNode.next))
                currentTargetNode.next=nodeMap.get(currentNode.next);
            else{
                currentTargetNode.next = new Node(currentNode.next.val);
                nodeMap.put(currentNode.next, currentTargetNode.next);
            }
            if(currentNode.random!=null){
                if(nodeMap.containsKey(currentNode.random)){
                    currentTargetNode.random=nodeMap.get(currentNode.random);
                }
                else{
                    currentTargetNode.random = new Node(currentNode.random.val);
                    nodeMap.put(currentNode.random, currentTargetNode.random);
                }
            }             
            currentNode = currentNode.next;
            currentTargetNode = currentTargetNode.next;
        }
        if(currentNode.random!=null){
            if(nodeMap.containsKey(currentNode.random)){
                currentTargetNode.random=nodeMap.get(currentNode.random);
            }
            else{
                currentTargetNode.random = new Node(currentNode.random.val);
                nodeMap.put(currentNode.random, currentTargetNode.random);
           }
        } 
        return hcopy;
    }
}
