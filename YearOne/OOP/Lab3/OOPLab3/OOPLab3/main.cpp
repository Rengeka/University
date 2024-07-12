#include <iostream>
#include <fstream>
#include "Line.h"

using namespace std;

ostream& operator << (ostream& os, Line& line)
{

	int i = 0;
	while (line._str[i] != '\0')
	{
		os << line._str[i];
		i++;
	}

	return os;
}

int main() 
{

	/*
	 
	�������� ����� ������ � ������������� ����������� : 
	����� ������, 
	��������� �� ������(������ �������� � ����������� ���������� ������).
	
	������������ ������ : 
	����������� �� �������� ����� ������, 
	����������� �� �������� ������, 
	����������� �� ������� ������� ������ ������, ����������� �����������, 
	������� ������, 
	����� ������.

	�����������(��������������) �������� : 
	+(������������), 
	-(�������� : �������� �������� �������� � ������ ������� ��������), 
	< (������), 
	> (������).

	*/



	const char c1[] {"HELLO"};

	const char c2[] {"ABCDEFGHI"};
	const char* c3 = "Char";

	Line line = *new Line(c2);

	cout << line << endl;



	Line line2 = line + c1;
	Line line3 = line - c1;

	line2.PrintLine();
	line3.PrintLine();

	
	cout << (line2 > c1) << endl;
	cout << (line2 < c1) << endl;
	cout << (Line(c1) > line2) << endl;
	cout << ( line2 > c3) << endl;

	cout << (line3 > line2) << endl;
	cout << (line3 < line2) << endl;


	/*line.ClearLine();
	line2.ClearLine();
	line3.ClearLine();*/

}