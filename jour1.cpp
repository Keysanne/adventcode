#include <cstring>
#include <iostream>
#include <fstream>
#include <string>
using namespace	std;

int first_number(string str)
{
	size_t rst = 1000;
	int final = -1;
	string	number[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	
	int i;
	for(i = 0; i < 9; i++)
	{
		if (str.find(number[i]) != string::npos)
		{
			if (str.find(number[i]) < rst)
			{
				rst = str.find(number[i]);
				final = i;
			}
		}
	}
	for (size_t j = 0; j < rst; j++)
		if (str[j] >= '0' && str[j] <= '9')
			return (str[j] - 48);
	if (final == -1)
		return 0;
	return final + 1;
}

int last_number(string str)
{
	size_t rst = 0;
	int final = -1;
	string	number[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	
	int i;
	for(i = 0; i < 9; i++)
	{
		if (str.rfind(number[i]) != string::npos)
		{
			if (str.rfind(number[i]) > rst)
			{
				rst = str.rfind(number[i]);
				final = i;
			}
		}
	}
	for (size_t j = strlen(str.c_str()); j >= rst; j--)
		if (str[j] >= '0' && str[j] <= '9')
			return (str[j] - 48);
	if (final == -1)
		return 0;
	return final + 1;
}

int	main()
{
	string		str;
	ifstream	recup("ref");
	int			rst = 0, i = 0, j = 0;

	while(getline(recup, str))
	{
		i = first_number(str);
		j = last_number(str);
		rst += i * 10 + j;
	}
	cout << rst << endl;
}