import java.util.Stack;

public class st {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(10);

        stack.push(20);
        stack.pop();
        stack.pop();

        System.out.println(stack);
    }
}
