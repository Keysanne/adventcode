#include <cstring>
#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <vector>
using namespace	std;

int	gears(vector<string> map, size_t i, size_t j)
{
	cout << map[i][j] << endl;
	return 0;
}

int parser(vector<string> map)
{
	int			rst = 0;
	size_t		j, i;

	for(i = 0; i < map.size(); i++)
		for(j = 0; map[i][j]; j++)
			if (map[i][j] != '.' && !(map[i][j] >= '0' && map[i][j] <= '9'))
				gears(map, i , j);
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
	rst += parser(map);
	cout << rst << endl;
}