#include <stack>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

void insert_at_bottom(stack<char>& st, char x){
    if(st.size() == 0){
        st.push(x);
    } else{
        char a = st.top();
        st.pop();
        insert_at_bottom(st, x);

        st.push(a);
    }
}

void reverse(stack<char>& st){

    if(st.size() > 0){
        char x = st.top();
        st.pop();
        reverse(st);

        insert_at_bottom(st, x);
    }
    return;
}

vector<stack<char>> parse_crates(string filename){
    ifstream fileIn(filename);
    string temp;
    string val;
    while(!fileIn.eof()){
        fileIn >> temp;
        if(temp != " "){
            val = temp;
        }
    }
    fileIn.close();

    fileIn.open(filename);
    int numRows = 0;
    string c;
    while(!fileIn.eof()){
        c = fileIn.get();
        if(c == "\n"){
            numRows++;
        }
    }

    fileIn.close();
    string::size_type sz;
    int size = stoi(val,&sz);
    vector<stack<char>> crates;
    for(int i = 0; i < size; i++){
        stack<char> temp1;
        crates.push_back(temp1);
    }


    fileIn.open(filename);
    char crateName = ' ';
    int counter = 0;
    for(int i = 0; i < numRows; i++){
        counter = 0;
        while(crateName != '\n'){
            crateName = fileIn.get();
            if(crateName == ' ' || crateName == '[' || crateName == ']' || crateName == '\n'){
                counter++;
                continue;
            }
            crates.at(counter/4).push(crateName);
            counter++;
            }
        crateName = fileIn.get();
    }
    fileIn.close();
    return crates;

}

void move(vector<stack<char>>& crates, int num, int from, int to){
    from--;
    to--;
    for(int i = 0; i < num; i++){
        char crate = crates.at(from).top();
        crates.at(from).pop();
        crates.at(to).push(crate);
    }
}

void move2(vector<stack<char>>& crates, int num, int from, int to){
    from--;
    to--;
    stack<char> temp;
    for(int i = 0; i < num; i++){
        temp.push(crates.at(from).top());
        crates.at(from).pop();
    }
    for(int i = 0; i < num; i++){
        crates.at(to).push(temp.top());
        temp.pop();
    }
}

vector<vector<int>> parse_instructions(string filename){
    vector<vector<int>> instructions; 
    ifstream fileIn(filename);
    const regex re("\\d+");
    smatch sm;
    string line = " ";
    while(!fileIn.eof()){
        getline(fileIn, line, '\n');
        vector<int> instruction;
        while (regex_search(line, sm, re)) {
            string::size_type sz;
            instruction.push_back(stoi(sm.str(0), &sz));

        // suffix to find the rest of the string.
        line = sm.suffix().str();
        }
        instructions.push_back(instruction);
    }

    return instructions;
}

int main(){

    vector<stack<char>> crates = parse_crates("crates.txt");
    for(unsigned int i = 0; i < crates.size(); i++){
        reverse(crates.at(i));
    }

    vector<vector<int>> instructions = parse_instructions("instructions.txt");

    for(unsigned int i = 0; i < instructions.size(); i++){
        move(crates, instructions.at(i).at(0), instructions.at(i).at(1), instructions.at(i).at(2));
    }

    cout << "Part 1 answer: ";
    for(unsigned int i = 0; i < crates.size(); i++){
        cout << crates.at(i).top();
    }

    vector<stack<char>> crates2 = parse_crates("crates.txt");
    for(unsigned int i = 0; i < crates2.size(); i++){
        reverse(crates2.at(i));
    }

    for(unsigned int i = 0; i < instructions.size(); i++){
        move2(crates2, instructions.at(i).at(0), instructions.at(i).at(1), instructions.at(i).at(2));
    }
    
    cout << endl;
    cout << "Part 2 answer: ";
    for(unsigned int i = 0; i < crates.size(); i++){
        cout << crates2.at(i).top();
    }
    return 0;
}