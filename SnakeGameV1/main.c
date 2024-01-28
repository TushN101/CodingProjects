//Made by using following a tutorial
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <unistd.h>
int height = 20,width = 20; //for the setup of the windows
int x , y,dir; // for the snake position and its direction
int gameover=0;//for checking if the game is over or not
int fruitx , fruity; //for fruit position
int score=0;//showing the score
void logic() //Has the reactions to input and other logically stuffs
{
    sleep(0.1); // kind off like update speed??
    switch(dir)//Switching based off input
    {
    case 1:
        x--;
        break;
    case 2:
        x++;
        break;
    case 3:
        y--;
        break;
    case 4:
        y++;
        break;
    }

    if(x==fruitx && y==fruity) //basically making new fruit if snakes eat the old fruits
    {
        score += 10;
        newfruit_x://setting the x position of the new fruit
            fruitx=rand()%20;
            if(fruitx==0)
                goto newfruit_x;
        newfruit_y://setting the y position of the new fruit
            fruity=rand()%20;
            if(fruity==0)
                goto newfruit_y;
    }
    if(x==height)
    {
        gameover=1;
    }
    if(y==width)
    {
        y=1;
    }

}
void input()//deals with input
{
    if(kbhit())//kbhit checks for input
    {
        switch(getch())//switches with cases based off input
        {
        case 'w':
            dir=1;
            break;
        case 's':
            dir=2;
            break;
        case 'a':
            dir=3;
            break;
        case 'd':
            dir=4;
            break;
        case 'q':
            gameover=1;
            break;
        }
    }
}
void snake() // deals with og snake and og fruit position
{
    x=height/2;
    y=width/2;
    fruit_x: //makes the fruits x position originally
        fruitx=rand()%20;
        if(fruitx==0)
            goto fruit_x;
    fruit_y: //makes the fruits y position orignal
        fruity=rand()%20;
        if(fruity==0)
            goto fruit_y;
}
void setup() //setup = more like a display screen or a scene
{
    system("cls");//clearing the scene so it feels updating
    for(int i=0;i<height;i++)//for loop for making a boundary
    {for(int j=0;j<width;j++)
        {
            if(i==0 || i==height-1 || j==0 || j==width-1)
            {
                printf("#");
            }
            else{
                if(i==x && j==y)
                {
                    printf("0");
                }
                else if(i==fruitx && j==fruity)
                {
                    printf("*");
                }
                else{
                printf(" ");
                }
            }
        }
        printf("\n");
    }
    printf("Score %d \n",score);
    printf("Press Q to quit");
}
void main()
{
    snake();
    while(!gameover)
    {
    setup();
    input();
    logic();
    }

}


