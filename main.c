#include <stdio.h>

struct User {
    char username[50];
    char password[50];
    // Add other user information as needed
};

int main() {
    // Create a user structure and get input (you can modify this part as needed)
    struct User newUser;
    printf("Enter username: ");
    scanf("%[^\n]", newUser.username);
    printf("Enter password: ");
    scanf("%s", newUser.password);

    // Open the file for writing, replace ".users.txt" with your desired file name
    FILE *file = fopen(".users.txt", "a");  // "a" for append mode

    // Check if the file is successfully opened
    if (file == NULL) {
        perror("Error opening the file");
        return 1;
    }

    // Write the user data to the file
    fprintf(file, "Username: %s\nPassword: %s\n\n", newUser.username, newUser.password);

    // Close the file
    fclose(file);

    printf("User registration successful.\n");

    int num;
    printf("Press 2 to see the content of the file: ");
    scanf("%d", &num);

    if (num == 2) {
        // Open the file for reading
        file = fopen(".users.txt", "r");

        // Check if the file is successfully opened
        if (file == NULL) {
            perror("Error opening the file");
            return 1;
        }

        // Read and display the content of the file
        char ch;
        while ((ch = fgetc(file)) != EOF) {
            putchar(ch);
        }

        // Close the file
        fclose(file);
    }

    return 0;
}
  