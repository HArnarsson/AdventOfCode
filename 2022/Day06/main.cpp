// Idea: Use queue to take in the list of inputs, then use a bit mask to see if there are any duplicates
// Don't really ahve to use a bitmask, could use a vector instead

#include <vector>
#include <queue>
#include <iostream>
#include <fstream>

using namespace std;

bool is_marker(queue<char>& toTest){
    queue<char> q = toTest;
    const int ALPHABET_SIZE(26);
    const int ASCII_SHIFT(97);
    const int SIZE = q.size();
    vector<bool> bitmask(ALPHABET_SIZE, false);
    for(int i = 0; i < SIZE; i++){
        if(bitmask.at((int)q.front()-ASCII_SHIFT) == true){
            return false;
        } else{
            bitmask.at((int)q.front()-ASCII_SHIFT) = true;
            q.pop();
        }
    }
    return true;
}
int main(){   
    const int MARKER_LENGTH = 4; 
    fstream fileIn("input.txt");

    char curr = ' ';
    queue<char> q;
    for(int i = 0; i < MARKER_LENGTH; i++){
        fileIn >> curr;
        q.push(curr);
    }
    
    int c = MARKER_LENGTH;
    while(true){
        if(is_marker(q)){
            break;
        } else{
            q.pop();
            fileIn >> curr;
            q.push(curr);
            c++;
        }
    }
    cout << c << endl;
    fileIn.close();
    
    const int MESSAGE_MARKER_LENGTH = 14;

    fstream fileIn2("input.txt");

    char curr2 = ' ';
    queue<char> q2;
    for(int i = 0; i < MESSAGE_MARKER_LENGTH; i++){
        fileIn2 >> curr2;
        q2.push(curr2);
    }
    
    int c2 = MESSAGE_MARKER_LENGTH;
    while(true){
        if(is_marker(q2)){
            break;
        } else{
            q2.pop();
            fileIn2 >> curr2;
            q2.push(curr2);
            c2++;
        }
    }
    cout << c2 << endl;
    fileIn.close();
    return 0;
}