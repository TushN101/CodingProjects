#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int get_1st_weekday(int year) //function to find the week of the first day of januaray using year
{
    int day;//declaring a day variable

    day = (((year - 1) * 365) + ((year - 1) / 4) - ((year - 1) / 100) + ((year) / 400) + 1) % 7; //Zeller algorithm to find the first day of first week in jan

    return day;//returning the day
}
int main()
{
    int year,daysinmonth,weekdays=0,startingday;//declaring necessary variable

    system("Color 1F");//setting the color to a new type of background

    printf("Enter the year: ");

    scanf("%d",&year);//Taking the year input

    char *months[]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    //declaring the character array month

    int monthday[] ={31,28,31,30,31,30,31,31,30,31,30,31};
    //declaring the int array of number of days in the month

    if((year%4==0&&year%100!=0)||year%400==0){//if condition to check if the year is a leap year

        monthday[1]=29;//changing the number of days to 29 in case of a leap year

    }

    startingday=get_1st_weekday(year);//getting the day which will be the starting day by calling the function

    for(int month=0;month<12;month++) //outer for loop
        {
            printf("\n\n----------------%s----------------",months[month]);//printing all the months

            printf("\n Sun  Mon  Tue  Wed  Thu  Fri  Sat\n");//printing the weeks

            daysinmonth=monthday[month];//declaring the number of days in the month using  month days array

            for(weekdays=0;weekdays<startingday;weekdays++){

                    printf("     ");//To shift the day to start of the month day

                }

            for(int day=1;day<=daysinmonth;day++)//For loop for printing the days
                {

                printf("%5d",day);//padding spacing of 5 spaces for printing days

                if(++weekdays>6){//if loop to increment the weekdays

                    printf("\n");//printing a new line after printing all the days and move the next line

                    weekdays=0;//reset the value of Weekdays

                    }startingday=weekdays;//so that the next month will have spaces to accord to perfect weekday for the day
                }
        }
        getch();
        return 0;
        
}

