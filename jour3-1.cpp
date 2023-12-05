#include <cstring>
#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <vector>
using namespace	std;

int space(int x)
{
	if (x < 10)
		return 1;
	if (x < 100)
		return 2;
	else
		return 3;
}

int recursive(vector<string> map, size_t i, size_t j)
{
	int symbol = 0;

	if (j < strlen(map[i].c_str()) - 1)
	{
		if (map[i][j + 1] != '.' && !(map[i][j + 1] >= '0' && map[i][j + 1] <= '9'))
				symbol++;
		if (i > 0)
			if (map[i - 1][j + 1] != '.' && !(map[i - 1][j + 1] >= '0' && map[i - 1][j + 1] <= '9'))
				symbol++;
		if (i < map.size() - 1)
			if (map[i + 1][j + 1] != '.' && !(map[i + 1][j + 1] >= '0' && map[i + 1][j + 1] <= '9'))
				symbol++;
	}
	if (j > 0)
	{
		if (map[i][j - 1] != '.' && !(map[i][j - 1] >= '0' && map[i][j - 1] <= '9'))
			symbol++;
		if (i > 0)
			if (map[i - 1][j - 1] != '.' && !(map[i - 1][j - 1] >= '0' && map[i - 1][j - 1] <= '9'))
				symbol++;
		if (i < map.size() - 1)
			if (map[i + 1][j - 1] != '.' && !(map[i + 1][j - 1] >= '0' && map[i + 1][j - 1] <= '9'))
				symbol++;
	}
	if (i > 0)
		if (map[i - 1][j] != '.' && !(map[i - 1][j] >= '0' && map[i - 1][j] <= '9'))
			symbol++;
	if (i < map.size() - 1)
		if (map[i + 1][j] != '.' && !(map[i + 1][j] >= '0' && map[i + 1][j] <= '9'))
			symbol++;
	if (symbol > 0)
		return 1;
	if (map[i][j + 1] >= '0' && map[i][j + 1] <= '9')
		return recursive(map, i, j + 1);
	else
	 	return 0;
}

int parser(vector<string> map, size_t i)
{
	stack<int>	nbr;
	int			rst;
	size_t		j;

	for(j = 0; map[i][j]; j++)
	{
		if (map[i][j] >= '0' && map[i][j] <= '9')
		{
			if (recursive(map, i, j) == 1)
			{
				rst = atoi(&map[i][j]);
				j += space(rst);
				nbr.push(rst);
			}
		}
	}
	rst = 0;	
	while(!nbr.empty())
	{
		rst+= nbr.top();
		nbr.pop();
	}
	return rst;
}

int	main()
{
	string		str;
	ifstream	recup("ref");
	vector<string>	map;
	int			rst = 0;

	while(getline(recup, str))
		map.push_back(str);
	for (size_t i = 0; i < map.size(); i++)
		rst += parser(map, i);
	cout << rst << endl;
}