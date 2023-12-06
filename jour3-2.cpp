#include <cstring>
#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <vector>
using namespace	std;

int	multiple(vector<string> map, size_t i, size_t j, int up, int down, int mid)
{
	int rst = 1;
	if (up > 0)
	{
		i--;
		for (int x = 0;x < up;)
		{
			if (j > 0)
			{
				int y = j - 1;
				while (map[i][y] >= '0' && map[i][y] <= '9' && y > 0)
					y--;
				if (map[i][y] == '.')
					y++;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == up)
						break;
				}
			}
			if (atoi(&map[i][j]) > 0)
			{
				rst *=  atoi(&map[i][j]);
				x++;
				if (x == up)
					break;
			}
			if (j < strlen(map[i].c_str()))
			{
				int y = j + 1;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == up)
						break;
				}
			}
		}
		i++;
	}
	if (mid > 0)
	{
		for (int x = 0;x < mid;)
		{
			if (j > 0)
			{
				int y = j - 1;
				while (map[i][y] >= '0' && map[i][y] <= '9' && y > 0)
					y--;
				if (map[i][y] == '.')
					y++;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == mid)
						break;
				}
			}
			if (j < strlen(map[i].c_str()))
			{
				int y = j + 1;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == mid)
						break;
				}
			}
		}
	}
	if (down > 0)
	{
		i++;
		for (int x = 0;x < down;)
		{
			if (j > 0)
			{
				int y = j - 1;
				while (map[i][y] >= '0' && map[i][y] <= '9' && y > 0)
					y--;
				if (map[i][y] == '.')
					y++;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == down)
						break;
				}
			}
			if (atoi(&map[i][j]) > 0)
			{
				rst *=  atoi(&map[i][j]);
				x++;
				if (x == down)
					break;
			}
			if (j < strlen(map[i].c_str()))
			{
				int y = j + 1;
				if (atoi(&map[i][y]) > 0)
				{
					rst *=  atoi(&map[i][y]);
					x++;
					if (x == down)
						break;
				}
			}
		}
		i--;
	}
	return rst;
}

int	line(vector<string> map, size_t i, size_t j)
{
	int number = 0;
	if (j > 0)
		if (map[i][j - 1] >= '0' && map[i][j -1] <= '9')
			number++;
	if (j < strlen(map[i].c_str()))
		if (map[i][j + 1] >= '0' && map[i][j + 1] <= '9')
			number++;
	if (number == 0 && map[i][j] >= '0' && map[i][j] <= '9')	
		number++;
	if (number == 2 && map[i][j] >= '0' && map[i][j] <= '9')
		number--;
	return number;
}

int	gears(vector<string> map, size_t i, size_t j)
{
	int up = 0, down = 0, mid = 0, rst = 0;
	
	if (i > 0)
		up += line(map, i - 1, j);
	if (i < map.size())
		down += line(map, i + 1, j);
	mid += line(map, i, j);
	if (up + mid + down != 2)
		return 0;
	rst = multiple(map, i, j, up, down, mid);
	return rst;
}

int parser(vector<string> map)
{
	int			rst = 0;
	size_t		j, i;

	for(i = 0; i < map.size(); i++)
		for(j = 0; map[i][j]; j++)
			if (map[i][j] == '*')
				rst += gears(map, i , j);
	return rst;
}

int	main()
{
	string		str;
	ifstream	recup("ref");
	vector<string>	map;
	int			rst;

	while(getline(recup, str))
		map.push_back(str);
	cout << parser(map) << endl;
}