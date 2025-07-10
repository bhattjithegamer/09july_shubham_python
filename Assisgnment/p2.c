#include <stdio.h>

// dessending

int main()
{
   int num[5] = {7, 80, 5, 12, 9};
   int i, j, a;

   for (i = 0; i < 5; i++)
   {
      for (j = 0; j < 5; j++)
      {
         if (num[i] > num[j])

         {
            a = num[i];
            num[i] = num[j];
            num[j] = a;
         }
      }
   }

   for (i = 0; i < 5; i++)
   {
      printf("%d", num[i]);
   }

   return 0;
}