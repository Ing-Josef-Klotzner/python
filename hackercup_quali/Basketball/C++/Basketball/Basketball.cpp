#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <list>
#include <vector>

using namespace std;

int main()
{
    int i;
    string line_list[1000000];
    char line[256]; // maximum 256 characters per line!
    FILE * iFile;
    FILE * oFile;
    oFile = fopen("out.txt","w");
    iFile = fopen("basketball_game_example_input.txt","r");
    while(fgets(line, 256, iFile))  //input from the file in.txt
    {
        //fputs(line,oFile);

        list<char> l(line, line + strlen(line));

        line_list[i]=line;   // line from input file to string array line_list

//        cout << line;
        i++;
    }
    for (int j=0;j<i-1;j++)   // Ausgabe array
    {
        cout<<" "<<line_list[j];
    }
    fclose (oFile);
    fclose (iFile);
    cout << "Basketball Game Calculator - JosefK - 20131207" << "\n";
    cout << "Result was written to file 'out.txt'." << "\n";
    return 0;
}
