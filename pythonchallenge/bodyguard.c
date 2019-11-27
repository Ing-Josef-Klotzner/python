#include <boost/regex.hpp>
#include <iostream>
#include <fstream>

using namespace std;
using namespace boost;

int main()
{
	regex rgx("(?<=[A-Z]{3})(?<![A-Z].{3})([a-z])(?=[A-Z]{3})(?!.{3}[A-Z])");
	string s;
	ifstream is("bodyguard.txt");
	smatch result;

	while (getline(is, s))
		if(regex_search(s, result, rgx))
			cout << result[1];
}
