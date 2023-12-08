#include <iostream>
#include <fstream>

using namespace std;

void addScore(const char THROW, int& score){
    if(THROW == 'A'){ // Rock
        score += 1;
    } else if(THROW == 'B'){ // Paper
        score += 2;
    } else if(THROW == 'C'){
        score += 3;
    } else{
        cerr << "SNO error" << endl;
    }
}

void play_rps(char oppThrow, char youThrow, int& oppScore, int& youScore){
    youThrow = (char)((int)(youThrow) - 23);
    addScore(oppThrow, oppScore);
    addScore(youThrow, youScore);
    if(oppThrow == youThrow){
        oppScore += 3;
        youScore += 3;
    } else if(((int)oppThrow- (int)youThrow + 3) % 3 == 1){
        oppScore += 6;
    } else if(((int)oppThrow - (int)youThrow + 3) % 3 == 2){
        youScore += 6;
    } else {
    }
}

int win(char oppThrow){
    if(oppThrow == 'A'){
        return 2 + 6;
    } else if(oppThrow == 'B'){
        return 3 + 6;
    } else if(oppThrow == 'C'){
        return 1 + 6;
    } else{
        cout << "SNO error" << endl;
        return 0;
    }
}

int draw(char oppThrow){
    return (int)oppThrow - 64 + 3;
}

int lose(char oppThrow){
    if(oppThrow == 'A'){
        return 3;
    } else if(oppThrow == 'B'){
        return 1;
    } else if(oppThrow == 'C'){
        return 2;
    } else{
        cout << "SNO error" << endl;
        return 0;
    }
}

void play_rps_2(char oppThrow, char youThrow, int& youScore){
    if(youThrow == 'X'){
        youScore += lose(oppThrow);
    } else if(youThrow == 'Y'){
        youScore += draw(oppThrow);
    } else if(youThrow == 'Z'){
        youScore += win(oppThrow);
    } 
}

int main(){
    int youScore = 0;
    int oppScore = 0;
    char youThrow = ' ';
    char oppThrow = ' ';
    ifstream fileIn("input.txt");
    while(true){
        fileIn >> oppThrow;
        fileIn >> youThrow;
        if(fileIn.eof()){
            break;
        }
        play_rps(oppThrow, youThrow, oppScore, youScore);
    }
    cout << "Part 1 answer: ";
    cout << youScore << endl;
    youScore = 0;
    ifstream fileIn2("input.txt");
    while(true){
        fileIn2 >> oppThrow;
        fileIn2 >> youThrow;
        if(fileIn2.eof()){
            break;
        }
        play_rps_2(oppThrow, youThrow, youScore);
    }
    cout << "Part 2 answer: ";
    cout << youScore << endl;

    return 0;
}