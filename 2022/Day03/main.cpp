#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <unordered_set>

using namespace std;

vector<char> intersection(string& halfOne, string& halfTwo){
    unordered_set<char> set(halfOne.cbegin(), halfOne.cend());
    vector<char> intersection;
    for(unsigned int i = 0; i < halfTwo.size(); i++){
        if(set.erase(halfTwo.at(i)) > 0){
            intersection.push_back(halfTwo.at(i));
        }
    }
    return intersection;
}

string intersection2(string& halfOne, string& halfTwo){
    unordered_set<char> set(halfOne.cbegin(), halfOne.cend());
    vector<char> intersection;
    for(unsigned int i = 0; i < halfTwo.size(); i++){
        if(set.erase(halfTwo.at(i)) > 0){
            intersection.push_back(halfTwo.at(i));
        }
    }
    string result = "";
    for(unsigned int i = 0; i < intersection.size(); i++){
        result += intersection.at(i);
    }
    return result;
}

int get_score(char in){
    if(islower(in)){
        return (int)(in) - 96;
    } else{
        return (int)(in) - 38;
    }
}
int main(){
    string temp = " ";
    vector<string> rucksacks;
    string halfOne = " ";
    string halfTwo = " ";
    ifstream fileIn("input.txt");
    string halfThree = " ";
    char output = ' ';
    int halfSize = 0;
    int sum = 0;
    int sum2 = 0;
    while(true){
        fileIn >> temp;
        rucksacks.push_back(temp);
        if(fileIn.eof()){
            break;
        }
    }
    for(unsigned int i = 0; i < rucksacks.size(); i++){
        // All rucksacks are even size
        halfSize = rucksacks.at(i).size()/2;
        halfOne = rucksacks.at(i).substr(0,halfSize);
        halfTwo = rucksacks.at(i).substr(halfSize);
        output = intersection(halfOne, halfTwo).at(0);
        sum += get_score(output);
    }
    cout << "Part 1 answer: ";
    cout << sum << endl;
    for(unsigned int i = 0; i < rucksacks.size(); i+=3){
        halfOne = rucksacks.at(i);
        halfTwo = rucksacks.at(i+1);
        halfThree = rucksacks.at(i+2);
        temp = intersection2(halfOne, halfTwo);
        output = intersection(temp, halfThree).at(0);
        sum2 += get_score(output);
    }
    cout << "Part 2 answer: ";
    cout << sum2 << endl;
    return 0;
}