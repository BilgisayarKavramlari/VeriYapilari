class Node {
    public int num1;
    public Node nextLink;

    public Node(int num1){
        this.num1 = num1;
    }
}
class LinkList{
    private Node head;

    public LinkList(){
        head = null;
    }

    public void add(int d1) {
        Node link = new Node(d1);
        if(head == null){
            link.nextLink = head;
            head=link;
        }
        else{
            Node current = head;
            Node previus = null;

            while(current!=null){
                previus =current;
                current = current.nextLink;
            }
            current = link;
            previus.nextLink = link;
        }
    }
    public void printList() {
        Node currentLink = head;
        System.out.print("List: ");
        while(currentLink != null) {
            System.out.print("{" + currentLink.num1 + "} ");
            currentLink = currentLink.nextLink;
        }
        System.out.println("");
    }
}
class LinkedList{

    public static void main(String args[]){

        LinkList list = new LinkList();
        int [] array = {2,3,6,3,4,1,9,8,2,6};

        for(int i = 0; i<array.length; i++){
            list.add(array[i]);
        }
        list.printList();
    }
}
