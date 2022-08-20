using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace proRandomNumberGen
{
    class Program
    {
        static void Main(string[] args)
        {
            int randomNumber;

            Console.WriteLine("Welcome  to the Number Generator Program!");

            Random randm = new Random();        
            randomNumber = randm.Next(1 , 100);         //This generates our random number. We have to change our range in the IDE.

            Console.WriteLine("The winner is " + randomNumber  + ". Congratulions!");
            Console.ReadKey();

        }
    }
}
