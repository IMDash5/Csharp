int Prompt(string message)
{
    Console.WriteLine(message);
    string StrCord = Console.ReadLine();
    int cord = int.Parse(StrCord);
    return cord;
}

int x = Prompt("Введите х: ");
int y = Prompt("Введите y: ");

int quarter = 0;
int answer = 0;

int Quart(int cordX, int cordY)
{
    if (cordX > 0)
    {
        if (cordY > 0)
        {
            quarter = 1;
        }
        else 
        {
            quarter = 4;
        }
    }
    else 
    {
        if (cordY > 0)
        {
            quarter = 2;
        }
        else 
        {
            quarter = 3;
        }
    }
    return quarter;
}

if (x == 0 || y ==0)
{
    Console.WriteLine("Одна из координат равна нулю");
}
else 
{
    answer = Quart(x, y);
    Console.WriteLine(answer);
}
