#include <bits/stdc++.h>
using namespace std;
string read_data() {

}
void write_data() {

}
vector<int> removeDupWord(string str)
{
    vector<int> op;
    // Used to split string around spaces.
    istringstream ss(str);
 
    string word; // for storing each word
 
    // Traverse through all words
    // while loop till we get
    // strings to store in string word
    while (ss >> word)
    {
        // print the read word
        op.push_back(stoi(word));
    }
    return op;
}
vector<int> encoding(string file)
{   
    string s1 = "";
    ifstream MyReadFile(file);
    // Use a while loop together with the getline() function to read the file line by line
    char mychar;
    while ( MyReadFile ) {
        mychar = MyReadFile.get();
        s1 += mychar;
    }
    s1 = s1.substr(0, s1.size()-1);
    MyReadFile.close();
    cout << s1; 
	cout << "Encoding\n";
	unordered_map<string, int> table;
	for (int i = 0; i <= 255; i++) {
		string ch = "";
		ch += char(i);
		table[ch] = i;
	}

	string p = "", c = "";
	p += s1[0];
	int code = 256;
	vector<int> output_code;
	cout << "String\tOutput_Code\tAddition\n";
	for (int i = 0; i < s1.length(); i++) {
		if (i != s1.length() - 1)
			c += s1[i + 1];
		if (table.find(p + c) != table.end()) {
			p = p + c;
		}
		else {
			cout << p << "\t" << table[p] << "\t\t"
				<< p + c << "\t" << code << endl;
			output_code.push_back(table[p]);
			table[p + c] = code;
			code++;
			p = c;
		}
		c = "";
	}
	cout << p << "\t" << table[p] << endl;
	output_code.push_back(table[p]);
	return output_code;
}

string decoding(string file)
{
    string s1 = "";
    ifstream MyReadFile(file);
    string myText;
    // Use a while loop together with the getline() function to read the file line by line
    while (getline (MyReadFile, myText)) {
    // Output the text from the file
        s1 += myText;
    }
    MyReadFile.close();
    //cout << s1; 
    vector<int> op = removeDupWord(s1);
	//cout << "\nDecoding\n";
	unordered_map<int, string> table;
	for (int i = 0; i <= 255; i++) {
		string ch = "";
		ch += char(i);
		table[i] = ch;
	}
	int old = op[0], n;
	string s = table[old];
	string c = "";
	c += s[0];
    string kq = s;
	cout << s;
	int count = 256;
	for (int i = 0; i < op.size() - 1; i++) {
		n = op[i + 1];
		if (table.find(n) == table.end()) {
			s = table[old];
			s = s + c;
		}
		else {
			s = table[n];
		}
        kq += s;
		cout << s;
		c = "";
		c += s[0];
		table[count] = table[old] + c;
		count++;
		old = n;
	}
    return kq;
}
int main(int argc, char *argv[])
{
    int i;
	char *argv_2, *argv_3;
	//Xử lý các tham số truyền vào chương trình
	switch (argc)
	{
		// Comparing For
	case 4:
		if (!strcmp(argv[1], "-E") && !strcmp(argv[2], "-i"))
		{
            string output = "";
			argv_2 = argv[3];
            vector<int> output_code = encoding(argv_2);
            cout << "Output Codes are: ";
            for (int i = 0; i < output_code.size(); i++) {
                cout << output_code[i] << " ";
                output += to_string(output_code[i]) + " ";
            }
            ofstream MyWriteFile("temp.txt");

            MyWriteFile << output;
            MyWriteFile.close();
            cout << endl;
            break;
		}
    case 6:
        if (!strcmp(argv[1], "-D"))
        {
            for (i = 2; i < 6; i++)
			{
				if (!strcmp(argv[i], "-i"))
					argv_2 = argv[i + 1];
				if (!strcmp(argv[i], "-o"))
					argv_3 = argv[i + 1];
			}
            ofstream MyWriteFile(argv_3);

            MyWriteFile << decoding(argv_2);;
            MyWriteFile.close();
            break;
        }
    default:
		printf("\t*** !! Error !! ERROR !! Error !!***\n");
		printf("*** EXECUTION ==> ");
		printf("\n\t\t*** ENCODING *** ==> \t./a.out -E -i <input.txt>\n");
		printf("\t\t*** DECODING *** ==> \t./a.out -D -i <input.txt> -o <output.txt>\n");
		//printf("\t\tFOR MORE DETAILS ===> **README**\n");
	}
    return 0;
}
