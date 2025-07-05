#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isOperator(char ch) {
    return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^';
}
int precedence(char op) {
    if (op == '^')
        return 3; 
    else if (op == '*' || op == '/')
        return 2;
    else if (op == '+' || op == '-')
        return 1;
    else
        return 0;
}
bool isRightAssociative(char op) {
    return op == '^';
}
string infixToPostfix(string infix) {
    stack<char> st;        
    string postfix = "";    
    for (int i = 0; i < infix.length(); i++) {
        char ch = infix[i];
        if (ch == ' ')
            continue;
        if (isalnum(ch)) {
            postfix += ch;
        }
        else if (ch == '(') {
            st.push(ch);
        }
        else if (ch == ')') {
            while (!st.empty() && st.top() != '(') {
                postfix += st.top();
                st.pop();
            }
            if (!st.empty())
                st.pop(); 
        }
        else if (isOperator(ch)) {
            while (!st.empty() && st.top() != '(' &&
                   (precedence(ch) < precedence(st.top()) ||
                   (precedence(ch) == precedence(st.top()) && !isRightAssociative(ch)))) {
                postfix += st.top();
                st.pop();
            }
            st.push(ch); 
        }
    }
    while (!st.empty()) {
        postfix += st.top();
        st.pop();
    }
    return postfix;
}

int main() {
    string infix;
    cout << "Enter an infix expression : ";
    getline(cin, infix);
    string postfix = infixToPostfix(infix);
     cout << "Postfix expression: " << postfix << endl;
    return 0;
}
