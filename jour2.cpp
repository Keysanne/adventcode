#include <cstring>
#include <iostream>
#include <fstream>
#include <string>
using namespace	std;

int check(string str)
{
	size_t i, j;
	int nbr = 0,r = 0 ,g = 0, b = 0;
	string	color[3] = {"red","green","blue"};

	for(i = 0; str[i]; i++)
	{
		nbr = atoi(&str[i]);
		if (nbr == 0)
			continue;
		i += 2;
		j = strlen(str.c_str());
		for(int x = 0; x < 3; x++)
			if (str.find(color[x], i) != string::npos) 
				if (str.find(color[x], i) < j)
					j = str.find(color[x], i);
		if (str[j] == 'r')
			if (nbr > r)
				r = nbr;
		if (str[j] == 'g')
			if (nbr > g)
				g = nbr;
		if (str[j] == 'b')
			if (nbr > b)
				b = nbr;
	}
	return r * g * b;
}

// int game_id(string str)
// {
// 	int rst = atoi(&str[4]);
// 	if (check(&str[str.find(":") + 2]) == 1)
// 		return 0;
// 	return rst;
// }

int	main()
{
	string		str;
	ifstream	recup("ref");
	int			rst = 0;

	while(getline(recup, str))
		rst += check(&str[str.find(":") + 2]);
	cout << rst << endl;
}