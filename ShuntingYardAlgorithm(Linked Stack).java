import java.io.*;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * LinkedStack based on LinkedList class
 *
 * For solving this problem i need 5 methods:
 * 1. isEmpty() - checks empty stack or not
 * 2. peek()    - return last element
 * 3. push()    - add element at the end of stack
 * 4. pop()     - return last element and delete it from stack
 * 5. size()    - return size of stack
 * @param <E>
 */
class LinkedStack<E> {
    LinkedList<E> list = new LinkedList<>();

    /** Returns is empty stack or not */
    public boolean isEmpty() {
        if (list.size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    /** Returns last element of stack */
    public E peek() {
        return list.getLast();
    }

    /** Adds element to the and of stack */
    public void push(E element) {
        list.addLast(element);
    }

    /** Returns last element of stack and deletes it from stack */
    public E pop() {
        E temp = list.getLast();
        list.removeLast();
        return temp;
    }

    /** Returns size of stack */
    public int size() {
        return list.size();
    }
}

/**
 * This class solve problem
 */
public class Solve {
    /** LinkedStack result where we will have Reverse Polish notation */
    static LinkedStack<String> result = new LinkedStack<String>();

    /** LinkedStack operators where we will store our operators */
    static LinkedStack<String> operators = new LinkedStack<String>();

    /**
     * isOperator() checks is it operator or not
     *
     * If it isn't operator it returns 0
     * If it is operator it returns values depend on precedence of each operator
     * @param str
     * @return
     */
    public static int isOperator(String str) {
        switch (str) {
            case "+": return 1; // Precedence of "+"
            case "-": return 1; // Precedence of "-"
            case "/": return 2; // Precedence of "/"
            case "*": return 2; // Precedence of "*"

            case "(": return -1;  // We call open bracer -1
            case ")": return -2;  // We call close bracer -2
            default : return 0;  // It means that current str is not a operator
        }
    }

    /**
     * For making our life easier we refactor input to
     * make between all operators and numbers spaces
     * @throws IOException
     */
    public static void RefactorOutputTxt() throws IOException {
        /** Take very convenient for us representation of input */
        String string = parser();

        BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));

        bw.write(string);
        bw.close();
    }

    /**
     * Parse data and add spaces
     * @return
     * @throws FileNotFoundException
     */
    public static String parser() throws FileNotFoundException {
        Scanner sc = new Scanner(new FileReader("input.txt"));
        String string = sc.nextLine();

        for (int i = 0; i < string.length(); i++) {

            /** If current char  doesn't exist number or '.'
             * add spaces for convenient reading
             */
            if (isOperator(string.substring(i,i+1)) != 0) {
                if (i == 0) {
                    string = string.substring(0, 1) + " " + string.substring(1, string.length());
                    i++;
                } else {
                    string = string.substring(0, i) + " " + string.substring(i, i + 1) + " " + string.substring(i + 1, string.length());
                    i += 2;
                }
            }
        }

        /** Return represent of input */
        return string;
    }

    /**
     * Represent data from input to Reverse Polish notation
     * @throws IOException
     */
    public static void ShuntingYardAlgorithm() throws IOException {
        Scanner sc = new Scanner(new FileReader("output.txt"));

        while (sc.hasNext()) {
            String temp = sc.next();

            int res = isOperator(temp);

            // If current string doesn't number
            if (res != 0) {
                // If we have no any elements in operators just push current string
                if (operators.isEmpty()) {
                    operators.push(temp);
                }

                // If current string is open bracket push() it into operator stack
                else if (res  == -1) {
                    operators.push(temp);
                }

                // If current string is close bracket pop() all elements and add them
                // to result stack while current element of operator stack isn't
                // equal "("
                // After it pop() last element ( "(" )
                else if (res == -2) {

                    int i = 0, size = operators.size();
                    for (; i < size; i++) {
                        if (isOperator(operators.peek()) == -1) {
                            operators.pop();
                            break;
                        } else {
                            result.push(operators.pop());
                        }
                    }

                    // If operator stack have no any element it means
                    // input file has error
                    if (i == size) {
                        BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
                        bw.write("ERROR");
                        bw.close();

                        // We have non-correct data and we end our program
                        System.exit(0);
                    }
                }

                // If precedence of operator's last element less than current string
                // push() current string to operators stack
                else if (res > isOperator(operators.peek())) {
                    operators.push(temp);
                }

                // If precedence of operator's last element equal precedence of
                // current string pop() element from operators stack and
                // push it into result stack
                // After push() current string into operators stack
                else if (res <= isOperator(operators.peek())) {
                    result.push(operators.pop());
                    operators.push(temp);
                }
            }

            // If string contains number push() it into result stack
            else {
                result.push(temp);
            }
        }

        // After all check just push() all elements from operators stack
        // to result stack
        while (!operators.isEmpty()) {
            result.push(operators.pop());
        }

    }


    public static int whichOperator(String str) {
        switch (str) {
            case "+": return 1; // Precedence of "+"
            case "-": return 2; // Precedence of "-"
            case "/": return 3; // Precedence of "/"
            case "*": return 4; // Precedence of "*"
            }
        return 0;
    }


    public static void CalculatingRevPolNot() throws IOException {
        LinkedStack<String> reversedResulStack = new LinkedStack<>();
        LinkedStack<String> tempStack = new LinkedStack<>();

        while (!result.isEmpty()) {
            reversedResulStack.push(result.pop());
        }

        while (!reversedResulStack.isEmpty()) {
            if (reversedResulStack.size() == 1 && isOperator(reversedResulStack.peek()) == 0) {
                break;
            } else if (isOperator(reversedResulStack.peek()) == 0) {
                tempStack.push(reversedResulStack.pop());
            } else if (whichOperator(reversedResulStack.peek()) == 1) {
                reversedResulStack.pop();
                double tempDouble1 = Double.valueOf(tempStack.pop()),
                        tempDouble2 = Double.valueOf(tempStack.pop());
                reversedResulStack.push(String.valueOf(tempDouble1 + tempDouble2));
            } else if (whichOperator(reversedResulStack.peek()) == 2) {
                reversedResulStack.pop();
                double tempDouble2 = Double.valueOf(tempStack.pop()),
                        tempDouble1 = Double.valueOf(tempStack.pop());
                reversedResulStack.push(String.valueOf(tempDouble1 - tempDouble2));
            } else if (whichOperator(reversedResulStack.peek()) == 3) {
                reversedResulStack.pop();
                double tempDouble2 = Double.valueOf(tempStack.pop()),
                        tempDouble1 = Double.valueOf(tempStack.pop());
                reversedResulStack.push(String.valueOf(tempDouble1 / tempDouble2));
            } else if (whichOperator(reversedResulStack.peek()) == 4) {
                reversedResulStack.pop();
                double tempDouble1 = Double.valueOf(tempStack.pop()),
                        tempDouble2 = Double.valueOf(tempStack.pop());
                reversedResulStack.push(String.valueOf(tempDouble1 * tempDouble2));
            }
        }

        BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
        bw.write(String.format("%.2f", Double.valueOf(reversedResulStack.pop())));
        bw.close();
    }


    /**
     * First, refactor input.txt file for convenient reading
     * Second, represent data from input.txt to Reverse Polish notation
     * Third, calculate value by using Reverse Polish notation
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        RefactorOutputTxt();
        ShuntingYardAlgorithm();
        CalculatingRevPolNot();
    }
}
