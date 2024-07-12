#include <iostream>           // ����������� ���������
#include <iomanip>            // ����������� ������� ��� ������ � �������� ������
#define _USE_MATH_DEFINES     // ���������� ����������� �������������� ���������
#define M_PI_3
#include <math.h>             // ����������� �������������� �������
//#include <conio.h>			  // ����������� ������� ��� ������ � �������� ������

void PrintHead()              // ������� ������ ��������� ���������� � ����� �������
{
	std::cout << std::endl;
	std::cout << "  [-PI/2; PI/2]" << std::endl << std::endl 
		<< "  Step +PI/10" << std::endl << std::endl;
	
	std::cout << "  ===============================" << std::endl;
	printf(" ||     x     ||        y       ||\n");
	std::cout << "  ===============================" << std::endl;
}

double MathFunc(double* x)    // �������������� �������
{
	if (*x <= M_PI / 3)      
	{						  // ���������� �� -������������� �� PI/3
		return exp(cos(*x));

	}
	else if (*x > M_PI / 3)   // ���������� �� PI/3 �� �������������
	{
		return cos(exp(*x));

	}
	else
	{
		return NULL;
	}
}

void PrintResult(double* x, double y)  // ������� ������ ���������� � �������
{
	std::cout << std::setiosflags(std::ios::left);
	std::cout << " || ";
	std::cout.width(10);
	std::cout << *x << "||" << "    " << std::setw(9) << y;
	printf("\t||\n");
}

int main()
{
	double* x = (double*)malloc(sizeof(double));   // ���������� ����������
	*x = -M_PI / 2;
	PrintHead();

	while (*x >= (-M_PI / 2) and *x <= (M_PI / 2)) // ���� � ����� � PI/10
	{
		PrintResult(x, MathFunc(x));
		*x += M_PI / 10;
	}

	std::cout << "  ===============================" << std::endl; // ���������� �������

	return 0;
}


