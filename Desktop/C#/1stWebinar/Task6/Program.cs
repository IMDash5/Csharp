// задача на вывод всех целых чисел в промежутке
// перевести в стринг и записать через запятую
Console.Write("Введите число: ");
string str_N = Console.ReadLine();
int N = int.Parse(str_N);

int N1 = -N;
string ans = " ";

while (N1 <= N){
    ans = ans + $"{N1}, ";
    N1 = N1 + 1;
}
Console.WriteLine($"Ответ: {ans}");
