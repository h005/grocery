// this file was created for encoded the plain text file
// Caesar code

// compile g++ en_deCoding.cpp -o en_deCoding
// run ./en_deCoding -e fileIn fileOut key
//					 -d fileIn fileOut key

#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;

char enCode(char c, char key)
{
    int val1 = (int)c + 128;
    int val2 = (int)key + 128;
    int val = (val1 + val2) % 256;
    return char(val - 128);	
}

void encode(char* key, char* fileIn, char* fileOut)
{
	ifstream infile(fileIn, std::ifstream::in);
	ofstream outfile(fileOut, std::ofstream::out);
	string ss;
	int keyLen = strlen(key);
	while(getline(infile,ss))
	{
		for(int i=0;i<ss.size();i++)
		{
			char c = enCode(ss[i],key[i%keyLen]);
			ss.replace(i,1,1,c);
		}
		outfile << ss << endl;
	}
	cout << "encoding done" << endl;
}

char deCode(char c, char key)
{
    int val1 = (int)c + 128;
    int val2 = (int)key + 128;
    int val = (val1 + 256 - val2) % 256;
    return char(val - 128);	
}

void decode(char* key, char* fileIn, char* fileOut)
{
	ifstream infile(fileIn, std::ifstream::in);
	ofstream outfile(fileOut, std::ofstream::out);
	string ss;
	int keyLen = strlen(key);
	while(getline(infile,ss))
	{
		for(int i=0;i<ss.size();i++)
		{
			char c = deCode(ss[i],key[i%keyLen]);
			ss.replace(i,1,1,c);
		}
		outfile << ss << endl;
	}
	cout << "decoding done" << endl;
}

int main(int argc, char** args)
{
	if(argc != 5)
	{
		cout << "Usage is -e / -d fileIn fileOut key" << endl;;
	}
	else
	{
		char* fileIn = args[2];
		char* fileOut = args[3];
		char* key = args[4];
		if(!strcmp(args[1],"-e"))
		{
			encode(key,fileIn,fileOut);
		}
		else if(!strcmp(args[1],"-d"))
		{
			decode(key,fileIn,fileOut);
		}
		else
		{
			cout << "parameter error" << endl;
		}


	}
}
