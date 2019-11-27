#include <iostream>
#include <string>
#include <sstream>
#include "curl/curl.h"

using namespace std;

static string buffer;

static size_t writer(char *data, size_t size, size_t nmemb, string *buffer)
{
	size_t realsize = size * nmemb;
	buffer->append(data, realsize);
	return realsize;
}

int main()
{
	string url("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=");
	string nothing("12345");

	int i;
	std::stringstream ss;

	CURL *curl;
	CURLcode result = CURLE_OK;

	if ((curl = curl_easy_init()) == NULL) {
		cout << "curl init failed";
	}

	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writer);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, &buffer);

	while (result == CURLE_OK) {
		curl_easy_setopt(curl, CURLOPT_URL, (url + nothing).c_str());
		result = curl_easy_perform(curl);

		if (result == CURLE_OK) {
			if (buffer.find("and the next nothing is") != string::npos)
				nothing.assign(buffer.substr(buffer.find_last_of(" ") + 1));
			else if (buffer.find("Yes. Divide by two") != string::npos) {
				ss.clear();
				ss << nothing;
				ss >> i;
				ss.clear();
				ss << i / 2;
				ss >> nothing;
			} else {
				cout << buffer;
				curl_easy_cleanup(curl);
				exit(0);
			}
			buffer.clear();
		} else {
			cout << "Error: " << result;
			exit(-1);
		}
	}
}
