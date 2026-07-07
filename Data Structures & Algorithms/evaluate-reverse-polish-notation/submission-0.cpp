class Solution {
public:
    int evalRPN(vector<string>& tokens) 
    {
        stack<int> st;
        for(string& s : tokens)
        {
            if(s == "+")
            {
                int temp1 = st.top();
                st.pop();
                int temp2 = st.top();
                st.pop();
                st.push(temp1+temp2);
            }
            else if (s == "*")
            {
                int temp1 = st.top();
                st.pop();
                int temp2 = st.top();
                st.pop();
                st.push(temp1*temp2);
            }
            else if (s == "-")
            {
                int temp1 = st.top();
                st.pop();
                int temp2 = st.top();
                st.pop();
                st.push(temp2 - temp1);
            }
            else if (s == "/")
            {
                int temp1 = st.top();
                st.pop();
                int temp2 = st.top();
                st.pop();
                st.push(temp2 / temp1);
            }
            else
            {
                st.push(stoi(s));
            }
        }
        return st.top();
        
    }
};
