// Программа вычисления функции x = f(a)
Console.Write("Введите число а: ");
string str_a = Console.ReadLine();
int a = int.Parse(str_a);

int x = a * 3;
Console.WriteLine($"Функция x = f(a) равна => {x}");