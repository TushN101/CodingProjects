//Coded in Notepad 
//Dated 18/1/24
//Code was Formatted using codebeutify.org
//Repetive code was generated using GPT


#include <stdio.h>

#include <conio.h>

#include <string.h>

#include <stdlib.h>

#include <windows.h>


struct person {
    char first_name[20];
    char last_name[20];
    int age;
};

void addrecord(struct person records[], int * count);

void viewrecord(struct person records[], int * count);

void remrecord(struct person records[], int * count);

void writeToFile(struct person records[], int count) {
    FILE * file = fopen("records.txt", "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        fprintf(file, "%s %s %d\n", records[i].first_name, records[i].last_name, records[i].age);
    }

    fclose(file);
    printf("Data saved to file.\n");
}

void readFromFile(struct person records[], int * count) {
    FILE * file = fopen("records.txt", "r");
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }

    * count = 0; 
    while (fscanf(file, "%s %s %d", records[ * count].first_name, records[ * count].last_name, & records[ * count].age) == 3) {
        ( * count) ++;
    }

    fclose(file);
    printf("Data loaded from file.\n");
}

void main() {
    struct person records[100];
    int count = 0;
    int choice;
    readFromFile(records, & count);
    while (choice != 4) {
        printf("---------------------------------\n");
        printf("Record Management System \n");
        printf("1.Add a Record \n");
        printf("2.Remove a Record \n");
        printf("3.View a Record \n");
        printf("4.Exit \n");
        printf("Enter your choice : ");
        scanf("%d", & choice);
        switch (choice) {
        case 1:
            addrecord(records, & count);
            break;
        case 2:
            remrecord(records, & count);
            break;
        case 3:
            viewrecord(records, & count);
            break;
        case 4:
            writeToFile(records, count);
            exit(0);
        }
    }
}

void addrecord(struct person records[], int * count) {
    printf("---------------------------------\n");
    printf("Enter its first name: ");
    scanf("%s", & records[ * count].first_name);
    printf("Enter its last name: ");
    scanf("%s", & records[ * count].last_name);
    printf("Enter its age: ");
    scanf("%d", & records[ * count].age);
    ( * count) ++;
    printf("Record saved succesfully \n\n");
    return;

}

void remrecord(struct person records[], int * count) {
    int remove_choice;
    char remove_first_name[20];
    char remove_last_name[20];
    int remove_age;
    printf("---------------------------------\n");
    printf("\nEnter the way you want to remove\n");
    printf("1.Remove Via First Name \n");
    printf("2.Remove Via Last Name \n");
    printf("3.Remove Via Age \n");
    printf("Enter your choice : ");
    scanf("%d", & remove_choice);

    switch (remove_choice) {
    case 1:
        printf("---------------------------------\n");
        printf("Enter the first name: ");
        scanf("%s", remove_first_name);

        for (int i = 0; i < * count; i++) {
            if (strcmp(strlwr(records[i].first_name), strlwr(remove_first_name)) == 0) {
                printf("\nRecord found:-\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);

                int confirm;
                printf("\nDo you want to remove this record? (1.Yes / 2.No): ");
                scanf("%d", & confirm);
                if (confirm == 1) {
                    for (int j = i; j < * count - 1; j++) {
                        strcpy(records[j].first_name, records[j + 1].first_name);
                        strcpy(records[j].last_name, records[j + 1].last_name);
                        records[j].age = records[j + 1].age;
                    }
                    ( * count) --;
                    printf("Record removed successfully.\n");
                } else {
                    printf("Record removal canceled.\n");
                }
                return;
            }
        }
        printf("No records found with the specified first name.\n");
        break;
    case 2:
        printf("---------------------------------\n");
        printf("Enter the last name: ");
        scanf("%s", remove_last_name);
        for (int i = 0; i < * count; i++) {
            if (strcmp(strlwr(records[i].last_name), strlwr(remove_last_name)) == 0) {
                printf("\nRecord found:-\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);
                int confirm;
                printf("\nDo you want to remove this record? (1.Yes / 2.No): ");
                scanf("%d", & confirm);
                if (confirm == 1) {
                    for (int j = i; j < * count - 1; j++) {
                        strcpy(records[j].first_name, records[j + 1].first_name);
                        strcpy(records[j].last_name, records[j + 1].last_name);
                        records[j].age = records[j + 1].age;
                    }
                    ( * count) --;
                    printf("Record removed successfully.\n");
                } else {
                    printf("Record removal canceled.\n");
                }
                return;
            }
        }
        printf("No records found with the specified last name.\n");
        break;

    case 3:
        printf("---------------------------------\n");
        printf("Enter the age: ");
        scanf("%d", & remove_age);

        for (int i = 0; i < * count; i++) {
            if (records[i].age == remove_age) {
                printf("\nRecord found:-\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);
                int confirm;
                printf("\nDo you want to remove this record? (1.Yes / 2.No): ");
                scanf("%d", & confirm);

                if (confirm == 1) {
                    for (int j = i; j < * count - 1; j++) {
                        strcpy(records[j].first_name, records[j + 1].first_name);
                        strcpy(records[j].last_name, records[j + 1].last_name);
                        records[j].age = records[j + 1].age;
                    }
                    ( * count) --;
                    printf("Record removed successfully.\n");
                } else {
                    printf("Record removal canceled.\n");
                }
                return;
            }
        }
        printf("No records found with the specified age.\n");
        break;

    default:
        printf("Invalid choice.\n");
    }
    return;
}

void viewrecord(struct person records[], int * count) {
    int search_choice;
    int rec_no;
    char search_first_name[20];
    char search_last_name[20];
    char temp_casing[20];
    int search_age;
    printf("---------------------------------\n");
    printf("\nEnter the way you want to search\n");
    printf("1.Search Via Record No. \n");
    printf("2.Search Via First Name \n");
    printf("3.Search Via Last Name \n");
    printf("4.Search Via Age \n");
    printf("Enter your choice : ");
    scanf("%d", & search_choice);
    switch (search_choice) {
    case 1:
        printf("---------------------------------\n");
        printf("Enter the record no. you want to search for: ");
        scanf("%d", & rec_no);
        if (rec_no >= 1 && rec_no <= * count) {
            printf("\nRecord found:_\n");
            printf("Record Number: %d\n", rec_no);
            printf("First Name: %s\n", records[rec_no - 1].first_name);
            printf("Last Name: %s\n", records[rec_no - 1].last_name);
            printf("Age: %d\n", records[rec_no - 1].age);

        } else {
            printf("No such records were found\n");
        }
        return;
        break;

    case 2:
        printf("---------------------------------\n");
        printf("Enter the first name to search for: ");
        scanf("%s", search_first_name);

        int recordFoundFirstName = 0;

        for (int i = 0; i < * count; i++) {
            strcpy(temp_casing, records[i].first_name);
            if (strcmp(strlwr(temp_casing), strlwr(search_first_name)) == 0) {
                printf("\nRecord found:-\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);
                recordFoundFirstName = 1;
            }
        }

        
        if (recordFoundFirstName) {
            printf("Now exiting view mode \n \n");
        } else {
            printf("No records found with the specified first name.\n");
        }
        return;
        break;

    case 3:
        printf("---------------------------------\n");
        printf("Enter the last name to search for: ");
        scanf("%s", search_last_name);

       
        int recordFoundLastName = 0;

        for (int i = 0; i < * count; i++) {
           
            strcpy(temp_casing, records[i].last_name);
            strlwr(temp_casing);

            if (strcmp(temp_casing, strlwr(search_last_name)) == 0) {
                printf("\nRecord found:\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);
                recordFoundLastName = 1;
            }
        }
    
        if (recordFoundLastName) {
            printf("Now exiting view mode \n \n");
        } else {
            printf("No records found with the specified last name.\n");
        }
        return;
        break;

    case 4:
        printf("---------------------------------\n");
        printf("Enter the age to search for: ");
        scanf("%d", & search_age);
        int recordFound = 0;
        for (int i = 0; i < * count; i++) {
            if (records[i].age == search_age) {
                printf("\nRecord found:\n");
                printf("Record Number: %d\n", i + 1);
                printf("First Name: %s\n", records[i].first_name);
                printf("Last Name: %s\n", records[i].last_name);
                printf("Age: %d\n", records[i].age);
                recordFound = 1;
            }
        }
        
        if (recordFound) {
            printf("Now exiting view mode \n \n");
        } else {
            printf("No records found with the specified age.\n");
        }
        return;
        break;

    }

}